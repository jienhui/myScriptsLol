import maya.cmds as cmds
import maya.cmds as cmds
import cCtrlHrc_Cl as CC
import cNailCtrlHrc_Cl as CN
import ArmAutoRig_Cl as AA
import bendySetup_Cl as B

# Proxy Bone Class
        
def AutoRigUI_Fn():
    
    win= "cAutoRig Setup"
    
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
    # InnerMouth Variables
    global cb2
    global mouthTF1
    global mouthB1
    global mouthTF2
    global mouthB2
    global mouthTF3
    global mouthB3
    # Spine Variables
    global cb3
    global spineTF1
    global spineB1
    # Arm Variables
    global cbG1
    global armTF1
    global armB1
    global armTF2
    global armB2
    # Fingers Variables
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
    if cmds.window( win, q=1, ex=True ):
        cmds.deleteUI( win )
    
    if cmds.windowPref( win, ex=True ):
        cmds.windowPref( win, remove=True )
        
    # Main Window 
    window= cmds.window( win, title="cAutoRig v1.0", iconName='Autorig', s=0 )
    # Menu Bar
    cmds.menuBarLayout()
    cmds.menu( label='Edit' )       
    cmds.menuItem( label='Reset', c='cReset()' )
    cmds.menuItem( label='Get Name', c='cGetName()' )
    cmds.menuItem( label= 'Expand All', c='cExpand()' )
    cmds.menuItem( label= 'Contract All', c='cContract()' )
    cmds.menu( label= 'Help', helpMenu=1 )
    cmds.menuItem( label ='About...', c= 'cHelpMenu()')
    cmds.separator( h=5 )
    cmds.setParent('..')
    # Body UI
    cmds.columnLayout( adjustableColumn=True )
    # Head Setup
    FL1= cmds.frameLayout( label= 'Head', borderStyle= 'etchedOut', collapsable= 1 )
    cb1= cmds.checkBox( label= 'Head Rig Setup', v=1 )
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
    cmds.rowLayout( numberOfColumns=5 )
    cmds.text( 'Eyes   : ' )
    headTF3= cmds.textField( placeholderText= 'Left eye joint name' )
    headB3= cmds.button( label= 'Add', c= 'cLEyeAddName()' )
    headTF4= cmds.textField( placeholderText= 'Right eye joint name')
    headB4= cmds.button( label= 'Add', c= 'cREyeAddName()' )
    cmds.setParent('..')
    # Inner Mouth
    FL2= cmds.frameLayout( label= 'Inner Mouth', borderStyle= 'etchedOut', collapsable= 1, collapse= 1 )
    cb2= cmds.checkBox( label= 'Inner Mouth Rig Setup', v=1 )
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
    FL3= cmds.frameLayout( label= 'Spine', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cb3= cmds.checkBox( label= 'Spine Rig Setup', v=1 )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Spine   :' )
    spineTF1= cmds.textField( placeholderText= 'First spine joint name' )
    spineB1= cmds.button( label= 'Add', c= 'cSpineAddName()' )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator()
    # Arm
    FL4= cmds.frameLayout( label= 'Arm', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cbG1= cmds.checkBoxGrp( ncb=3, la3=['Arm Rig Setup','Setup Bendy', 'Setup Both Arms'], va3= [1,1,1], cw3= [100,100,100] )
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
    # Fingers
    FL5= cmds.frameLayout( label= 'Fingers', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cbG2= cmds.checkBoxGrp( ncb=2, la2=['Finger Rig Setup','Setup Both Arms'], va2= [1,1], cw2= [150,100] )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb1= cmds.checkBox( label= 'Thumb:', v=1 )
    fingerTF1= cmds.textField( placeholderText= 'First thumb joint name' )
    fingerB1= cmds.button( label= 'Add', c= 'cThumbAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb2= cmds.checkBox( label= 'Index :', v=1  )
    fingerTF2= cmds.textField( placeholderText= 'First index joint name' )
    fingerB2= cmds.button( label= 'Add', c= 'cIndexAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb3= cmds.checkBox( label= 'Middle:', v=1  )
    fingerTF3= cmds.textField( placeholderText= 'First Middle joint name' )
    fingerB3= cmds.button( label= 'Add', c= 'cMiddleAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb4= cmds.checkBox( label= 'Ring   :', v=1  )
    fingerTF4= cmds.textField( placeholderText= 'First ring joint name' )
    fingerB4= cmds.button( label= 'Add', c= 'cRingAddName()' )
    cmds.setParent('..')
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    fingerCb5= cmds.checkBox( label= 'Pinky :', v=1  )
    fingerTF5= cmds.textField( placeholderText= 'First pinky joint name' )
    fingerB5= cmds.button( label= 'Add', c= 'cPinkyAddName()' )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator()
    # Leg
    FL6= cmds.frameLayout( label= 'Leg', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cbG3= cmds.checkBoxGrp( ncb=3, la3=['Leg Rig Setup','Setup Bendy','Setup Both Legs'], va3= [1,1,1], cw3= [100,100,100] )
    cmds.rowLayout( numberOfColumns=3, adjustableColumn= 2 )
    cmds.text( 'Hip   :' )
    legTF1= cmds.textField( placeholderText= 'Hip joint name' )
    legB1= cmds.button( label= 'Add', c= 'cLegAddName()' )
    cmds.setParent('..')
    # Reverse Foot 
    FL7= cmds.frameLayout( label= 'Feet', borderStyle= 'etchedOut', collapsable= 1, collapse=1 )
    cbG4= cmds.checkBoxGrp( ncb=2, la2=['Reverse Foot Setup','Setup Both Feets'], va2= [1,1], cw2= [150,100] )
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
    cmds.columnLayout( adjustableColumn=True )
    cmds.button( label='Setup Rig', bgc= [0.65,0.65,0.65] )
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
    cmds.setParent( '..' )
    cmds.showWindow( window )
    
    tfList= [ headTF1, headTF2, headTF3, headTF4, mouthTF1, mouthTF2, mouthTF3, spineTF1, armTF1, armTF2, fingerTF1, fingerTF2, fingerTF3, fingerTF4, fingerTF5, legTF1, footTF1, footTF2, footTF3, footTF4, footTF5, footTF6 ]
    cbList= [ cb1, cb2, cb3, fingerCb1, fingerCb2, fingerCb3, fingerCb4, fingerCb5 ]
    cbGList= [ cbG1, cbG2, cbG3, cbG4 ]
    bList= [ headB1, headB2, headB3, headB4, mouthB1, mouthB2, mouthB3, spineB1, armB1, armB2, fingerB1, fingerB2, fingerB3, fingerB4, fingerB5, legB1, footB1, footB2, footB3, footB4, footB5, footB6 ]
    FLList= [ FL1, FL2, FL3, FL4, FL5, FL6, FL7 ]
    
# Reset Funtion
def cReset():
    
    for each in tfList:
        cmds.textField( each, e=1, tx= '' )
    
    for each in cbList:
        cmds.checkBox( each, e=1, v=1 )
    
    for each in cbGList:
        cmds.checkBoxGrp( each, e=1, va2= [1,1] )
        
# Help Funtion
def cHelpMenu():
    cHelpWin= 'Auto Rig Help Window'
    
    if cmds.window( cHelpWin, q=1, ex=True ):
        cmds.deleteUI( cHelpWin )
    
    if cmds.windowPref( cHelpWin, ex=True ):
        cmds.windowPref( cHelpWin, remove=True )
        
    cHelpWin= cmds.window( title= 'Auto Rig v.1.0 Help', s=0, w= 400, h= 150 )
    cmds.frameLayout( 'Help', borderStyle= 'etchedOut', collapsable= 1, collapse=0  )
    form= cmds.formLayout()
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
def cTongueAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF1, e=1, tx= str(selJnt[0]) )

def cUpTeethAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF2, e=1, tx= str(selJnt[0]) )
    
def cDnTeethAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( mouthTF3, e=1, tx= str(selJnt[0]) )
    
# Add Spine Name Funtion
def cSpineAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( spineTF1, e=1, tx= str(selJnt[0]) )
    
# Add Arm Name Funtion
def cClavicleAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( armTF1, e=1, tx= str(selJnt[0]) )

def cArmAddName():
   
    selJnt= cmds.ls(sl=1)
    cmds.textField( armTF2, e=1, tx= str(selJnt[0]) )

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
        if 'tongue' in str(each):
            cmds.textField( mouthTF1, e=1 , tx= str(each))
        if 'teeth' in str(each):
            if 'up' in str(each):
                cmds.textField( mouthTF2, e=1, tx= str(each))
            if 'low' in str(each):
                cmds.textField( mouthTF3, e=1, tx= str(each))
        if 'spine' in str(each):
            cmds.textField( spineTF1, e=1 , tx= str(each))
        if 'l_' in str(each):
            if 'clavicle' in str(each):
                    cmds.textField( armTF1, e=1 , tx= str(each))
            if 'shoulder' in str(each):
                    cmds.textField( armTF2, e=1 , tx= str(each))
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
    

        
AutoRigUI_Fn()
