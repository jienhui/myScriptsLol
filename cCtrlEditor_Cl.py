import maya.cmds as cmds

# Global Procedure
if cmds.window( "Control Curve Editor", q=1, ex=True ):
    cmds.deleteUI( "Control Curve Editor" )
    cmds.windowPref( "Control Curve Editor", remove=True )
        
# Main Window 
win= cmds.window( "Control Curve Editor", title="Control Curve Editor v1.0", iconName='Autorig', s=0, tlb=1 )
# Menu Item
cmds.menuBarLayout()
cmds.menu( label='Edit' )       
cmds.menuItem( label='Select All Controllers', c='cGetControllers()')
cmds.separator( h=5 )
cmds.setParent('..')
# Color Picker
FL3= cmds.frameLayout( label= 'Color Picker', borderStyle= 'etchedOut', collapsable= 1 )
cmds.rowLayout( numberOfColumns=6 )
colorB1= cmds.button( l= '', bgc= [255,0,0], c= 'cRed()' )
colorB2= cmds.button( l= '', bgc= [255,255,0], c= 'cYellow()' )
colorB3= cmds.button( l= '', bgc= [0,255,0], c= 'cGreen()' )
colorB4= cmds.button( l= '', bgc= [0,255,255], c= 'cCryan()' )
colorB5= cmds.button( l= '', bgc= [0,0,255], c= 'cBlue()' )
colorB6= cmds.button( l= '', bgc= [255,0,255], c= 'cPink()' )
cmds.setParent('..')
cmds.separator( st= "in" )
cmds.setParent('..')
cmds.setParent('..')
# Scale UI
FL2= cmds.frameLayout( label= 'Scale', borderStyle= 'etchedOut', collapsable= 1 )
cmds.rowLayout( numberOfColumns=2 )
scaleB1= cmds.button( label= 'Decrease', c= 'cMinusScale()', width= 105, height= 30 )
scaleB2= cmds.button( label= 'Increase', c= 'cAddScale()', width= 105, height= 30, bgc= [0.65,0.65,0.65] )
cmds.showWindow()

# Select All Function    
def cGetControllers():

    selObj= cmds.ls( '%s' % '*_ctrl' )
    if cmds.objExists( 'worldArrow1'):
        if cmds.objExists( 'worldArrow2'):
            if cmds.objExists( 'worldArrow3'):
                if cmds.objExists( 'worldArrow4'):
                    selObj.append('worldArrow1', 'worldArrow2', 'worldArrow3', 'worldArrow4' )
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
    cmds.select( selObj )
    
# Scale Function
def cAddScale():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.scale( 1.2, 1.2, 1.2, '%s.cv[0:*]' % each, ocp= True )

def cMinusScale():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.scale( 0.8, 0.8, 0.8, '%s.cv[0:*]' % each, ocp= True )

# Color Piker Function
def cRed():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.setAttr( '%s.overrideEnabled' % each, 1 )
        cmds.setAttr( '%s.overrideColor' % each, 13 )

def cYellow():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.setAttr( '%s.overrideEnabled' % each, 1 )
        cmds.setAttr( '%s.overrideColor' % each, 17 )
        
def cGreen():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.setAttr( '%s.overrideEnabled' % each, 1 )
        cmds.setAttr( '%s.overrideColor' % each, 14 )
        
def cCryan():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.setAttr( '%s.overrideEnabled' % each, 1 )
        cmds.setAttr( '%s.overrideColor' % each, 18 )

def cBlue():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.setAttr( '%s.overrideEnabled' % each, 1 )
        cmds.setAttr( '%s.overrideColor' % each, 6 )

def cPink():
    
    selCtrl= cmds.ls( sl=1 )
    for each in selCtrl:
        cmds.setAttr( '%s.overrideEnabled' % each, 1 )
        cmds.setAttr( '%s.overrideColor' % each, 20 )
