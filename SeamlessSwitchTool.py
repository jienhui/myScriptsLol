from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as mui
import maya.cmds as cmds
from shiboken import wrapInstance

########################################################################################### 

# Main UI
def mayaMainWindow():
    mainWindow= mui.MQtUtil.mainWindow()
    return wrapInstance(long(mainWindow), QWidget)

class Form(QDialog):
    def __init__(self, parent=mayaMainWindow()):
        super(Form, self).__init__()
        # Layout
        mainLayout= QVBoxLayout()
        mainLayout.setSpacing(5)
        gridLayout= QGridLayout()
        addCharLayout= QHBoxLayout()
        self.chrLE= QLineEdit()
        self.chrLE.setText( "Select any controller . . ." )
        self.chrLE.setStyleSheet("color: Grey ")
        self.chrLE.setPlaceholderText( "Select any controller . . ." )
        self.chrLE.setReadOnly(True)
        self.addBttn= QPushButton( "Add" )
        self.addBttn.clicked.connect( self.addChar )
        self.addBttn.setFixedSize( 50, 20 )
        addCharLayout.addWidget( self.chrLE )
        addCharLayout.addWidget( self.addBttn )
        mainLayout.addLayout( addCharLayout )
        mainLayout.addLayout( gridLayout )
        gridLayout.addWidget( self.rAgrpBox(), 1, 0 )
        gridLayout.addWidget( self.lAgrpBox(), 1, 1 )
        gridLayout.addWidget( self.rLgrpBox(), 2, 0 )
        gridLayout.addWidget( self.lLgrpBox(), 2, 1 )
        gridLayout.setColumnStretch( 0,1 )
        gridLayout.setColumnStretch( 1,1 )
        # Window Structure
        self.setFixedSize( 250, 170 )
        self.setLayout(mainLayout)
        self.setWindowTitle("Seamless IK/FK Switch")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
            
###########################################################################################                    
    def rAgrpBox(self):
               
        rAgbLayout= QVBoxLayout()
        rAgbBox= QGroupBox("Right Arm")
        self.rAswitchBttn= QPushButton( "Switch" )
        rAgbLayout.addWidget( self.rAswitchBttn )
        
        rAgbBox.setLayout( rAgbLayout )
        
        self.rAswitchBttn.clicked.connect( self.rArmSwitch )
        return rAgbBox
        
    def lAgrpBox(self):
               
        lAgbLayout= QVBoxLayout()
        lAgbBox= QGroupBox("Left Arm")
        self.lAswitchBttn= QPushButton("Switch")
        lAgbLayout.addWidget( self.lAswitchBttn )
        
        lAgbBox.setLayout( lAgbLayout )    
        
        self.lAswitchBttn.clicked.connect( self.lArmSwitch )
        return lAgbBox
        
    def rLgrpBox(self):
               
        rLgbLayout= QVBoxLayout()
        rLgbBox= QGroupBox("Right Leg")
        self.rLswitchBttn= QPushButton("Switch")
        rLgbLayout.addWidget( self.rLswitchBttn ) 
        
        rLgbBox.setLayout( rLgbLayout )    

        self.rLswitchBttn.clicked.connect( self.rLegSwitch )
        return rLgbBox
    
    def lLgrpBox(self):
               
        lLgbLayout= QVBoxLayout()
        lLgbBox= QGroupBox("Left Leg")
        self.lLswitchBttn= QPushButton("Switch")
        lLgbLayout.addWidget( self.lLswitchBttn )
        
        lLgbBox.setLayout( lLgbLayout )
        
        self.lLswitchBttn.clicked.connect( self.lLegSwitch )
        return lLgbBox

