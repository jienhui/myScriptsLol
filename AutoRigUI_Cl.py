import maya.cmds as cmds
import maya.cmds as cmds
import cCtrlHrc_Cl as CC
import cNailCtrlHrc_Cl as CN
import cBasicSetup_Cl as CB
import cArmSetup_Cl as CA
import cSpineSetup_Cl as CS
import cHeadSetup_Cl as CH
import cLegSetup_Cl as CL
reload( CL )
import bendySetup_Cl as B

# Proxy Bone Class
        
def AutoRigUI_Fn():
    
    
    # Global Variables
    # Head Variables 
    global cb1
    global headTF1
    global headB1
    global headTF2
    global headB2
    global headTF3
    global headB3
    global headTF4
    global headB4
    # Mouth Variables
    global cb2
    global mouthTF0
    global mouthB0
    global mouthTF1
    global mouthB1
    global mouthTF2
    global mouthB2
    global mouthTF3
    global mouthB3
    # Spine Variables
    global cb3
    global rootTF1
    global spineTF0
    global spineB0
    global spineTF1
    global rootB1
    global spineB1
    global spineTF2
    global spineB2
    # Arm Variables
    global cbG1
    global armTF1
    global armB1
    global armTF2
    global armB2
    # Fingers Variables
    global palmTF1
    global palmB1
    global cbG2
    global fingerCb1
    global fingerTF1
    global fingerB1
    global fingerCb2
    global fingerTF2
    global fingerB2
    global fingerCb3
    global fingerTF3
    global fingerB3
    global fingerCb4
    global fingerTF4
    global fingerB4
    global fingerCb5
    global fingerTF5
    global fingerB5
    # Leg Variables
    global cbG3
    global legTF1
    global legB1
    # Reverse Foot Variables
    global cbG4
    global footTF1
    global footB1
    global footTF2
    global footB2
    global footTF3
    global footB3
    global footTF4
    global footB4
    global footTF5
    global footB5
    global footTF6
    global footB6
    # List
    global tfList
    global cbList
    global cbGList
    global bList
    global FLList
    # Frame Layout Variables
    global FL1
    global FL2
    global FL3
    global FL4
    global FL5
    global FL6
    global FL7
    
    # Global Procedure
    if cmds.window( "cAutoRig Setup", q=1, ex=True ):
        cmds.deleteUI( "cAutoRig Setup" )
        cmds.windowPref( "cAutoRig Setup", remove=True )
        
    # Main Window 
    window= cmds.window( "cAutoRig Setup", title="cAutoRig v1.0", iconName='Autorig', s=0, h=600 )
    # Menu Bar
    cmds.menuBarLayout()
    cmds.menu( label='Edit' )       
    cmds.menuItem( label='Reset', c='cReset()' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Get Name', c='cGetName()')
    cmds.menuItem( divider=True )
    cmds.menuItem( label= 'Expand All', c='cExpand()' )
    cmds.menuItem( label= 'Contract All', c='cContract()' )
    cmds.menu( label= 'Help', helpMenu=1 )
    cmds.menuItem( label ='About...', c= 'cHelpMenu()')
    cmds.separator( h=5 )
    cmds.setParent('..')
    # Body UI
    cmds.scrollLayout( h=610, cr=1, vst=0 )
    cmds.columnLayout( adjustableColumn=True )
    # Head Setup
    FL1= cmds.frameLayout( label= 'Head', borderStyle= 'etchedOut', collapsable= 1 )
    cb1= cmds.checkBox( label= 'Head Rig Setup', v=1, onc= 'cHeadCBOn()', ofc= 'cHeadCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Neck  :' )
    headTF1= cmds.textField( placeholderText= 'Neck joint name')
    headB1= cmds.button( label= 'Add', c= 'cNeckAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Head  :' )
    headTF2= cmds.textField( placeholderText= 'Head joint name')
    headB2= cmds.button( label= 'Add', c= 'cHeadAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=5, ad2=1, ad4=1 )
    cmds.text( 'Eyes   : ' )
    headTF3= cmds.textField( placeholderText= 'Left eye joint name' )
    headB3= cmds.button( label= 'Add', c= 'cLEyeAddName()' )
    headTF4= cmds.textField( placeholderText= 'Right eye joint name')
    headB4= cmds.button( label= 'Add', c= 'cREyeAddName()' )
    cmds.setParent('..')
    # Inner Mouth
    FL2= cmds.frameLayout( label= 'Mouth', borderStyle= 'etchedOut', collapsable= 1, collapse= 1 )
    cb2= cmds.checkBox( label= 'Mouth Rig Setup', v=1, onc= 'cMouthCBOn()', ofc= 'cMouthCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Jaw     :' )
    mouthTF0= cmds.textField( placeholderText= 'First jaw joint name')
    mouthB0= cmds.button( label= 'Add', c= 'cJawAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Tongue:' )
    mouthTF1= cmds.textField( placeholderText= 'First tongue joint name')
    mouthB1= cmds.button( label= 'Add', c= 'cTongueAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=5 )
    cmds.text( 'Teeth   :' )
    mouthTF2= cmds.textField( placeholderText= 'First up teeth joint name' )
    mouthB2= cmds.button( label= 'Add', c= 'cUpTeethAddName()' )
    mouthTF3= cmds.textField( placeholderText= 'First low teeth joint name')
    mouthB3= cmds.button( label= 'Add', c= 'cDnTeethAddName()' )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator()
    # Spine
    FL3= cmds.frameLayout( label= 'Spine', borderStyle= 'etchedOut', collapsable= 1 )
    cb3= cmds.checkBox( label= 'Spine Rig Setup', v=1, onc= 'cSpineCBOn()', ofc= 'cSpineCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Root    :' )
    rootTF1= cmds.textField( placeholderText= 'First root joint name' )
    rootB1= cmds.button( label= 'Add', c= 'cRootAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Pelvis  :' )
    spineTF0= cmds.textField( placeholderText= 'First pelvis joint name' )
    spineB0= cmds.button( label= 'Add', c= 'cPelvisAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Spine   :' )
    spineTF1= cmds.textField( placeholderText= 'First spine joint name' )
    spineB1= cmds.button( label= 'Add', c= 'cSpineAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Chest  :' )
    spineTF2= cmds.textField( placeholderText= 'First chest joint name' )
    spineB2= cmds.button( label= 'Add', c= 'cChestAddName()' )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator()
    # Arm
    FL4= cmds.frameLayout( label= 'Arm', borderStyle= 'etchedOut', collapsable= 1 )
    cbG1= cmds.checkBoxGrp( ncb=3, la3=['Arm Rig Setup','Setup Bendy', 'Setup Both Arms'], va3= [1,1,1], cw3= [100,100,100], on1= 'cArmCBOn()', of1= 'cArmCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Clavicle   :' )
    armTF1= cmds.textField( placeholderText= 'Clavicle joint name' )
    armB1= cmds.button( label= 'Add', c= 'cClavicleAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Shoulder :' )
    armTF2= cmds.textField( placeholderText= 'Shoulder joint name' )
    armB2= cmds.button( label= 'Add', c= 'cArmAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Palm        :' )
    palmTF1= cmds.textField( placeholderText= 'Palm joint name' )
    palmB1= cmds.button( label= 'Add', c= 'cPalmAddName()' )
    cmds.setParent('..')
    # Fingers
    FL5= cmds.frameLayout( label= 'Fingers', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cbG2= cmds.checkBoxGrp( ncb=2, la2=['Finger Rig Setup','Setup Both Arms'], va2= [1,1], cw2= [150,100], on1= 'cFingersCBOn()', of1= 'cFingersCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb1= cmds.checkBox( label= 'Thumb:', v=1, onc= 'cThumbCBOn()', ofc= 'cThumbCBOff()' )
    fingerTF1= cmds.textField( placeholderText= 'First thumb joint name' )
    fingerB1= cmds.button( label= 'Add', c= 'cThumbAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb2= cmds.checkBox( label= 'Index :', v=1, onc= 'cIndexCBOn()', ofc= 'cIndexCBOff()'  )
    fingerTF2= cmds.textField( placeholderText= 'First index joint name' )
    fingerB2= cmds.button( label= 'Add', c= 'cIndexAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb3= cmds.checkBox( label= 'Middle:', v=1, onc= 'cMiddleCBOn()', ofc= 'cMiddleCBOff()'  )
    fingerTF3= cmds.textField( placeholderText= 'First Middle joint name' )
    fingerB3= cmds.button( label= 'Add', c= 'cMiddleAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb4= cmds.checkBox( label= 'Ring   :', v=1, onc= 'cRingCBOn()', ofc= 'cRingCBOff()'  )
    fingerTF4= cmds.textField( placeholderText= 'First ring joint name' )
    fingerB4= cmds.button( label= 'Add', c= 'cRingAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb5= cmds.checkBox( label= 'Pinky :', v=1, onc= 'cPinkyCBOn()', ofc= 'cPinkyCBOff()'  )
    fingerTF5= cmds.textField( placeholderText= 'First pinky joint name' )
    fingerB5= cmds.button( label= 'Add', c= 'cPinkyAddName()' )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator()
    # Leg
    FL6= cmds.frameLayout( label= 'Leg', borderStyle= 'etchedOut', collapsable= 1 )
    cbG3= cmds.checkBoxGrp( ncb=3, la3=['Leg Rig Setup','Setup Bendy','Setup Both Legs'], va3= [1,1,1], cw3= [100,100,100], on1= 'cLegCBOn()', of1= 'cLegCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Hip   :' )
    legTF1= cmds.textField( placeholderText= 'Hip joint name' )
    legB1= cmds.button( label= 'Add', c= 'cLegAddName()' )
    cmds.setParent('..')
    # Reverse Foot 
    FL7= cmds.frameLayout( label= 'Feet', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cbG4= cmds.checkBoxGrp( ncb=2, la2=['Reverse Foot Setup','Setup Both Feets'], va2= [1,1], cw2= [150,100], on1= 'cReverseFootCBOn()', of1= 'cReverseFootCBOff()' )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Heel   :' )
    footTF1= cmds.textField( placeholderText= 'Heel joint name' )
    footB1= cmds.button( label= 'Add', c= 'cHeelAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Ball    :' )
    footTF2= cmds.textField( placeholderText= 'Ball joint name' )
    footB2= cmds.button( label= 'Add', c= 'cBallAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Toe    :' )
    footTF3= cmds.textField( placeholderText= 'Toe joint name' )
    footB3= cmds.button( label= 'Add', c= 'cToeAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'ToeTip:' )
    footTF4= cmds.textField( placeholderText= 'ToeTip joint name' )
    footB4= cmds.button( label= 'Add', c= 'cToeTipAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'SideL  :' )
    footTF5= cmds.textField( placeholderText= 'SideL joint name' )
    footB5= cmds.button( label= 'Add', c= 'cSideLAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'SideR  :' )
    footTF6= cmds.textField( placeholderText= 'SideR joint name' )
    footB6= cmds.button( label= 'Add', c= 'cSideRAddName()' )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator()
    # Setup Button
    cmds.setParent('..')
    cmds.columnLayout( adjustableColumn=True )
    cmds.button( label='Setup Rig', bgc= [0.65,0.65,0.65], c= 'cSetup()' )
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
    cmds.setParent( '..' )
    cmds.showWindow( window )
    
    tfList= [ headTF1, headTF2, headTF3, headTF4, mouthTF0, mouthTF1, mouthTF2, mouthTF3, rootTF1, spineTF0, spineTF1, spineTF2, armTF1, armTF2, palmTF1, fingerTF1, fingerTF2, fingerTF3, fingerTF4, fingerTF5, legTF1, footTF1, footTF2, footTF3, footTF4, footTF5, footTF6 ]
    cbList= [ cb1, cb2, cb3, fingerCb1, fingerCb2, fingerCb3, fingerCb4, fingerCb5 ]
    cbGList= [ cbG1, cbG2, cbG3, cbG4 ]
    bList= [ headB1, headB2, headB3, headB4, mouthB0, mouthB1, mouthB2, mouthB3, rootB1, spineB0, spineB1, spineB2, armB1, armB2, palmB1, fingerB1, fingerB2, fingerB3, fingerB4, fingerB5, legB1, footB1, footB2, footB3, footB4, footB5, footB6 ]
    FLList= [ FL1, FL2, FL3, FL4, FL5, FL6, FL7 ]
    
# Reset Funtion
def cReset():
    
    for each in tfList:
        cmds.textField( each, e=1, tx= '' )
    
    for each in cbList:
        cmds.checkBox( each, e=1, v=1 )
    
    for each in cbGList:
        cmds.checkBoxGrp( each, e=1, va2= [1,1] )
        
    cmds.checkBoxGrp( cbG1, e=1, va3= [1,1,1] )
    cmds.checkBoxGrp( cbG3, e=1, va3= [1,1,1] )
    cmds.frameLayout( FL1, e=1, collapse= 0 )
    cmds.frameLayout( FL2, e=1, collapse= 1 )
    cmds.frameLayout( FL3, e=1, collapse= 0 )
    cmds.frameLayout( FL4, e=1, collapse= 0 )
    cmds.frameLayout( FL5, e=1, collapse= 1 )
    cmds.frameLayout( FL6, e=1, collapse= 0 )
    cmds.frameLayout( FL7, e=1, collapse= 1 )
    cHeadCBOn()
    cMouthCBOn()
    cSpineCBOn()
    cArmCBOn()
    cFingersCBOn()
    cThumbCBOn()
    cIndexCBOn()
    cMiddleCBOn()
    cRingCBOn()
    cPinkyCBOn()
    cLegCBOn()
    cReverseFootCBOn()
        
# Help Funtion
def cHelpMenu():
    cHelpWin= 'Auto Rig Help Window'
    
    if cmds.window( cHelpWin, q=1, ex=True ):
        cmds.deleteUI( cHelpWin )
    
    if cmds.windowPref( cHelpWin, ex=True ):
        cmds.windowPref( cHelpWin, remove=True )
        
    cHelpWin= cmds.window( title= 'Auto Rig v.1.0 Help', s=0, w= 400, h= 150 )
    cmds.frameLayout( 'Help', borderStyle= 'etchedOut', collapsable= 1, collapse=0  )
    cmds.formLayout()
    content= ('This is the joint based auto rig setup, a proper joint chain should be built before using this Auto Rig Setup.'
              + '\n\n'
              + 'The Auto Get Name Function will always get the 1st joint which matched the name. '
              + '\n\n'
              + 'No Fuck is given if it is not working.'
              + '\n\n'
              + 'BhwaHahahahahahhahahah!!!!!'
              + '\n\n'
              + '                        -- Created by Choi Jien Hui'  )
              
    cmds.scrollField( wordWrap= True, editable= False, text= content, w= 400, h= 200 )
    cmds.showWindow( cHelpWin )
    
# Add Head Name Funtion
def cNeckAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( headTF1, e=1, tx= str(selJnt[0]) )

def cHeadAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( headTF2, e=1, tx= str(selJnt[0]) )
    
def cLEyeAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( headTF3, e=1, tx= str(selJnt[0]) )
    
def cREyeAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( headTF4, e=1, tx= str(selJnt[0]) )

# Add Mouth Name Funtion
def cJawAddName():
    
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF0, e=1, tx= str(selJnt[0]) )
    
def cTongueAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF1, e=1, tx= str(selJnt[0]) )

def cUpTeethAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF2, e=1, tx= str(selJnt[0]) )
    
def cDnTeethAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF3, e=1, tx= str(selJnt[0]) )
    
# Add Root Name Funtion
def cRootAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( rootTF1, e=1, tx= str(selJnt[0]) ) 
    
# Add Pelvis Name Funtion
def cPelvisAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( spineTF0, e=1, tx= str(selJnt[0]) ) 

# Add Spine Name Funtion
def cSpineAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( spineTF1, e=1, tx= str(selJnt[0]) )
    
# Add Chest Name Funtion
def cChestAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( spineTF2, e=1, tx= str(selJnt[0]) )
    
# Add Arm Name Funtion
def cClavicleAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( armTF1, e=1, tx= str(selJnt[0]) )

def cArmAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( armTF2, e=1, tx= str(selJnt[0]) )

def cPalmAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( palmTF1, e=1, tx= str(selJnt[0]) )

# Add Fingers Name Funtion
def cThumbAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( fingerTF1, e=1, tx= str(selJnt[0]) )

def cIndexAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( fingerTF2, e=1, tx= str(selJnt[0]) )

def cMiddleAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( fingerTF3, e=1, tx= str(selJnt[0]) )

def cRingAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( fingerTF4, e=1, tx= str(selJnt[0]) )

def cPinkyAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( fingerTF5, e=1, tx= str(selJnt[0]) )
    
# Add Leg Name Funtion
def cLegAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( legTF1, e=1, tx= str(selJnt[0]) )
    
# Add Feet Name Funtion
def cHeelAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( footTF1, e=1, tx= str(selJnt[0]) )

def cBallAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( footTF2, e=1, tx= str(selJnt[0]) )

def cToeAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( footTF3, e=1, tx= str(selJnt[0]) )

def cToeTipAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( footTF4, e=1, tx= str(selJnt[0]) )

def cSideLAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( footTF5, e=1, tx= str(selJnt[0]) )
    
def cSideRAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( footTF6, e=1, tx= str(selJnt[0]) )
    
# Auto Get Name Function
def cGetName():
    
    cmds.select( cl=1 )
    selJnt= cmds.ls( type= 'joint', v=1 )
    for each in selJnt:
        if 'root' in str(each):
            cmds.textField( rootTF1, e=1 , tx= str(each))
    jnt01= []
    for each in selJnt:
        if '1' in str(each):
            jnt01.append(each)
    # Filling Joint Name
    for each in jnt01:
        if 'neck' in str(each):
            cmds.textField( headTF1, e=1, tx= str(each) )
        if 'head' in str(each):
            cmds.textField( headTF2, e=1, tx= str(each) )
        if 'eye' in str(each):
            if 'l' in str(each):
                cmds.textField( headTF3, e=1, tx= str(each) )
            if 'r' in str(each):
                cmds.textField( headTF4, e=1, tx= str(each) )
        if 'jaw' in str(each):
            cmds.textField( mouthTF0, e=1 , tx= str(each))
        if 'tongue' in str(each):
            cmds.textField( mouthTF1, e=1 , tx= str(each))
        if 'teeth' in str(each):
            if 'up' in str(each):
                cmds.textField( mouthTF2, e=1, tx= str(each))
            if 'low' in str(each):
                cmds.textField( mouthTF3, e=1, tx= str(each))
        if 'pelvis' in str(each):
            cmds.textField( spineTF0, e=1 , tx= str(each))
        if 'spine' in str(each):
            cmds.textField( spineTF1, e=1 , tx= str(each))
        if 'chest' in str(each):
            cmds.textField( spineTF2, e=1 , tx= str(each))
        if 'l_' in str(each):
            if 'clavicle' in str(each):
                    cmds.textField( armTF1, e=1 , tx= str(each))
            if 'shoulder' in str(each):
                    cmds.textField( armTF2, e=1 , tx= str(each))
            if 'palm' in str(each):
                    cmds.textField( palmTF1, e=1 , tx= str(each))
            if 'thumb' in str(each):
                    cmds.textField( fingerTF1, e=1 , tx= str(each))
            if 'index' in str(each):
                    cmds.textField( fingerTF2, e=1 , tx= str(each))
            if 'middle' in str(each):
                    cmds.textField( fingerTF3, e=1 , tx= str(each))
            if 'ring' in str(each):
                    cmds.textField( fingerTF4, e=1 , tx= str(each))
            if 'pinky' in str(each):
                    cmds.textField( fingerTF5, e=1 , tx= str(each))
            if 'hip' in str(each):
                    cmds.textField( legTF1, e=1 , tx= str(each))
    # Filling reverse Foot Name
    for each in selJnt:
        if 'l_' in str(each):
            if 'heels' in str(each):
                cmds.textField( footTF1, e=1, tx= str(each) )
            if 'ball' in str(each):
                cmds.textField( footTF2, e=1, tx= str(each) )
            if 'toe01' in str(each):
                cmds.textField( footTF3, e=1, tx= str(each) )
            if 'toeTip' in str(each):
                cmds.textField( footTF4, e=1, tx= str(each) )
            if 'sideL' in str(each):
                cmds.textField( footTF5, e=1, tx= str(each) )
            if 'sideR' in str(each):
                cmds.textField( footTF6, e=1, tx= str(each) )
                
# Expand All Function
def cExpand():
    
    for each in FLList:
        cmds.frameLayout( each, e=1, collapse= 0 )

# Contract All Function
def cContract():
    
    for each in FLList:
        cmds.frameLayout( each, e=1, collapse= 1 )
    
# Check Box Function
# Head On
def cHeadCBOn():

    cmds.textField( headTF1, e=1, en= True )
    cmds.textField( headTF2, e=1, en= True )
    cmds.textField( headTF3, e=1, en= True )
    cmds.textField( headTF4, e=1, en= True )
    cmds.button( headB1, e=1, en= True )
    cmds.button( headB2, e=1, en= True )
    cmds.button( headB3, e=1, en= True )
    cmds.button( headB4, e=1, en= True )
# Head Off
def cHeadCBOff():

    cmds.textField( headTF1, e=1, en= False )
    cmds.textField( headTF2, e=1, en= False )
    cmds.textField( headTF3, e=1, en= False )
    cmds.textField( headTF4, e=1, en= False )
    cmds.button( headB1, e=1, en= False )
    cmds.button( headB2, e=1, en= False )
    cmds.button( headB3, e=1, en= False )
    cmds.button( headB4, e=1, en= False )
# Mouth On
def cMouthCBOn():
    
    cmds.textField( mouthTF0, e=1, en= True )
    cmds.textField( mouthTF1, e=1, en= True )
    cmds.textField( mouthTF2, e=1, en= True )
    cmds.textField( mouthTF3, e=1, en= True )
    cmds.button( mouthB0, e=1, en= True )
    cmds.button( mouthB1, e=1, en= True )
    cmds.button( mouthB2, e=1, en= True )
    cmds.button( mouthB3, e=1, en= True )
# Mouth Off
def cMouthCBOff():
    
    cmds.textField( mouthTF0, e=1, en= False )
    cmds.textField( mouthTF1, e=1, en= False )
    cmds.textField( mouthTF2, e=1, en= False )
    cmds.textField( mouthTF3, e=1, en= False )
    cmds.button( mouthB0, e=1, en= False )
    cmds.button( mouthB1, e=1, en= False )
    cmds.button( mouthB2, e=1, en= False )
    cmds.button( mouthB3, e=1, en= False )
# Spine On
def cSpineCBOn():
    
    cmds.textField( rootTF1, e=1, en= True )
    cmds.textField( spineTF0, e=1, en= True )
    cmds.textField( spineTF1, e=1, en= True )
    cmds.textField( spineTF2, e=1, en= True )
    cmds.button( rootB1, e=1, en= True )
    cmds.button( spineB0, e=1, en= True )
    cmds.button( spineB1, e=1, en= True )
    cmds.button( spineB2, e=1, en= True )
# Spine Off
def cSpineCBOff():
    
    cmds.textField( rootTF1, e=1, en= False )
    cmds.textField( spineTF0, e=1, en= False )
    cmds.textField( spineTF1, e=1, en= False )
    cmds.textField( spineTF2, e=1, en= False )
    cmds.button( rootB1, e=1, en= False )
    cmds.button( spineB0, e=1, en= False )
    cmds.button( spineB1, e=1, en= False )
    cmds.button( spineB2, e=1, en= False )
# Arm On
def cArmCBOn():
    
    cmds.textField( armTF1, e=1, en= True )
    cmds.textField( armTF2, e=1, en= True )
    cmds.textField( palmTF1, e=1, en= True )
    cmds.button( armB1, e=1, en= True )
    cmds.button( armB2, e=1, en= True )
    cmds.button( palmB1, e=1, en= True )
    cmds.checkBoxGrp( cbG1, e=1, v2= True, v3= True )
# Arm Off
def cArmCBOff():
    
    cmds.textField( armTF1, e=1, en= False )
    cmds.textField( armTF2, e=1, en= False )
    cmds.textField( palmTF1, e=1, en= False )
    cmds.button( armB1, e=1, en= False )
    cmds.button( armB2, e=1, en= False )
    cmds.button( palmB1, e=1, en= False )
    cmds.checkBoxGrp( cbG1, e=1, v2= False, v3= False )
# Finger On
def cFingersCBOn():
    
    cmds.textField( fingerTF1, e=1, en= True )
    cmds.textField( fingerTF2, e=1, en= True )
    cmds.textField( fingerTF3, e=1, en= True )
    cmds.textField( fingerTF4, e=1, en= True )
    cmds.textField( fingerTF5, e=1, en= True )
    cmds.button( fingerB1, e=1, en= True )
    cmds.button( fingerB2, e=1, en= True )
    cmds.button( fingerB3, e=1, en= True )
    cmds.button( fingerB4, e=1, en= True )
    cmds.button( fingerB5, e=1, en= True )
    cmds.checkBox( fingerCb1, e=1, en= True )
    cmds.checkBox( fingerCb2, e=1, en= True )
    cmds.checkBox( fingerCb3, e=1, en= True )
    cmds.checkBox( fingerCb4, e=1, en= True )
    cmds.checkBox( fingerCb5, e=1, en= True )
    cmds.checkBoxGrp( cbG2, e=1, v2= True )
# Finger Off
def cFingersCBOff():
    
    cmds.textField( fingerTF1, e=1, en= False )
    cmds.textField( fingerTF2, e=1, en= False )
    cmds.textField( fingerTF3, e=1, en= False )
    cmds.textField( fingerTF4, e=1, en= False )
    cmds.textField( fingerTF5, e=1, en= False )
    cmds.button( fingerB1, e=1, en= False )
    cmds.button( fingerB2, e=1, en= False )
    cmds.button( fingerB3, e=1, en= False )
    cmds.button( fingerB4, e=1, en= False )
    cmds.button( fingerB5, e=1, en= False )
    cmds.checkBox( fingerCb1, e=1, en= False )
    cmds.checkBox( fingerCb2, e=1, en= False )
    cmds.checkBox( fingerCb3, e=1, en= False )
    cmds.checkBox( fingerCb4, e=1, en= False )
    cmds.checkBox( fingerCb5, e=1, en= False )
    cmds.checkBoxGrp( cbG2, e=1, v2= False )
# Thumb On
def cThumbCBOn():
    
    cmds.textField( fingerTF1, e=1, en= True )
    cmds.button( fingerB1, e=1, en= True )
# Thumb Off
def cThumbCBOff():
    
    cmds.textField( fingerTF1, e=1, en= False )
    cmds.button( fingerB1, e=1, en= False )
# Index On
def cIndexCBOn():
    
    cmds.textField( fingerTF2, e=1, en= True )
    cmds.button( fingerB2, e=1, en= True )
# Index Off
def cIndexCBOff():
    
    cmds.textField( fingerTF2, e=1, en= False )
    cmds.button( fingerB2, e=1, en= False )
# Middle On
def cMiddleCBOn():
    
    cmds.textField( fingerTF3, e=1, en= True )
    cmds.button( fingerB3, e=1, en= True )
# Middle Off
def cMiddleCBOff():
    
    cmds.textField( fingerTF3, e=1, en= False )
    cmds.button( fingerB3, e=1, en= False )
# Ring On
def cRingCBOn():
    
    cmds.textField( fingerTF4, e=1, en= True )
    cmds.button( fingerB4, e=1, en= True )
# Ring Off
def cRingCBOff():
    
    cmds.textField( fingerTF4, e=1, en= False )
    cmds.button( fingerB4, e=1, en= False )
# Pinky On
def cPinkyCBOn():
    
    cmds.textField( fingerTF5, e=1, en= True )
    cmds.button( fingerB5, e=1, en= True )
# Piky Off
def cPinkyCBOff():
    
    cmds.textField( fingerTF5, e=1, en= False )
    cmds.button( fingerB5, e=1, en= False )
# Leg On
def cLegCBOn():
    
    cmds.textField( legTF1, e=1, en= True )
    cmds.button( legB1, e=1, en= True )
    cmds.checkBoxGrp( cbG3, e=1, v2= True, v3= True )
# Leg Off
def cLegCBOff():
    
    cmds.textField( legTF1, e=1, en= False )
    cmds.button( legB1, e=1, en= False )
    cmds.checkBoxGrp( cbG3, e=1, v2= False, v3= False )
# Reverse Foot On
def cReverseFootCBOn():
    
    cmds.textField( footTF1, e=1, en= True )
    cmds.textField( footTF2, e=1, en= True )
    cmds.textField( footTF3, e=1, en= True )
    cmds.textField( footTF4, e=1, en= True )
    cmds.textField( footTF5, e=1, en= True )
    cmds.textField( footTF6, e=1, en= True )
    cmds.button( footB1, e=1, en= True )
    cmds.button( footB2, e=1, en= True )
    cmds.button( footB3, e=1, en= True )
    cmds.button( footB4, e=1, en= True )
    cmds.button( footB5, e=1, en= True )
    cmds.button( footB6, e=1, en= True )
    cmds.checkBoxGrp( cbG4, e=1, v2= True )
# Reverse Foot Off
def cReverseFootCBOff():
    
    cmds.textField( footTF1, e=1, en= False )
    cmds.textField( footTF2, e=1, en= False )
    cmds.textField( footTF3, e=1, en= False )
    cmds.textField( footTF4, e=1, en= False )
    cmds.textField( footTF5, e=1, en= False )
    cmds.textField( footTF6, e=1, en= False )
    cmds.button( footB1, e=1, en= False )
    cmds.button( footB2, e=1, en= False )
    cmds.button( footB3, e=1, en= False )
    cmds.button( footB4, e=1, en= False )
    cmds.button( footB5, e=1, en= False )
    cmds.button( footB6, e=1, en= False )
    cmds.checkBoxGrp( cbG4, e=1, v2= False )

# Main Setup Function
def cSetup():            
    
    # Create a custom progressBar in a windows ...
    pWin = cmds.window( title="Setting up Rig ... " )
    cmds.columnLayout()
    progressControl = cmds.progressBar(maxValue=23.5, width=300)
    cmds.progressBar(progressControl, edit=True, step=1 )
    cmds.showWindow( pWin )
    
    # Setup Head
    h= CH.HeadSetup_Cl()
    neckJnt= cmds.textField( headTF1, q=1, tx=1 )
    headJnt= cmds.textField( headTF2, q=1, tx=1 )
    lEyeJnt= cmds.textField( headTF3, q=1, tx=1 )
    rEyeJnt= cmds.textField( headTF4, q=1, tx=1 )
    if cmds.checkBox( cb1, q=1, v=1 )== True:
        if 'neck' in str(neckJnt):
            if 'head' in str(headJnt):
                if 'eye' in str(lEyeJnt):
                    if 'eye' in str(rEyeJnt):
                        h.headSetup_Fn( neckJnt, headJnt, lEyeJnt, rEyeJnt, 'head' )
                    else:
                        cmds.warning( 'Invalid Right Eye Joint!' )
                else:
                    cmds.warning( 'Invalid Left Eye Joint!' )
            else:
                cmds.warning( 'Invalid Head Joint!' )
        else:
            cmds.warning( 'Invalid Neck Joint!' )
    else:
        pass
    
    # Setup Mouth
    jawJnt= cmds.textField( mouthTF0, q=1, tx=1 )
    tongueJnt= cmds.textField( mouthTF1, q=1, tx=1 )
    upTeethJnt= cmds.textField( mouthTF2, q=1, tx=1 )
    dnTeethJnt= cmds.textField( mouthTF3, q=1, tx=1 )
    if cmds.checkBox( cb2, q=1, v=1 )== True:
        if 'jaw' in str(jawJnt):
            if 'tongue' in str(tongueJnt):
                if 'teeth' in str(upTeethJnt):
                    if 'teeth' in str(dnTeethJnt):
                        h.mouthSetup_Fn( jawJnt, tongueJnt, upTeethJnt, dnTeethJnt, 'mouth' )
                    else:
                        cmds.warning( 'Invalid Lower Teeth Joint!' )
                else:
                    cmds.warning( 'Invalid Upper Teeth Joint!' )
            else:
                cmds.warning( 'Invalid Tongue Joint!' )
        else:
            cmds.warning( 'Invalid Jaw Joint!' )
    else:
        pass
        
    # Setup Spine
    cmds.progressBar(progressControl, edit=True, step=3 )
    spineJnt= cmds.textField( spineTF1, q=1, tx=1 )
    if cmds.checkBox( cb3, q=1, v=1 )== True:
        if 'spine' in str(spineJnt):
            spine= CS.SpineSetup_Cl(spineJnt, 'spine')
        else:
            cmds.warning( 'Invalid Spine Joint!' )
    else:
        pass
    
    # Setup Arm   
    clavicleJnt= cmds.textField( armTF1, q=1, tx=1 )
    shoulderJnt= cmds.textField( armTF2, q=1, tx=1 )
     
    if cmds.checkBoxGrp( cbG1, q=1, v1=1 )== True:
        if 'clavicle' in str( clavicleJnt ):
            if 'shoulder' in str( shoulderJnt ):
                lArm= CA.cArmSetup_Cl()
                lArm.cArmSetup_Fn( shoulderJnt, clavicleJnt, 'arm' )
                if cmds.checkBoxGrp( cbG1, q=1, v2=1 )== True:
                    # Setupp Bendy
                    cmds.select( shoulderJnt, hi=1 )
                    lArmJnt= cmds.ls(sl=1)
                    # Get Joints Position
                    l_arm_jnt01Pos= cmds.xform( lArmJnt[0], q= 1, t= 1, ws= 1 )
                    l_arm_jnt02Pos= cmds.xform( lArmJnt[1], q= 1, t= 1, ws= 1 )
                    l_arm_jnt03Pos= cmds.xform( lArmJnt[2], q= 1, t= 1, ws= 1 )
                    # Get Middle Cv Position
                    l_arm_crv01X= (l_arm_jnt01Pos[0] + l_arm_jnt02Pos[0])/2
                    l_arm_crv01Y= (l_arm_jnt01Pos[1] + l_arm_jnt02Pos[1])/2
                    l_arm_crv01Z= (l_arm_jnt01Pos[2] + l_arm_jnt02Pos[2])/2
                    # Crv02
                    l_arm_crv02X= (l_arm_jnt02Pos[0] + l_arm_jnt03Pos[0])/2
                    l_arm_crv02Y= (l_arm_jnt02Pos[1] + l_arm_jnt03Pos[1])/2
                    l_arm_crv02Z= (l_arm_jnt02Pos[2] + l_arm_jnt03Pos[2])/2
                    l_arm_tmpCrv1= cmds.curve( d=2, p= [ l_arm_jnt01Pos, [l_arm_crv01X, l_arm_crv01Y, l_arm_crv01Z], l_arm_jnt02Pos ] )
                    l_arm_upperCrv= cmds.rename( str(l_arm_tmpCrv1), 'l_upperArm_crv' )
                    l_arm_upperCrvName= str(l_arm_upperCrv).split( '_crv' )
                    l_arm_tmpCrv2= cmds.curve( d=2, p= [ l_arm_jnt02Pos, [l_arm_crv02X, l_arm_crv02Y, l_arm_crv02Z], l_arm_jnt03Pos ] )
                    l_arm_lowerCrv= cmds.rename( str(l_arm_tmpCrv2), 'l_lowerArm_crv' )
                    l_arm_lowerCrvName= str(l_arm_lowerCrv).split( '_crv' )
                    # Create Bendy
                    l_upperArmBendy= B.BendySetup_Cl( l_arm_upperCrv, l_arm_upperCrvName[0] )
                    l_lowerArmBendy= B.BendySetup_Cl( l_arm_lowerCrv, l_arm_lowerCrvName[0] )
                    # Clean Up Bendy
                    cmds.parentConstraint( lArmJnt[0], l_upperArmBendy.ctrlGrp, mo=1 )
                    cmds.parentConstraint( lArmJnt[1], l_lowerArmBendy.ctrlGrp, mo=1 )
                    cmds.connectAttr( '%s.rx' % lArmJnt[0], '%s.twist' % str(l_upperArmBendy.bendyCtrl03[0][0]) )
                    cmds.connectAttr( '%s.rx' % lArmJnt[2], '%s.twist' % str(l_lowerArmBendy.bendyCtrl03[0][0]) )
                else:
                    pass
                if cmds.checkBoxGrp( cbG1, q=1, v3=1 )== True:
                    r_shoulderJnt= str(shoulderJnt).replace( 'l_', 'r_' )
                    r_clavicleJnt= str(clavicleJnt).replace( 'l_', 'r_' )                 
                    if 'r_shoulder' in r_shoulderJnt:
                        if 'r_clavicle' in r_clavicleJnt:
                            rArm= CA.cArmSetup_Cl()
                            rArm.cArmSetup_Fn( r_shoulderJnt, r_clavicleJnt, 'arm' )
                            if cmds.checkBoxGrp( cbG1, q=1, v2=1 )== True:
                                # Setupp Bendy
                                cmds.select( r_shoulderJnt, hi=1 )
                                rArmJnt= cmds.ls(sl=1)
                                # Get Joints Position
                                r_arm_jnt01Pos= cmds.xform( rArmJnt[0], q= 1, t= 1, ws= 1 )
                                r_arm_jnt02Pos= cmds.xform( rArmJnt[1], q= 1, t= 1, ws= 1 )
                                r_arm_jnt03Pos= cmds.xform( rArmJnt[2], q= 1, t= 1, ws= 1 )
                                # Get Middle Cv Position
                                r_arm_crv01X= (r_arm_jnt01Pos[0] + r_arm_jnt02Pos[0])/2
                                r_arm_crv01Y= (r_arm_jnt01Pos[1] + r_arm_jnt02Pos[1])/2
                                r_arm_crv01Z= (r_arm_jnt01Pos[2] + r_arm_jnt02Pos[2])/2
                                # Crv02
                                r_arm_crv02X= (r_arm_jnt02Pos[0] + r_arm_jnt03Pos[0])/2
                                r_arm_crv02Y= (r_arm_jnt02Pos[1] + r_arm_jnt03Pos[1])/2
                                r_arm_crv02Z= (r_arm_jnt02Pos[2] + r_arm_jnt03Pos[2])/2
                                r_arm_tmpCrv1= cmds.curve( d=2, p= [ r_arm_jnt01Pos, [r_arm_crv01X, r_arm_crv01Y, r_arm_crv01Z], r_arm_jnt02Pos ] )
                                r_arm_upperCrv= cmds.rename( str(r_arm_tmpCrv1), 'r_upperArm_crv' )
                                r_arm_upperCrvName= str(r_arm_upperCrv).split( '_crv' )
                                r_arm_tmpCrv2= cmds.curve( d=2, p= [ r_arm_jnt02Pos, [r_arm_crv02X, r_arm_crv02Y, r_arm_crv02Z], r_arm_jnt03Pos ] )
                                r_arm_lowerCrv= cmds.rename( str(r_arm_tmpCrv2), 'r_lowerArm_crv' )
                                r_arm_lowerCrvName= str(r_arm_lowerCrv).split( '_crv' )
                                # Create Bendy
                                r_upperArmBendy= B.BendySetup_Cl( r_arm_upperCrv, r_arm_upperCrvName[0] )
                                r_lowerArmBendy= B.BendySetup_Cl( r_arm_lowerCrv, r_arm_lowerCrvName[0] )
                                # Clean Up Bendy
                                cmds.parentConstraint( rArmJnt[0], r_upperArmBendy.ctrlGrp, mo=1 )
                                cmds.parentConstraint( rArmJnt[1], r_lowerArmBendy.ctrlGrp, mo=1 )
                                cmds.connectAttr( '%s.rx' % rArmJnt[0], '%s.twist' % str(r_upperArmBendy.bendyCtrl03[0][0]) )
                                cmds.connectAttr( '%s.rx' % rArmJnt[2], '%s.twist' % str(r_lowerArmBendy.bendyCtrl03[0][0]) )
                            else:
                                pass
                        else:
                            cmds.warning( 'Invalid Right Clavicle Joint!' )
                    else:
                        cmds.warning( 'Invalid Right Shoulder Joint!' )
                else:
                    pass
            else:
                cmds.warning( 'Invalid Shoulder Joint!' )
        else:
            cmds.warning( 'Invalid Clavicle Joint!' )
    else:
        pass
    
    # Setup Finger
    palmJnt= cmds.textField( palmTF1, q=1, tx=1 )
    r_palmJnt= str(palmJnt).replace( 'l_', 'r_' )
    thumbJnt= cmds.textField( fingerTF1, q=1, tx=1 )
    r_thumbJnt= str(thumbJnt).replace( 'l_', 'r_' )
    indexJnt= cmds.textField( fingerTF2, q=1, tx=1 )
    r_indexJnt= str(indexJnt).replace( 'l_', 'r_' )
    middleJnt= cmds.textField( fingerTF3, q=1, tx=1 )
    r_middleJnt= str(middleJnt).replace( 'l_', 'r_' )
    ringJnt= cmds.textField( fingerTF4, q=1, tx=1 )
    r_ringJnt= str(ringJnt).replace( 'l_', 'r_' )
    pinkyJnt= cmds.textField( fingerTF5, q=1, tx=1 )
    r_pinkyJnt= str(pinkyJnt).replace( 'l_', 'r_' )
    
    if cmds.checkBoxGrp( cbG2, q=1, v1=1 )== True:
        a= CA.cArmSetup_Cl()
        lFingerGrp= cmds.group( n='l_fingerCtrlGrp', em=1 )
        tmpCnst= cmds.parentConstraint( palmJnt, lFingerGrp )
        cmds.delete( tmpCnst )
        cmds.parentConstraint( palmJnt, lFingerGrp )
        if cmds.checkBox( fingerCb1, q=1, v=1 )== True:
            if 'thumb' in thumbJnt:
                lThumb= a.cThumbSetup_Fn( thumbJnt )
                cmds.parent( lThumb[1][0], lFingerGrp )
            else:
                cmds.warning( 'Invalid Thumb Joint!' )
        else:
            pass
        if cmds.checkBox( fingerCb2, q=1, v=1 )== True:
            if 'index' in indexJnt:
                lIndex= a.cFingerSetup_Fn( indexJnt )
                cmds.parent( lIndex[1][0], lFingerGrp )
            else:
                cmds.warning( 'Invalid Index Joint!' )
        else:
            pass
        if cmds.checkBox( fingerCb3, q=1, v=1 )== True:
            if 'middle' in middleJnt:
                lMiddle= a.cFingerSetup_Fn( middleJnt )
                cmds.parent( lMiddle[1][0], lFingerGrp )
            else:
                cmds.warning( 'Invalid Middle Joint!' )
        else:
            pass
        if cmds.checkBox( fingerCb4, q=1, v=1 )== True:
            if 'ring' in ringJnt:
                lRing= a.cFingerSetup_Fn( ringJnt )
                cmds.parent( lRing[1][0], lFingerGrp )
            else:
                cmds.warning( 'Invalid Ring Joint!' )
        else:
            pass
        if cmds.checkBox( fingerCb5, q=1, v=1 )== True:
            if 'pinky' in pinkyJnt:
                lPinky= a.cFingerSetup_Fn( pinkyJnt )
                cmds.parent( lPinky[1][0], lFingerGrp )
            else:
                cmds.warning( 'Invalid Pinky Joint!' )
        else:
            pass
        if cmds.checkBoxGrp( cbG2, q=1, v2=1 )== True:
            rFingerGrp= cmds.group( n='r_fingerCtrlGrp', em=1 )
            tmpCnst= cmds.parentConstraint( r_palmJnt, rFingerGrp )
            cmds.delete( tmpCnst )
            cmds.parentConstraint( r_palmJnt, rFingerGrp )
            if cmds.checkBox( fingerCb1, q=1, v=1 )== True:
                if 'r_thumb' in r_thumbJnt:
                    rThumb= a.cThumbSetup_Fn( thumbJnt.replace( 'l_', 'r_' ) )
                    cmds.parent( rThumb[1][0], rFingerGrp )
                else:
                    cmds.warning( 'Invalid Right Thumb Joint!' )
            else:
                pass
            if cmds.checkBox( fingerCb2, q=1, v=1 )== True:
                if 'r_index' in r_indexJnt:
                    rIndex= a.cFingerSetup_Fn( indexJnt.replace( 'l_', 'r_' ) )
                    cmds.parent( rIndex[1][0], rFingerGrp )
                else:
                    cmds.warning( 'Invalid Right Index Joint!' )
            else:
                pass
            if cmds.checkBox( fingerCb3, q=1, v=1 )== True:
                if 'r_middle' in r_middleJnt:
                    rMiddle= a.cFingerSetup_Fn( middleJnt.replace( 'l_', 'r_' ) )
                    cmds.parent( rMiddle[1][0], rFingerGrp )
                else:
                    cmds.warning( 'Invalid Right Middle Joint!' )
            else:
                pass
            if cmds.checkBox( fingerCb4, q=1, v=1 )== True:
                if 'r_ring' in r_ringJnt:
                    rRing= a.cFingerSetup_Fn( ringJnt.replace( 'l_', 'r_' ) )
                    cmds.parent( rRing[1][0], rFingerGrp )
                else:
                    cmds.warning( 'Invalid Right Ring Joint!' )
            else:
                pass
            if cmds.checkBox( fingerCb5, q=1, v=1 )== True:
                if 'r_pinky' in r_pinkyJnt:
                    rPinky= a.cFingerSetup_Fn( pinkyJnt.replace( 'l_', 'r_' ) )
                    cmds.parent( rPinky[1][0], rFingerGrp )
                else:
                        cmds.warning( 'Invalid Right Pinky Joint!' )
    else:
        pass
        
    # Setup Leg
    lLeg= CL.cLegSetup_Cl()
    hipJnt= cmds.textField( legTF1, q=1, tx=1 )
    r_hipJnt= str(hipJnt).replace( 'l_', 'r_' )
    
    if cmds.checkBoxGrp( cbG3, q=1, v1=1 )== True:
        if 'hip' in str( hipJnt ):
            lLeg.cLegSetup_Fn( hipJnt, 'leg' )
            if cmds.checkBoxGrp( cbG3, q=1, v2=1 )== True:
                # Setupp Bendy
                cmds.select( hipJnt, hi=1 )
                lLegJnt= cmds.ls(sl=1)
                # Get Joints Position
                l_leg_jnt01Pos= cmds.xform( lLegJnt[0], q= 1, t= 1, ws= 1 )
                l_leg_jnt02Pos= cmds.xform( lLegJnt[1], q= 1, t= 1, ws= 1 )
                l_leg_jnt03Pos= cmds.xform( lLegJnt[2], q= 1, t= 1, ws= 1 )
                # Get Middle Cv Position
                l_leg_crv01X= (l_leg_jnt01Pos[0] + l_leg_jnt02Pos[0])/2
                l_leg_crv01Y= (l_leg_jnt01Pos[1] + l_leg_jnt02Pos[1])/2
                l_leg_crv01Z= (l_leg_jnt01Pos[2] + l_leg_jnt02Pos[2])/2
                # Crv02
                l_leg_crv02X= (l_leg_jnt02Pos[0] + l_leg_jnt03Pos[0])/2
                l_leg_crv02Y= (l_leg_jnt02Pos[1] + l_leg_jnt03Pos[1])/2
                l_leg_crv02Z= (l_leg_jnt02Pos[2] + l_leg_jnt03Pos[2])/2
                l_leg_tmpCrv1= cmds.curve( d=2, p= [ l_leg_jnt01Pos, [l_leg_crv01X, l_leg_crv01Y, l_leg_crv01Z], l_leg_jnt02Pos ] )
                l_leg_upperCrv= cmds.rename( str(l_leg_tmpCrv1), 'l_upperLeg_crv' )
                l_leg_upperCrvName= str(l_leg_upperCrv).split( '_crv' )
                l_leg_tmpCrv2= cmds.curve( d=2, p= [ l_leg_jnt02Pos, [l_leg_crv02X, l_leg_crv02Y, l_leg_crv02Z], l_leg_jnt03Pos ] )
                l_leg_lowerCrv= cmds.rename( str(l_leg_tmpCrv2), 'l_lowerLeg_crv' )
                l_leg_lowerCrvName= str(l_leg_lowerCrv).split( '_crv' )
                # Create Bendy
                l_upperLegBendy= B.BendySetup_Cl( l_leg_upperCrv, l_leg_upperCrvName[0] )
                l_lowerLegBendy= B.BendySetup_Cl( l_leg_lowerCrv, l_leg_lowerCrvName[0] )
                # Clean Up Bendy
                cmds.parentConstraint( lLegJnt[0], l_upperLegBendy.ctrlGrp, mo=1 )
                cmds.parentConstraint( lLegJnt[1], l_lowerLegBendy.ctrlGrp, mo=1 )
                cmds.connectAttr( '%s.rx' % lLegJnt[0], '%s.twist' % str(l_upperLegBendy.bendyCtrl03[0][0]) )
                cmds.connectAttr( '%s.rx' % lLegJnt[2], '%s.twist' % str(l_lowerLegBendy.bendyCtrl03[0][0]) )
            else:
                pass
            if cmds.checkBoxGrp( cbG3, q=1, v3=1 )== True:               
                if 'r_hip' in r_hipJnt:
                    rLeg= CL.cLegSetup_Cl()
                    rLeg.cLegSetup_Fn( r_hipJnt, 'leg' )
                    if cmds.checkBoxGrp( cbG3, q=1, v2=1 )== True:
                        # Setupp Bendy
                        cmds.select( r_hipJnt, hi=1 )
                        rLegJnt= cmds.ls(sl=1)
                        # Get Joints Position
                        r_leg_jnt01Pos= cmds.xform( rLegJnt[0], q= 1, t= 1, ws= 1 )
                        r_leg_jnt02Pos= cmds.xform( rLegJnt[1], q= 1, t= 1, ws= 1 )
                        r_leg_jnt03Pos= cmds.xform( rLegJnt[2], q= 1, t= 1, ws= 1 )
                        # Get Middle Cv Position
                        r_leg_crv01X= (r_leg_jnt01Pos[0] + r_leg_jnt02Pos[0])/2
                        r_leg_crv01Y= (r_leg_jnt01Pos[1] + r_leg_jnt02Pos[1])/2
                        r_leg_crv01Z= (r_leg_jnt01Pos[2] + r_leg_jnt02Pos[2])/2
                        # Crv02
                        r_leg_crv02X= (r_leg_jnt02Pos[0] + r_leg_jnt03Pos[0])/2
                        r_leg_crv02Y= (r_leg_jnt02Pos[1] + r_leg_jnt03Pos[1])/2
                        r_leg_crv02Z= (r_leg_jnt02Pos[2] + r_leg_jnt03Pos[2])/2
                        r_leg_tmpCrv1= cmds.curve( d=2, p= [ r_leg_jnt01Pos, [r_leg_crv01X, r_leg_crv01Y, r_leg_crv01Z], r_leg_jnt02Pos ] )
                        r_leg_upperCrv= cmds.rename( str(r_leg_tmpCrv1), 'r_upperLeg_crv' )
                        r_leg_upperCrvName= str(r_leg_upperCrv).split( '_crv' )
                        r_leg_tmpCrv2= cmds.curve( d=2, p= [ r_leg_jnt02Pos, [r_leg_crv02X, r_leg_crv02Y, r_leg_crv02Z], r_leg_jnt03Pos ] )
                        r_leg_lowerCrv= cmds.rename( str(r_leg_tmpCrv2), 'r_lowerLeg_crv' )
                        r_leg_lowerCrvName= str(r_leg_lowerCrv).split( '_crv' )
                        # Create Bendy
                        r_upperLegBendy= B.BendySetup_Cl( r_leg_upperCrv, r_leg_upperCrvName[0] )
                        r_lowerLegBendy= B.BendySetup_Cl( r_leg_lowerCrv, r_leg_lowerCrvName[0] )
                        # Clean Up Bendy
                        cmds.parentConstraint( rLegJnt[0], r_upperLegBendy.ctrlGrp, mo=1 )
                        cmds.parentConstraint( rLegJnt[1], r_lowerLegBendy.ctrlGrp, mo=1 )
                        cmds.connectAttr( '%s.rx' % rLegJnt[0], '%s.twist' % str(r_upperLegBendy.bendyCtrl03[0][0]) )
                        cmds.connectAttr( '%s.rx' % rLegJnt[2], '%s.twist' % str(r_lowerLegBendy.bendyCtrl03[0][0]) )
                    else:
                        pass
                else:
                    cmds.warning( 'Invalid Right Hip Joint!' )
            else:
                pass
        else:
            cmds.warning( 'Invalid Hip Joint!' )
    else:
        pass
    
    # Setup Reverse Foot
    heelJnt= cmds.textField( footTF1, q=1, tx=1 )
    ballJnt= cmds.textField( footTF2, q=1, tx=1 )
    toeJnt= cmds.textField( footTF3, q=1, tx=1 )
    toeTipJnt= cmds.textField( footTF4, q=1, tx=1 )
    sideLJnt= cmds.textField( footTF5, q=1, tx=1 )
    sideRJnt= cmds.textField( footTF6, q=1, tx=1 )
    r_heelJnt= str(heelJnt).replace( 'l_', 'r_' )
    r_ballJnt= str(ballJnt).replace( 'l_', 'r_' )
    r_toeJnt= str(toeJnt).replace( 'l_', 'r_' )
    r_toeTipJnt= str(toeTipJnt).replace( 'l_', 'r_' )
    r_sideLJnt= str(sideLJnt).replace( 'l_', 'r_' )
    r_sideRJnt= str(sideRJnt).replace( 'l_', 'r_' )
    
    if cmds.checkBoxGrp( cbG4, q=1, v1=1 )== True:
        if 'heel' in heelJnt:
            if 'ball' in ballJnt:
                if 'toe' in toeJnt:
                    if 'toeTip' in toeTipJnt:
                        if 'sideL' in sideLJnt:
                            if 'sideR' in sideRJnt:
                                lFeet= CL.cLegSetup_Cl()
                                lFeet.cFootSetup_Fn( lLeg.ikCtrl, lLeg.ikH[0], lLeg.ikJntSel, heelJnt, ballJnt, toeJnt, toeTipJnt, sideRJnt, sideLJnt, 'l' )
                                cmds.parent( lFeet.feetLocGrp, lLeg.locGrp )
                                if cmds.checkBoxGrp( cbG4, q=1, v2=1 )== True:
                                    rFeet= CL.cLegSetup_Cl()
                                    rFeet.cFootSetup_Fn( rLeg.ikCtrl, rLeg.ikH[0], rLeg.ikJntSel, r_heelJnt, r_ballJnt, r_toeJnt, r_toeTipJnt, r_sideRJnt, r_sideLJnt, 'r' )
                                    cmds.parent( rFeet.feetLocGrp, rLeg.locGrp )
                            else:
                                cmds.warning( 'Invalid sideR Joint!' )
                        else:
                            cmds.warning( 'Invalid sideL Joint!' )
                    else:
                        cmds.warning( 'Invalid toeTip Joint!' )
                else:
                    cmds.warning( 'Invalid Toe Joint!' )
            else:
                cmds.warning( 'Invalid Ball Joint!' )
        else:
            cmds.warning( 'Invalid Heel Joint!' )
    else:
        pass
    
    # Finalize Rig
    cmds.progressBar(progressControl, edit=True, step=3 )
    basic= CB.BasicSetup_Cl()
    pelvisJnt= cmds.textField( spineTF0, q=1, tx=1 )
    chestJnt= cmds.textField( spineTF2, q=1, tx=1 )
    rootJnt= cmds.textField( rootTF1, q=1, tx=1 )
            
    if cmds.checkBox( cb1, q=1, v=1 )== True:
        if cmds.checkBox( cb3, q=1, v=1 )== True:
            if cmds.checkBoxGrp( cbG1, q=1, v1=1 )== True:
                if cmds.checkBoxGrp( cbG3, q=1, v1=1 )== True:
                    if 'chest' in str( chestJnt ):
                        if 'pelvis' in str( pelvisJnt ):
                            if 'root' in str( rootJnt ):
                                basic.cBasicSetup_Fn( rootJnt, pelvisJnt, chestJnt, 'BasicSetup' )
                                # Clean Up Spine Setup
                                if cmds.checkBox( cb3, q=1, v=1 )== True:
                                    cmds.parent( basic.chestSpace, spine.fkCtrlList[-1] )
                                    cmds.parent( spine.fkSpaceList[0], basic.rootCtrl )
                                    cmds.parent( spine.drvJntGrp, spine.spineCrv, basic.extraGrp )
                                    cmds.parent( spine.spineIK[0], basic.ikGrp )
                                else:
                                    pass
                                # Clean Up Head Setup
                                if cmds.checkBox( cb1, q=1, v=1 )== True:
                                    cmds.parent( h.neckCtrl[-1], basic.chestCtrl )
                                    cmds.parent( h.headSpace, h.mainEye[-1], basic.rootCtrl )
                                    worldCnst1= cmds.parentConstraint( basic.moverCtrl, h.headSpace, mo=1 )
                                    headReverse= cmds.createNode( 'reverse', n= 'head_eye_follow_R01' )
                                    cmds.connectAttr( '%s.follow' % h.headCtrl, '%s.inputX' % headReverse )
                                    cmds.connectAttr( '%s.outputX' % headReverse, str(worldCnst1[0]) + '.%sW1' % basic.moverCtrl[0] )
                                    worldCnst2= cmds.parentConstraint( basic.moverCtrl, h.mainEye[-1], mo=1 )
                                    cmds.connectAttr( '%s.follow' % h.mainEye[0][0], '%s.inputY' % headReverse )
                                    cmds.connectAttr( '%s.outputX' % headReverse, str(worldCnst2[0]) + '.%sW1' % basic.moverCtrl[0] )
                                    # Clean Up Mouth Setup
                                    if cmds.checkBox( cb2, q=1, v=1 )== True:
                                        cmds.parent( h.jawSpace, h.innerMouth, basic.rootCtrl )
                                    else:
                                        pass
                                else:
                                    pass
                                # Clean Up Arm Setup
                                if cmds.checkBoxGrp( cbG1, q=1, v1=1 )== True:
                                    # Left Arm
                                    cmds.parentConstraint( basic.chestCtrl, lArm.clavicleSpace, mo=1 )
                                    cmds.parentConstraint( basic.chestCtrl, lArm.IKFKSpace, mo=1 )
                                    cmds.parent( lArm.IKFKSpace, lArm.clavicleSpace, lArm.fkCtrlSpaceList[0], lFingerGrp, basic.rootCtrl )
                                    cmds.parent( lArm.ikCtrlGrp, basic.moverCtrl )
                                    cmds.parent( lArm.locGrp, basic.extraGrp )
                                    # Right Arm
                                    if cmds.checkBoxGrp( cbG1, q=1, v3=1 )== True:
                                        cmds.parentConstraint( basic.chestCtrl, rArm.clavicleSpace, mo=1 )
                                        cmds.parentConstraint( basic.chestCtrl, rArm.IKFKSpace, mo=1 )
                                        cmds.parent( rArm.IKFKSpace, rArm.clavicleSpace, rArm.fkCtrlSpaceList[0], rFingerGrp, basic.rootCtrl )
                                        cmds.parent( rArm.ikCtrlGrp, basic.moverCtrl )
                                        cmds.parent( rArm.locGrp, basic.extraGrp )
                                    else:
                                        pass
                                else:
                                    pass
                                # Clean Up Leg Setup
                                if cmds.checkBoxGrp( cbG3, q=1, v1=1 )== True:
                                    # Left Leg
                                    cmds.parentConstraint( basic.pelvisCtrl, lLeg.aimLocGrp, mo=1 )
                                    cmds.parentConstraint( basic.pelvisCtrl, lLeg.distLoc1[0], mo=1 )
                                    cmds.parentConstraint( basic.pelvisCtrl, lLeg.IKFKSpace, mo=1 )
                                    cmds.parentConstraint( basic.pelvisCtrl, lLeg.aimHrc, mo=1 )
                                    cmds.parentConstraint( basic.pelvisCtrl, lLeg.fkCtrlSpaceList[0], mo=1 )
                                    cmds.parent( lLeg.IKFKSpace, lLeg.fkCtrlSpaceList[0], basic.rootCtrl )
                                    cmds.parent( lLeg.ikCtrlGrp, basic.moverCtrl )
                                    cmds.parent( lLeg.locGrp, basic.extraGrp )
                                    # Right Leg
                                    if cmds.checkBoxGrp( cbG3, q=1, v3=1 )== True:
                                        cmds.parentConstraint( basic.pelvisCtrl, rLeg.aimLocGrp, mo=1 )
                                        cmds.parentConstraint( basic.pelvisCtrl, rLeg.distLoc1[0], mo=1 )
                                        cmds.parentConstraint( basic.pelvisCtrl, rLeg.IKFKSpace, mo=1 )
                                        cmds.parentConstraint( basic.pelvisCtrl, rLeg.aimHrc, mo=1 )
                                        cmds.parentConstraint( basic.pelvisCtrl, rLeg.fkCtrlSpaceList[0], mo=1 )
                                        cmds.parent( rLeg.IKFKSpace, rLeg.fkCtrlSpaceList[0], basic.rootCtrl )
                                        cmds.parent( rLeg.ikCtrlGrp, basic.moverCtrl )
                                        cmds.parent( rLeg.locGrp, basic.extraGrp )
                                    else:
                                        pass
                                # Clean Up Arm Bendy
                                if cmds.checkBoxGrp( cbG1, q=1, v2=1 )== True:
                                    # Left UpperArm
                                    lUpArm02Ctrl= cmds.duplicate( l_upperArmBendy.bendyCtrl02[0], n= str(l_upperArmBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                    lUpArm02Sdk= cmds.group( n= '%s_sdk' % lUpArm02Ctrl[0], em=1 )
                                    cmds.group( n= '%s_align' % lUpArm02Ctrl[0], em=0 )
                                    lUpArm02Space= cmds.group( n= '%s_space' % lUpArm02Ctrl[0], em=0 )
                                    tmpCnst= cmds.parentConstraint( l_upperArmBendy.bendyCtrl02[0], lUpArm02Space, mo=0 )
                                    cmds.delete( tmpCnst, lUpArm02Ctrl[1] )
                                    cmds.parentConstraint( lArmJnt[0], lUpArm02Space, mo=1 )
                                    cmds.parent( lUpArm02Ctrl[0], lUpArm02Sdk  )
                                    cmds.connectAttr( '%s.t' % lUpArm02Ctrl[0], '%s.t' % l_upperArmBendy.bendyCtrl02[0][0] )
                                    # Left LowerArm
                                    lDnArm02Ctrl= cmds.duplicate( l_lowerArmBendy.bendyCtrl02[0], n= str(l_lowerArmBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                    lDnArm02Sdk= cmds.group( n= '%s_sdk' % lDnArm02Ctrl[0], em=1 )
                                    cmds.group( n= '%s_align' % lDnArm02Ctrl[0], em=0 )
                                    lDnArm02Space= cmds.group( n= '%s_space' % lDnArm02Ctrl[0], em=0 )
                                    tmpCnst= cmds.parentConstraint( l_lowerArmBendy.bendyCtrl02[0], lDnArm02Space, mo=0 )
                                    cmds.delete( tmpCnst, lDnArm02Ctrl[1] )
                                    cmds.parentConstraint( lArmJnt[1], lDnArm02Space, mo=1 )
                                    cmds.parent( lDnArm02Ctrl[0], lDnArm02Sdk  )
                                    cmds.connectAttr( '%s.t' % lDnArm02Ctrl[0], '%s.t' % l_lowerArmBendy.bendyCtrl02[0][0] )
                                    # Clean Up Left Arm Bendy
                                    armSecondaryCtrlGrp= cmds.group( n= 'armScondary_ctrlGrp', em=1 )
                                    cmds.parent( armSecondaryCtrlGrp, basic.rootCtrl ) 
                                    cmds.parent( lUpArm02Space, lDnArm02Space, armSecondaryCtrlGrp )
                                    bendyGrp= cmds.group( n='bendy_extraGrp', em=1 )
                                    cmds.parent( l_upperArmBendy.mainGrp, l_lowerArmBendy.mainGrp, bendyGrp  )
                                    cmds.parent( bendyGrp, basic.extraGrp )
                                    if cmds.checkBoxGrp( cbG1, q=1, v3=1 )== True:
                                        # Right UpperArm
                                        rUpArm02Ctrl= cmds.duplicate( r_upperArmBendy.bendyCtrl02[0], n= str(r_upperArmBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                        rUpArm02Sdk= cmds.group( n= '%s_sdk' % rUpArm02Ctrl[0], em=1 )
                                        cmds.group( n= '%s_align' % rUpArm02Ctrl[0], em=0 )
                                        rUpArm02Space= cmds.group( n= '%s_space' % rUpArm02Ctrl[0], em=0 )
                                        tmpCnst= cmds.parentConstraint( r_upperArmBendy.bendyCtrl02[0], rUpArm02Space, mo=0 )
                                        cmds.delete( tmpCnst, rUpArm02Ctrl[1] )
                                        cmds.parentConstraint( rArmJnt[0], rUpArm02Space, mo=1 )
                                        cmds.parent( rUpArm02Ctrl[0], rUpArm02Sdk  )
                                        cmds.connectAttr( '%s.t' % rUpArm02Ctrl[0], '%s.t' % r_upperArmBendy.bendyCtrl02[0][0] )
                                        # Right LowerArm
                                        rDnArm02Ctrl= cmds.duplicate( r_lowerArmBendy.bendyCtrl02[0], n= str(r_lowerArmBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                        rDnArm02Sdk= cmds.group( n= '%s_sdk' % rDnArm02Ctrl[0], em=1 )
                                        cmds.group( n= '%s_align' % rDnArm02Ctrl[0], em=0 )
                                        rDnArm02Space= cmds.group( n= '%s_space' % rDnArm02Ctrl[0], em=0 )
                                        tmpCnst= cmds.parentConstraint( r_lowerArmBendy.bendyCtrl02[0], rDnArm02Space, mo=0 )
                                        cmds.delete( tmpCnst, rDnArm02Ctrl[1] )
                                        cmds.parentConstraint( rArmJnt[1], rDnArm02Space, mo=1 )
                                        cmds.parent( rDnArm02Ctrl[0], rDnArm02Sdk  )
                                        cmds.connectAttr( '%s.t' % rDnArm02Ctrl[0], '%s.t' % r_lowerArmBendy.bendyCtrl02[0][0] )
                                        # Clean Up Right Arm Bendy 
                                        cmds.parent( rUpArm02Space, rDnArm02Space, armSecondaryCtrlGrp )
                                        cmds.parent( r_upperArmBendy.mainGrp, r_lowerArmBendy.mainGrp, bendyGrp  )
                                    else:
                                        pass
                                # Clean Up Leg Bendy
                                if cmds.checkBoxGrp( cbG3, q=1, v2=1 )== True:
                                    # Left UpperLeg
                                    lUpLeg02Ctrl= cmds.duplicate( l_upperLegBendy.bendyCtrl02[0], n= str(l_upperLegBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1  )
                                    lUpLeg02Sdk= cmds.group( n= '%s_sdk' % lUpLeg02Ctrl[0], em=1 )
                                    cmds.group( n= '%s_align' % lUpLeg02Ctrl[0], em=0 )
                                    lUpLeg02Space= cmds.group( n= '%s_space' % lUpLeg02Ctrl[0], em=0 )
                                    tmpCnst= cmds.parentConstraint( l_upperLegBendy.bendyCtrl02[0], lUpLeg02Space, mo=0 )
                                    cmds.delete( tmpCnst, lUpLeg02Ctrl[1] )
                                    cmds.parentConstraint( lLegJnt[0], lUpLeg02Space, mo=1 )
                                    cmds.parent( lUpLeg02Ctrl[0], lUpLeg02Sdk  )
                                    cmds.connectAttr( '%s.t' % lUpLeg02Ctrl[0], '%s.t' % l_upperLegBendy.bendyCtrl02[0][0] )
                                    # Left LowerLeg
                                    lDnLeg02Ctrl= cmds.duplicate( l_lowerLegBendy.bendyCtrl02[0], n= str(l_lowerLegBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                    lDnLeg02Sdk= cmds.group( n= '%s_sdk' % lDnLeg02Ctrl[0], em=1 )
                                    cmds.group( n= '%s_align' % lDnLeg02Ctrl[0], em=0 )
                                    lDnLeg02Space= cmds.group( n= '%s_space' % lDnLeg02Ctrl[0], em=0 )
                                    tmpCnst= cmds.parentConstraint( l_lowerLegBendy.bendyCtrl02[0], lDnLeg02Space, mo=0 )
                                    cmds.delete( tmpCnst, lDnLeg02Ctrl[1] )
                                    cmds.parentConstraint( lLegJnt[1], lDnLeg02Space, mo=1 )
                                    cmds.parent( lDnLeg02Ctrl[0], lDnLeg02Sdk  )
                                    cmds.connectAttr( '%s.t' % lDnLeg02Ctrl[0], '%s.t' % l_lowerLegBendy.bendyCtrl02[0][0] )
                                    # Clean Up Left Leg Bendy
                                    legSecondaryCtrlGrp= cmds.group( n= 'legSecondary_ctrlGrp', em=1 )
                                    cmds.parent( legSecondaryCtrlGrp, basic.rootCtrl ) 
                                    cmds.parent( lUpLeg02Space, lDnLeg02Space, legSecondaryCtrlGrp )
                                    cmds.parent( l_upperLegBendy.mainGrp, l_lowerLegBendy.mainGrp, bendyGrp  )
                                    if cmds.checkBoxGrp( cbG3, q=1, v3=1 )== True:
                                        # Right UpperLeg
                                        rUpLeg02Ctrl= cmds.duplicate( r_upperLegBendy.bendyCtrl02[0], n= str(r_upperLegBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                        rUpLeg02Sdk= cmds.group( n= '%s_sdk' % rUpLeg02Ctrl[0], em=1 )
                                        cmds.group( n= '%s_align' % rUpLeg02Ctrl[0], em=0 )
                                        rUpLeg02Space= cmds.group( n= '%s_space' % rUpLeg02Ctrl[0], em=0 )
                                        tmpCnst= cmds.parentConstraint( r_upperLegBendy.bendyCtrl02[0], rUpLeg02Space, mo=0 )
                                        cmds.delete( tmpCnst, rUpLeg02Ctrl[1] )
                                        cmds.parentConstraint( rLegJnt[0], rUpLeg02Space, mo=1 )
                                        cmds.parent( rUpLeg02Ctrl[0], rUpLeg02Sdk  )
                                        cmds.connectAttr( '%s.t' % rUpLeg02Ctrl[0], '%s.t' % r_upperLegBendy.bendyCtrl02[0][0] )
                                        # Right LowerLeg
                                        rDnLeg02Ctrl= cmds.duplicate( r_lowerLegBendy.bendyCtrl02[0], n= str(r_lowerLegBendy.bendyCtrl02[0][0]).replace( 'bendy02', 'secondary' ), rc=1 )
                                        rDnLeg02Sdk= cmds.group( n= '%s_sdk' % rDnLeg02Ctrl[0], em=1 )
                                        cmds.group( n= '%s_align' % rDnLeg02Ctrl[0], em=0 )
                                        rDnLeg02Space= cmds.group( n= '%s_space' % rDnLeg02Ctrl[0], em=0 )
                                        tmpCnst= cmds.parentConstraint( r_lowerLegBendy.bendyCtrl02[0], rDnLeg02Space, mo=0 )
                                        cmds.delete( tmpCnst, rDnLeg02Ctrl[1] )
                                        cmds.parentConstraint( rLegJnt[1], rDnLeg02Space, mo=1 )
                                        cmds.parent( rDnLeg02Ctrl[0], rDnLeg02Sdk  )
                                        cmds.connectAttr( '%s.t' % rDnLeg02Ctrl[0], '%s.t' % r_lowerLegBendy.bendyCtrl02[0][0] )
                                        # Clean Up Right Leg Bendy 
                                        cmds.parent( rUpLeg02Space, rDnLeg02Space, legSecondaryCtrlGrp )
                                        cmds.parent( r_upperLegBendy.mainGrp, r_lowerLegBendy.mainGrp, bendyGrp  )
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                cmds.warning( 'Invalid Root Joint!' )
                        else:
                            cmds.warning( 'Invalid Pelvis Joint!' )
                    else:
                            cmds.warning( 'Invalid Chest Joint!' )
                else:
                    pass

    cmds.select( cl=1 )
    cmds.progressBar(progressControl, edit=True, step=4 )
    cmds.progressBar(progressControl, edit=True, step=5 )
    cmds.progressBar(progressControl, edit=True, step=6 )
    cmds.progressBar(progressControl, edit=True, step=8 )
    cmds.progressBar(progressControl, edit=True, step=9 )
    cmds.progressBar(progressControl, edit=True, step=10 )
    cmds.deleteUI( pWin )
        
AutoRigUI_Fn()
