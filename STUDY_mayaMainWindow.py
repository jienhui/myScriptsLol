import maya.OpenMayaUI as mui
from PySide import QtCore
from PySide import QtGui
from shiboken import wrapInstance

def mayaMainWindow():
    mainWindow = mui.MQtUtil.mainWindow()
    return wrapInstance( long(mainWindow), QtGui.QWidget )
    
def form():
    label = QtGui.QLabel( "Hellow, World!", parent= mayaMainWindow() )
    label.setWindowFlags( QtCore.Qt.Window )
    label.show()
    
if __name__ == "__main__":
    form()
