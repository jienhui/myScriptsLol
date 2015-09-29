import maya.OpenMayaUI as mui
from math import *
from PySide.QtCore import *
from PySide.QtGui import *
from shiboken import wrapInstance

def mayaMainWindow():
    mainWindow = mui.MQtUtil.mainWindow()
    return wrapInstance( long(mainWindow), QWidget )

class Form(QDialog):
    def __init__(self, parent=mayaMainWindow):
        super(Form, self).__init__()
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect(self.lineedit, SIGNAL("returnPressed()"),self.updateUi)
        self.setWindowTitle("Calculate")
        
    def updateUi(self):
        try:
            text = unicode(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)
            
if __name__ == "__main__":
    f= Form()
    f.show()