###########################################################################################
    # Add Character Function
    def addChar( self ):
        
        selCtrl= cmds.ls( sl=1 )
        
        if len(selCtrl) == 1 :
            self.nameSpace= str(selCtrl[0]).split( ":" )[0]
            charName= str(self.nameSpace).split( "_" )
            self.chrLE.setText( charName[0] )
            self.chrLE.setStyleSheet("color: medium grey")
            self.chrLE.setStyleSheet("background-color: green")
            self.prefix= self.nameSpace + ":"
            # RightArm button set text
            if cmds.getAttr("%s:R_arm_extra_CTL.ikFKSwitch" % self.nameSpace) == 1:
                self.rAswitchBttn.setStyleSheet("background-color: grey ")
                self.rAswitchBttn.setText( "FK" )
            else:
                self.rAswitchBttn.setStyleSheet("background-color: dark grey ")
                self.rAswitchBttn.setText( "IK" )
            # LeftArm button set text
            if cmds.getAttr("%s:L_arm_extra_CTL.ikFKSwitch" % self.nameSpace) == 1:
                self.lAswitchBttn.setStyleSheet("background-color: grey ")
                self.lAswitchBttn.setText( "FK" )
            else:
                self.lAswitchBttn.setStyleSheet("background-color: dark grey ")
                self.lAswitchBttn.setText( "IK" )
            # RightLeg button set text
            if cmds.getAttr("%s:R_leg_extra_CTL.ikFKSwitch" % self.nameSpace) == 1:
                self.rLswitchBttn.setStyleSheet("background-color: grey ")
                self.rLswitchBttn.setText( "FK" )
            else:
                self.rLswitchBttn.setStyleSheet("background-color: dark grey ")
                self.rLswitchBttn.setText( "IK" )
            # Left Leg button set text
            if cmds.getAttr("%s:L_leg_extra_CTL.ikFKSwitch" % self.nameSpace) == 1:
                self.lLswitchBttn.setStyleSheet("background-color: grey ")
                self.lLswitchBttn.setText( "FK" )
            else:
                self.lLswitchBttn.setStyleSheet("background-color: dark grey ")
                self.lLswitchBttn.setText( "IK" ) 
        elif len(selCtrl) > 1 :
            cmds.warning( "Please select ONE controller only! " )
        else:
            cmds.warning( "Please select any controller! " )
              
