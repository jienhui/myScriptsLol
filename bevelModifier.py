from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as mui
import maya.cmds as cmds
from shiboken import wrapInstance

def mayaMainWindow():
    mainWindow= mui.MQtUtil.mainWindow()
    return wrapInstance(long(mainWindow), QWidget)
    
class Form(QDialog):
    def __init__(self, parent=mayaMainWindow()):
        super(Form, self).__init__()
        # UI layout
        bmLayout= QGridLayout()
        PosXBttn= QPushButton( "+  X" )
        NegXBttn= QPushButton( "-  X" )
        PosYBttn= QPushButton( "+  Y" )
        PosZBttn= QPushButton( "+  Z" )
        NegZBttn= QPushButton( "-  Z" )
        
        bmLayout.addWidget( PosXBttn, 0, 0 )
        bmLayout.addWidget( NegXBttn, 0, 1 )
        bmLayout.addWidget( PosYBttn, 1, 0 )
        bmLayout.addWidget( PosZBttn, 2, 0 )
        bmLayout.addWidget( NegZBttn, 2, 1 )
        self.setLayout( bmLayout )
        self.setWindowFlags( Qt.WindowStaysOnTopHint )
        self.setWindowTitle( "Bevel Modifier v1.0" )
        
        # Signal
        PosXBttn.clicked.connect( self.posX )
        NegXBttn.clicked.connect( self.negX )
        PosYBttn.clicked.connect( self.posY )
        PosZBttn.clicked.connect( self.posZ )
        NegZBttn.clicked.connect( self.negZ )
        
    # Bevel Modifier Function
    def posX(self):
        
        selVert= cmds.ls( sl=1, fl=1 )
        vertParent= cmds.listRelatives( cmds.listRelatives(selVert[0], p=1), p=1 )
        tmpClu= cmds.cluster()[1]
        vertPosX=[]
        
        # get vertices position
        for vert in selVert:
            vertPos= cmds.xform( vert, q=1, ws=1, t=1 )
            vertPosX.append( vertPos[0] )
        
        # get highest value for each direction    
        maxPosX= max( vertPosX )
        
        # use loctor as a template pivot
        tmpLoc= cmds.spaceLocator( n="tmpPivLoc" )[0]
        tmpCnst= cmds.parentConstraint( vertParent, tmpLoc, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parent( tmpLoc, vertParent )
        cmds.xform( tmpLoc, t= [maxPosX, 0 , 0] )
        locPos= cmds.xform( tmpLoc, q=1, ws=1, t=1 )
        cmds.xform( tmpClu, piv= locPos )
        cmds.setAttr( "%s.sx" % tmpClu, 0.1 )
        cmds.delete( vertParent, ch=1 )
        cmds.delete( tmpLoc )
        cmds.select( selVert )
        
    def negX(self):
        
        selVert= cmds.ls( sl=1, fl=1 )
        vertParent= cmds.listRelatives( cmds.listRelatives(selVert[0], p=1), p=1 )
        tmpClu= cmds.cluster()[1]
        vertPosX=[]
        
        # get vertices position
        for vert in selVert:
            vertPos= cmds.xform( vert, q=1, ws=1, t=1 )
            vertPosX.append( vertPos[0] )
        
        # get highest value for each direction    
        minPosX= mix( vertPosX )
        
        # use loctor as a template pivot
        tmpLoc= cmds.spaceLocator( n="tmpPivLoc" )[0]
        tmpCnst= cmds.parentConstraint( vertParent, tmpLoc, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parent( tmpLoc, vertParent )
        cmds.xform( tmpLoc, t= [mixPosX, 0 , 0] )
        locPos= cmds.xform( tmpLoc, q=1, ws=1, t=1 )
        cmds.xform( tmpClu, piv= locPos )
        cmds.setAttr( "%s.sx" % tmpClu, 0.1 )
        cmds.delete( vertParent, ch=1 )
        cmds.delete( tmpLoc )
        cmds.select( selVert )
        
    def posY(self):
        
        selVert= cmds.ls( sl=1, fl=1 )
        vertParent= cmds.listRelatives( cmds.listRelatives(selVert[0], p=1), p=1 )
        tmpClu= cmds.cluster()[1]
        vertPosY=[]
        
        # get vertices position
        for vert in selVert:
            vertPos= cmds.xform( vert, q=1, ws=1, t=1 )
            vertPosY.append( vertPos[1] )
        
        # get highest value for each direction    
        maxPosY= max( vertPosY )
        
        # use loctor as a template pivot
        tmpLoc= cmds.spaceLocator( n="tmpPivLoc" )[0]
        tmpCnst= cmds.parentConstraint( vertParent, tmpLoc, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parent( tmpLoc, vertParent )
        cmds.xform( tmpLoc, t= [0, maxPosY , 0] )
        locPos= cmds.xform( tmpLoc, q=1, ws=1, t=1 )
        cmds.xform( tmpClu, piv= locPos )
        cmds.setAttr( "%s.sy" % tmpClu, 0.1 )
        cmds.delete( vertParent, ch=1 )
        cmds.delete( tmpLoc )
        cmds.select( selVert )
        
    def posZ(self):
        
        selVert= cmds.ls( sl=1, fl=1 )
        vertParent= cmds.listRelatives( cmds.listRelatives(selVert[0], p=1), p=1 )
        tmpClu= cmds.cluster()[1]
        vertPosZ=[]
        
        # get vertices position
        for vert in selVert:
            vertPos= cmds.xform( vert, q=1, ws=1, t=1 )
            vertPosZ.append( vertPos[2] )
        
        # get highest value for each direction    
        maxPosZ= max( vertPosZ )
        
        # use loctor as a template pivot
        tmpLoc= cmds.spaceLocator( n="tmpPivLoc" )[0]
        tmpCnst= cmds.parentConstraint( vertParent, tmpLoc, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parent( tmpLoc, vertParent )
        cmds.xform( tmpLoc, t= [0, 0 , maxPosZ] )
        locPos= cmds.xform( tmpLoc, q=1, ws=1, t=1 )
        cmds.xform( tmpClu, piv= locPos )
        cmds.setAttr( "%s.sz" % tmpClu, 0.1 )
        cmds.delete( vertParent, ch=1 )
        cmds.delete( tmpLoc )
        cmds.select( selVert )
        
    def negZ(self):
        
        selVert= cmds.ls( sl=1, fl=1 )
        vertParent= cmds.listRelatives( cmds.listRelatives(selVert[0], p=1), p=1 )
        tmpClu= cmds.cluster()[1]
        vertPosZ=[]
        
        # get vertices position
        for vert in selVert:
            vertPos= cmds.xform( vert, q=1, ws=1, t=1 )
            vertPosZ.append( vertPos[2] )
        
        # get highest value for each direction    
        minPosZ= min( vertPosZ )
        
        # use loctor as a template pivot
        tmpLoc= cmds.spaceLocator( n="tmpPivLoc" )[0]
        tmpCnst= cmds.parentConstraint( vertParent, tmpLoc, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parent( tmpLoc, vertParent )
        cmds.xform( tmpLoc, t= [0, 0, minPosZ] )
        locPos= cmds.xform( tmpLoc, q=1, ws=1, t=1 )
        cmds.xform( tmpClu, piv= locPos )
        cmds.setAttr( "%s.sz" % tmpClu, 0.1 )
        cmds.delete( vertParent, ch=1 )
        cmds.delete( tmpLoc )
        cmds.select( selVert )

if __name__ == "__main__":
    haha= Form()
    haha.show()
        
        
