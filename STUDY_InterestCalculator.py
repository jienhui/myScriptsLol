from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as mui
from shiboken import wrapInstance

def mayaMainWindow():
    mainWindow = mui.MQtUtil.mainWindow()
    return wrapInstance( long(mainWindow), QWidget )

class Form(QDialog):    
    def __init__( self, parent=mayaMainWindow() ):
        super( Form, self ).__init__()
        # Create widgets
        principal_label = QLabel( "Principal:" )
        self.principalSpinBox= QDoubleSpinBox()
        self.principalSpinBox.setPrefix( "$ " )
        self.principalSpinBox.setRange( 0.01, 10000000.00 )
        self.principalSpinBox.setValue( 2000.00 )
        rate_label = QLabel( "Rate:" )
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setSuffix( "%" )
        self.rateSpinBox.setRange( 0.01, 100.00 )
        self.rateSpinBox.setValue( 5.25 )
        years_label = QLabel( "Years:" )
        self.yearsComboBox = QComboBox()
        for each in range(1,101):
            self.yearsComboBox.addItem( "%s years" % each )
        amount_label = QLabel( "Amount:" )
        self.output_label = QLabel()
        # Layout
        grid = QGridLayout()
        grid.addWidget( principal_label, 0, 0 )
        grid.addWidget( self.principalSpinBox, 0, 1 )
        grid.addWidget( rate_label, 1, 0 )
        grid.addWidget( self.rateSpinBox, 1, 1 )
        grid.addWidget( years_label, 2, 0 )
        grid.addWidget( self.yearsComboBox, 2, 1 )
        grid.addWidget( amount_label, 3, 0 )
        grid.addWidget( self.output_label, 3, 1 )
        self.setLayout( grid )
        self.setWindowFlags(  Qt.WindowStaysOnTopHint )
        # Signal
        self.connect(self.principalSpinBox,
                     SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.rateSpinBox,
                     SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.yearsComboBox,
                SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.setWindowTitle( "Interest" )
        self.updateUi()
    
    # Functions
    def updateUi(self):
        """Calculates compound interest"""
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value()
        years = self.yearsComboBox.currentIndex() + 1
        amount = principal * ((1 + (rate / 100.0)) ** years)
        self.output_label.setText("$ %.2f" % amount)
        
if __name__ == "__main__":
    m= Form()
    m.show()