###########################################################################################
    # IkFK Seamless Switching Tools Function 
    def lArmSwitch( self ):
        switchValue= cmds.getAttr("%sL_arm_extra_CTL.ikFKSwitch" % self.prefix)
        if switchValue == 0 :
            self.cSwitchToFK_Fn(["%sL_shoulder_FK01_CTL" % self.prefix, "%sL_elbow_FK01_CTL" % self.prefix, "%sL_wrist_FK01_CTL" % self.prefix], ["%sL_shoulder_IK01" % self.prefix, "%sL_elbow_IK01" % self.prefix, "%sL_wrist_IK01" % self.prefix, "%sL_wrist_IK02" % self.prefix])
            cmds.setAttr( "%sL_arm_extra_CTL.ikFKSwitch"  % self.prefix, 1 )
            self.lAswitchBttn.setStyleSheet("background-color: grey ")
            self.lAswitchBttn.setText( "FK" )
            print "Switched Left Arm To FK.",
        else:
            self.cSwitchToIK_Fn(["%sL_shoulder_IK01_CTL" % self.prefix, "%sL_arm_pv_CTL" % self.prefix, "%sL_armIK_CTL" % self.prefix], ["%sL_shoulder_FK01" % self.prefix, "%sL_elbow_FK01" % self.prefix, "%sL_wrist_FK01" % self.prefix])
            cmds.setAttr( "%sL_arm_extra_CTL.ikFKSwitch" % self.prefix, 0 )
            self.lAswitchBttn.setStyleSheet("background-color: dark grey ")
            self.lAswitchBttn.setText( "IK" )
            print "Switched Left Arm To IK.",
    
    def rArmSwitch(self):
        switchValue= cmds.getAttr("%sR_arm_extra_CTL.ikFKSwitch" % self.prefix)
        if switchValue == 0 :
            self.cSwitchToFK_Fn(["%sR_shoulder_FK01_CTL" % self.prefix, "%sR_elbow_FK01_CTL" % self.prefix, "%sR_wrist_FK01_CTL" % self.prefix], ["%sR_shoulder_IK01" % self.prefix, "%sR_elbow_IK01" % self.prefix, "%sR_wrist_IK01" % self.prefix, "%sR_wrist_IK02" % self.prefix])
            cmds.setAttr( "%sR_arm_extra_CTL.ikFKSwitch" % self.prefix, 1 )
            self.rAswitchBttn.setStyleSheet("background-color: grey ")
            self.rAswitchBttn.setText( "FK" )
            print "Switched Right Arm To FK.", 
        else:
            self.cSwitchToIK_Fn(["%sR_shoulder_IK01_CTL" % self.prefix, "%sR_arm_pv_CTL" % self.prefix, "%sR_armIK_CTL" % self.prefix], ["%sR_shoulder_FK01" % self.prefix, "%sR_elbow_FK01" % self.prefix, "%sR_wrist_FK01" % self.prefix])
            cmds.setAttr( "%sR_arm_extra_CTL.ikFKSwitch" % self.prefix, 0 )
            self.rAswitchBttn.setStyleSheet("background-color: dark grey ")
            self.rAswitchBttn.setText( "IK" )
            print "Switched Right Arm To IK.",
    
    def lLegSwitch(self):
        switchValue= cmds.getAttr( "%sL_leg_extra_CTL.ikFKSwitch" % self.prefix )
        if switchValue == 0 :
            self.cSwitchToFK_Fn(["%sL_hip_FK01_CTL" % self.prefix, "%sL_knee_FK01_CTL" % self.prefix, "%sL_ankle_FK01_CTL" % self.prefix], ["%sL_hip_IK01" % self.prefix, "%sL_knee_IK01" % self.prefix, "%sL_ankle_IK01" % self.prefix, "%sL_ankle_IK02" % self.prefix])
            cmds.setAttr( "%sL_leg_extra_CTL.ikFKSwitch" % self.prefix, 1 )
            self.lLswitchBttn.setStyleSheet("background-color: grey ")
            self.lLswitchBttn.setText( "FK" )
            print "Switched Left Leg To FK.",
        else:
            self.cSwitchToIK_Fn(["%sL_hip_IK01_CTL" % self.prefix, "%sL_leg_pv_CTL" % self.prefix, "%sL_legIK_CTL" % self.prefix], ["%sL_hip_FK01" % self.prefix, "%sL_knee_FK01" % self.prefix, "%sL_ankle_FK01" % self.prefix])
            cmds.setAttr( "%sL_leg_extra_CTL.ikFKSwitch" % self.prefix, 0 )
            self.lLswitchBttn.setStyleSheet("background-color: dark grey ")
            self.lLswitchBttn.setText( "IK" )
            print "Switched Left Leg To IK.",
    
    def rLegSwitch(self):    
        switchValue= cmds.getAttr("%sR_leg_extra_CTL.ikFKSwitch" % self.prefix )
        if switchValue == 0 :
            self.cSwitchToFK_Fn(["%sR_hip_FK01_CTL" % self.prefix, "%sR_knee_FK01_CTL" % self.prefix, "%sR_ankle_FK01_CTL" % self.prefix], ["%sR_hip_IK01" % self.prefix, "%sR_knee_IK01" % self.prefix, "%sR_ankle_IK01" % self.prefix, "%sR_ankle_IK02" % self.prefix])
            cmds.setAttr( "%sR_leg_extra_CTL.ikFKSwitch" % self.prefix, 1 )
            self.rLswitchBttn.setStyleSheet("background-color: grey ")
            self.rLswitchBttn.setText( "FK" )
            print "Switched Right Leg To FK.",
        else:
            self.cSwitchToIK_Fn(["%sR_hip_IK01_CTL" % self.prefix, "%sR_leg_pv_CTL" % self.prefix, "%sR_legIK_CTL" % self.prefix], ["%sR_hip_FK01" % self.prefix, "%sR_knee_FK01" % self.prefix, "%sR_ankle_FK01" % self.prefix])
            cmds.setAttr( "%sR_leg_extra_CTL.ikFKSwitch" % self.prefix, 0 )
            self.rLswitchBttn.setStyleSheet("background-color: dark grey ")
            self.rLswitchBttn.setText( "IK" )
            print "Switched Right Leg To IK.",
        
    # Switch To FK Function
    def cSwitchToFK_Fn( self, FKCtrlList, IKJntList ):
        self.FKCtrlList= FKCtrlList
        self.IKJntList= IKJntList
        
        if cmds.objExists( self.FKCtrlList[0] )==True:
            if cmds.objExists( self.FKCtrlList[1] )==True:
                if cmds.objExists( self.FKCtrlList[2] )==True:
                    if cmds.objExists( self.IKJntList[0] )==True:
                        if cmds.objExists( self.IKJntList[1] )==True:
                            if cmds.objExists( self.IKJntList[2] )==True:
                                pass
                            else:
                                cmds.warning( "Invalid IK Wrist/Ankle Joint." )
                        else:
                            cmds.warning( "Invalid IK Elbow/Knee Joint." )
                    else:
                        cmds.warning( "Invalid IK Shoulder/Hip Joint." )
                else:
                    cmds.warning( "Invalid FK Wrist/Ankle Controller." )
            else:
                cmds.warning( "Invalid FK Elbow/Knee Controller." )
        else:
            cmds.warning( "Invalid FK Shoulder/Hip Controller." )
        
        # Create Temparary FK Controllers Hierachy
        self.ctrlGrpList=[]
        self.locList=[]
        self.locGrpList= []
        
        for each in self.FKCtrlList:
            ctrlGrp= cmds.listRelatives( each, p=1 )[0]
            self.ctrlGrpList.append( ctrlGrp )
            loc= cmds.spaceLocator( n=str(each).replace( "CTL", "loc" ) )[0]
            self.locList.append( loc )
            locGrp= cmds.group( n="%s_GRP" % loc, em=0 )
            self.locGrpList.append( locGrp )
            tmpCnst= cmds.parentConstraint( ctrlGrp, locGrp, mo=0 )
            cmds.delete( tmpCnst )
        
        tmpCnst= cmds.parentConstraint( self.FKCtrlList[2], self.locGrpList[2], mo=0 )
        cmds.delete( tmpCnst )
        locNum= len( self.locList )
        locGrpNum= len( self.locGrpList )
        
        if locNum == locGrpNum:
            for each in reversed(range(1,locGrpNum)):
                n= each
                cmds.parent( self.locGrpList[n], self.locList[(n-1)] )
                n= n-1
        
        # Mimic IK Shoulder/Hip Position
        tmpCnst=cmds.parentConstraint( self.IKJntList[0], self.locList[0], mo=0 )
        cmds.delete( tmpCnst )
        locAPosX= cmds.getAttr( "%s.tx" % self.locList[0] )
        locAPosY= cmds.getAttr( "%s.ty" % self.locList[0] )
        locAPosZ= cmds.getAttr( "%s.tz" % self.locList[0] )
        locAOrientX= cmds.getAttr( "%s.rx" % self.locList[0] )
        locAOrientY= cmds.getAttr( "%s.ry" % self.locList[0] )
        locAOrientZ= cmds.getAttr( "%s.rz" % self.locList[0] )
        cmds.setAttr( "%s.tx" % self.FKCtrlList[0], locAPosX )
        cmds.setAttr( "%s.ty" % self.FKCtrlList[0], locAPosY )
        cmds.setAttr( "%s.tz" % self.FKCtrlList[0], locAPosZ )
        cmds.setAttr( "%s.rx" % self.FKCtrlList[0], locAOrientX )
        cmds.setAttr( "%s.ry" % self.FKCtrlList[0], locAOrientY )
        cmds.setAttr( "%s.rz" % self.FKCtrlList[0], locAOrientZ )
        
        # Mimic IK Elbow/Knee Position
        tmpCnst=cmds.parentConstraint( self.IKJntList[1], self.locList[1], mo=0 )
        cmds.delete( tmpCnst )
        locBPosX= cmds.getAttr( "%s.tx" % self.IKJntList[1] )
        locBPosY= cmds.getAttr( "%s.ty" % self.IKJntList[1] )
        locBPosZ= cmds.getAttr( "%s.tz" % self.IKJntList[1] )
        locBOrientX= cmds.getAttr( "%s.rx" % self.IKJntList[1] )
        locBOrientY= cmds.getAttr( "%s.ry" % self.IKJntList[1] )
        locBOrientZ= cmds.getAttr( "%s.rz" % self.IKJntList[1] )
        
        if cmds.getAttr( "%s.preferredAngleY" % self.IKJntList[1] ) == -90 :
            ctrlGrpBPosX= cmds.getAttr( "%s.tx" % self.ctrlGrpList[1] )
            cmds.setAttr( "%s.tx" % self.FKCtrlList[1], (locBPosX - ctrlGrpBPosX) )
        else:
            ctrlGrpBPosX= cmds.getAttr( "%s.tx" % self.ctrlGrpList[1] )
            cmds.setAttr( "%s.tx" % self.FKCtrlList[1], (locBPosX + ctrlGrpBPosX) )
        
        if cmds.getAttr( "%s.preferredAngleX" % self.IKJntList[1] ) == 90 :
            ctrlGrpBPosY= cmds.getAttr( "%s.ty" % self.ctrlGrpList[1] )
            cmds.setAttr( "%s.ty" % self.FKCtrlList[1], (locBPosY - ctrlGrpBPosY) )
        else:
            ctrlGrpBPosY= cmds.getAttr( "%s.ty" % self.ctrlGrpList[1] )
            cmds.setAttr( "%s.ty" % self.FKCtrlList[1], (locBPosY + ctrlGrpBPosY) ) 
            
        cmds.setAttr( "%s.tz" % self.FKCtrlList[1], locBPosZ )
        cmds.setAttr( "%s.rx" % self.FKCtrlList[1], locBOrientX )
        cmds.setAttr( "%s.ry" % self.FKCtrlList[1], locBOrientY )
        cmds.setAttr( "%s.rz" % self.FKCtrlList[1], locBOrientZ )
        
        # Mimic IK Wrist/Ankle Position
        if self.IKJntList[2].startswith( "%sL_wrist" % self.prefix ):
            name= "L_arm"
        if self.IKJntList[2].startswith( "%sR_wrist" % self.prefix ):
            name= "R_arm"    
        if self.IKJntList[2].startswith( "%sL_ankle" % self.prefix ):
            name= "L_leg"
        if self.IKJntList[2].startswith( "%sR_ankle" % self.prefix ):
            name= "R_leg"
        ikCTL02= "%s%sIK_CTL" % (self.prefix, name)
        tmpCnst=cmds.parentConstraint( ikCTL02, self.locList[2], mo=0 )
        cmds.delete( tmpCnst )
        locCPosX= cmds.getAttr( "%s.tx" % self.IKJntList[2] )
        locCPosY= cmds.getAttr( "%s.ty" % self.IKJntList[2] )
        locCPosZ= cmds.getAttr( "%s.tz" % self.IKJntList[2] )
        locOrientX= cmds.getAttr( "%s.rx" % self.locList[2] )
        locOrientY= cmds.getAttr( "%s.ry" % self.locList[2] )
        locOrientZ= cmds.getAttr( "%s.rz" % self.locList[2] )
        
        if cmds.getAttr( "%s.preferredAngleY" % self.IKJntList[1] ) == -90 :
            ctrlGrpCPosX= cmds.getAttr( "%s.tx" % self.ctrlGrpList[2] )
            cmds.setAttr( "%s.tx" % self.FKCtrlList[2], (locCPosX - ctrlGrpCPosX) )
        else:
            ctrlGrpCPosX= cmds.getAttr( "%s.tx" % self.ctrlGrpList[2] )
            cmds.setAttr( "%s.tx" % self.FKCtrlList[2], (locCPosX + ctrlGrpCPosX) )
        
        if cmds.getAttr( "%s.preferredAngleX" % self.IKJntList[1] ) == 90 :
            ctrlGrpCPosY= cmds.getAttr( "%s.ty" % self.ctrlGrpList[2] )
            cmds.setAttr( "%s.ty" % self.FKCtrlList[2], (locCPosY - ctrlGrpCPosY) )
        else:
            ctrlGrpCPosY= cmds.getAttr( "%s.ty" % self.ctrlGrpList[2] )
            cmds.setAttr( "%s.ty" % self.FKCtrlList[2], (locCPosY + ctrlGrpCPosY) )  

        cmds.setAttr( "%s.tz" % self.FKCtrlList[2], locCPosZ )
        cmds.setAttr( "%s.rx" % self.FKCtrlList[2], locOrientX )
        cmds.setAttr( "%s.ry" % self.FKCtrlList[2], locOrientY )
        cmds.setAttr( "%s.rz" % self.FKCtrlList[2], locOrientZ )
        
        cmds.delete( self.locGrpList[0] )
                  
    # Switch To IK Function
    def cSwitchToIK_Fn( self, IKCtrlList, FKJntList ):
        self.IKCtrlList= IKCtrlList
        self.FKJntList= FKJntList
        
        if cmds.objExists( self.IKCtrlList[0] )==True:
            if cmds.objExists( self.IKCtrlList[1] )==True:
                if cmds.objExists( self.IKCtrlList[2] )==True:
                    if cmds.objExists( self.FKJntList[0] )==True:
                        if cmds.objExists( self.FKJntList[1] )==True:
                            if cmds.objExists( self.FKJntList[2] )==True:
                                pass
                            else:
                                cmds.warning( "Invalid FK Wrist/Ankle Joint." )
                        else:
                            cmds.warning( "Invalid FK Elbow/Knee Joint." )
                    else:
                        cmds.warning( "Invalid FK Shoulder/Hip Joint." )
                else:
                    cmds.warning( "Invalid IK Wrist/Ankle Controller." )
            else:
                cmds.warning( "Invalid IK Elbow/Knee Controller." )
        else:
            cmds.warning( "Invalid IK Shoulder/Hip Controller." )
        
        # Create Temparary IK Controllers Hierachy
        ctrlGrpList= []
        self.locList=[]
        self.locGrpList= []
        
        for each in self.IKCtrlList:
            ctrlGrp= cmds.listRelatives( each, p=1 )[0]
            ctrlGrpList.append( ctrlGrp )
            loc= cmds.spaceLocator( n=str(each).replace( "CTL", "loc" ) )[0]
            self.locList.append( loc )
            locGrp= cmds.group( n="%s_GRP" % loc, em=0 )
            self.locGrpList.append( locGrp )
            tmpCnst= cmds.parentConstraint( ctrlGrp, locGrp, mo=0 )
            cmds.delete( tmpCnst )
            cmds.select( cl=1 )
        
        # Mimic Shoulder/Hip Joint Position
        tmpCnst= cmds.parentConstraint( self.FKJntList[0], self.locList[0], mo=0 )
        cmds.delete( tmpCnst )
        locAPosX= cmds.getAttr( "%s.tx" % self.locList[0] )
        locAPosY= cmds.getAttr( "%s.ty" % self.locList[0] )
        locAPosZ= cmds.getAttr( "%s.tz" % self.locList[0] )
        locOrientX= cmds.getAttr( "%s.rx" % self.locList[0] )
        locOrientY= cmds.getAttr( "%s.ry" % self.locList[0] )
        locOrientZ= cmds.getAttr( "%s.rz" % self.locList[0] )
        cmds.setAttr( "%s.tx" % self.IKCtrlList[0], locAPosX )
        cmds.setAttr( "%s.ty" % self.IKCtrlList[0], locAPosY )
        cmds.setAttr( "%s.tz" % self.IKCtrlList[0], locAPosZ )
        
        locB= cmds.spaceLocator( n=str(self.IKCtrlList[1]).replace( "CTL", "locB" ) )[0]
        locBGrp= cmds.group( n="%s_GRP" % locB, em=0 ) 
        if self.FKJntList[1].startswith( "%sL_elbow" % self.prefix ):
            cmds.setAttr( "%s.tz" % locB, -80 )
        if self.FKJntList[1].startswith( "%sR_elbow" % self.prefix ):
            cmds.setAttr( "%s.tz" % locB, 80 )
        if self.FKJntList[1].startswith( "%sL_knee" % self.prefix ):
            cmds.setAttr( "%s.tz" % locB, 80 )
        if self.FKJntList[1].startswith( "%sR_knee" % self.prefix ):
            cmds.setAttr( "%s.tz" % locB, -80 )
        tmpCnst= cmds.parentConstraint(self.FKJntList[1], locBGrp, mo=0 )
        cmds.delete( tmpCnst )
        
        # Mimic Elbow/Knee Joint Position
        tmpCnst= cmds.parentConstraint( locB, self.locList[1], mo=0 )
        cmds.delete( tmpCnst )
        locBPosX= cmds.getAttr( "%s.tx" % self.locList[1] )
        locBPosY= cmds.getAttr( "%s.ty" % self.locList[1] )
        locBPosZ= cmds.getAttr( "%s.tz" % self.locList[1] )
        cmds.setAttr( "%s.tx" % self.IKCtrlList[1], locBPosX )
        cmds.setAttr( "%s.ty" % self.IKCtrlList[1], locBPosY )
        cmds.setAttr( "%s.tz" % self.IKCtrlList[1], locBPosZ )
        
        # Hand/Leg CTL Rotation Value
        tmpCnst= cmds.parentConstraint( self.FKJntList[2], self.locList[2], mo=0 )
        cmds.delete( tmpCnst )
        locCPosX= cmds.getAttr( "%s.tx" % self.locList[2] )
        locCPosY= cmds.getAttr( "%s.ty" % self.locList[2] )
        locCPosZ= cmds.getAttr( "%s.tz" % self.locList[2] )
        
        if cmds.getAttr( "%s.preferredAngleY" % self.FKJntList[1] ) == -90:
            locCOrientX= cmds.getAttr( "%s.rx" % self.locList[2] )
            if locCOrientX > 120 :
                locCOrientX= locCOrientX -180
            elif locCOrientX < -120 :
                locCOrientX= locCOrientX +180
            locCOrientY= cmds.getAttr( "%s.ry" % self.locList[2] )
            locCOrientZ= cmds.getAttr( "%s.rz" % self.locList[2] )
        elif cmds.getAttr( "%s.preferredAngleX" % self.FKJntList[1] ) == 90:
            locC= cmds.spaceLocator( n=str(self.IKCtrlList[2]).replace( "CTL", "locC" ) )[0]
            locCGrp= cmds.group( n= "%s_GRP" % locC, em=0 )
            cmds.parent( locCGrp, locBGrp )
            cmds.setAttr( "%s.translateX" % locCGrp, 0 )
            cmds.setAttr( "%s.translateY" % locCGrp, 0 )
            cmds.setAttr( "%s.translateZ" % locCGrp, 0 )
            cmds.setAttr( "%s.rotateX" % locCGrp, 0 )
            cmds.setAttr( "%s.rotateY" % locCGrp, 0 )
            cmds.setAttr( "%s.rotateZ" % locCGrp, 0 )
            fkCtrl02= "%s_CTL" % self.FKJntList[2]
            tmpCnst= cmds.parentConstraint( fkCtrl02, locCGrp, mo=0 )
            cmds.delete( tmpCnst )
            cmds.parentConstraint( locC, self.locList[2], mo=0 )
            locCOrientX= cmds.getAttr( "%s.rx" % self.locList[2] )
            locCOrientY= cmds.getAttr( "%s.ry" % self.locList[2] )
            locCOrientZ= cmds.getAttr( "%s.rz" % self.locList[2] )
            cmds.delete( locCGrp )
        else:
            locCOrientX= cmds.getAttr( "%s.rx" % self.locList[2] )
            if locCOrientX > 120 :
                locCOrientX= locCOrientX -180
            elif locCOrientX < -120 :
                locCOrientX= locCOrientX +180
            locCOrientY= cmds.getAttr( "%s.ry" % self.locList[2] )
            locCOrientZ= cmds.getAttr( "%s.rz" % self.locList[2] )
            
        cmds.setAttr( "%s.tx" % self.IKCtrlList[2], locCPosX )
        cmds.setAttr( "%s.ty" % self.IKCtrlList[2], locCPosY )
        cmds.setAttr( "%s.tz" % self.IKCtrlList[2], locCPosZ )
        cmds.setAttr( "%s.rx" % self.IKCtrlList[2], locCOrientX )
        cmds.setAttr( "%s.ry" % self.IKCtrlList[2], locCOrientY )
        cmds.setAttr( "%s.rz" % self.IKCtrlList[2], locCOrientZ )

        cmds.delete( self.locGrpList[0], self.locGrpList[1], self.locGrpList[2], locBGrp )

if __name__ == "__main__" :
    a= Form()
    a.show()
