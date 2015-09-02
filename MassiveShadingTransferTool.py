import maya.cmds as cmds
import sys 

def cMConnectAttr():

    win='MassiveShadingTransferTool'

###### GLOBAL VARIABLES ######
    
    global tsl1
    global tsl2
    global menu1
    global radio1
    global radioA
    global radioB
    global cb1
    global cb2
    
###### GROBAL PROCEDURE ######
    
    if cmds.window( win, q=1, ex=True ):
        cmds.deleteUI( win )
        
    if cmds.windowPref( win, ex=True ):
        cmds.windowPref( win, remove=True )
        
###### CREATE WINDOW ######

    cmds.window( win, t='Massive Shader Transfer Tool v1.0', w=320, h=390)
    # menu Bar
    cmds.menuBarLayout()
    cmds.menu( label='Edit' )
    menu1=cmds.menuItem( label='reset', c='cMCAReset()' )
    cmds.menu( label= 'Help', helpMenu=1 )
    cmds.menuItem( label ='About...', c= 'cHelpMenu()')
    cmds.separator( h=5 )
    cmds.setParent('..')
    # tsl Layout for both tsk
    form1=cmds.formLayout()
    # tsl1 Layout
    column1= cmds.columnLayout( adj=True ,w=160, rs=1 )
    cmds.text( label='Source', al='center' )
    tsl1= cmds.textScrollList( numberOfRows=20, allowMultiSelection=True, w=150 )
    cmds.setParent('..')
    # tsl2 Layout
    column2= cmds.columnLayout( adj=True ,w=160, rs=1 )
    cmds.text( label='Target', al='center' )
    tsl2= cmds.textScrollList( numberOfRows=20,allowMultiSelection=True, w=150 )
    cmds.setParent('..')
    cmds.setParent('..')
    cmds.separator( h=5 )
    cmds.formLayout( form1, e=1, af=[(column1,'left',5), (column2,'right',5)], ap=[(column1,'right',2.5,50), (column2,'left',2.5,50)] )
    # radio selection Layout
    cmds.rowColumnLayout( nr=1, cat=[1,'left',10], cs= (1,40) )
    radio1= cmds.radioCollection()
    radioA= cmds.radioButton( sl=1, label='Transfer  One ---> One' )
    radioB= cmds.radioButton( label='Transfer  One ---> All' )
    cmds.setParent('..')
    cmds.separator()
    # add sel buttons Layout
    cmds.rowLayout( nc=2, cw2=[165,165], cat=( [1,'both',1], [2,'both',1] ) )
    cmds.button( label='Add Selected', c='cMCAAddSel1()' )
    cmds.button( label='Add Selected', c='cMCAAddSel2()' )
    cmds.setParent('..')
    # remove sel buttons Layout
    cmds.rowLayout( nc=2, cw2=[165,165], cat=( [1,'both',1], [2,'both',1] ) )
    cmds.button( label='Clear Source List', c='cMACRemoveSel1()' )
    cmds.button( label='Clear Target List', c='cMACRemoveSel2()' )
    cmds.setParent('..')
    # One to One Button
    cmds.separator()
    cmds.separator()
    cmds.rowLayout( nc=1, cw=[1,330], cat=[1,'both',1] )
    cmds.button( label='One to One Transfer', bgc=[0.65,0.65,0.65], c='cMACOneToOneTransfer()' )
    cmds.setParent('..')
    # connect button Layout
    cmds.separator()
    cmds.rowLayout( nc=1, cw=[1,330], cat=[1,'both',1] )
    cmds.button( label='Transfer', bgc=[0.85,0.85,0.85], c='cMACTransfer()' )
    cmds.showWindow( win )

###### HELP MENU FUNCTION ######
def cHelpMenu():
    cHelpWin= 'Auto Rig Help Window'
    
    if cmds.window( cHelpWin, q=1, ex=True ):
        cmds.deleteUI( cHelpWin )
    
    if cmds.windowPref( cHelpWin, ex=True ):
        cmds.windowPref( cHelpWin, remove=True )
        
    cHelpWin= cmds.window( title= 'Massive Shader Transfer Tool v.1.0 Help', s=0, w= 360, h= 180 )
    cmds.frameLayout( 'Help', borderStyle= 'etchedOut', collapsable= 1, collapse=0  )
    cmds.formLayout()
    content= ('This script eases the pain of transfering shaders from a list of objects either One to All, or One to One in List.'
              + '\n\n'
              + 'Polygon objects do not have to be same topology for transfer properly. '
              + '\n\n'
              + 'The concept is from the Trasfer Shading Sets from default maya tool.'
              + '\n\n'
              + '                      -- Created by Choi Jien Hui'  )
              
    cmds.scrollField( wordWrap= True, editable= False, text= content, w= 360, h= 180 )
    cmds.showWindow( cHelpWin )

###### RESET WINDOW FUNCTION ######

def cMCAReset():
    cmds.textScrollList( tsl1, e= 1, removeAll= True )
    cmds.textScrollList( tsl2, e= 1, removeAll= True )
    cmds.radioButton( radioA, e= 1, sl= 1 )    

###### ADD SELECTED OBJECTS TO OUTPUT LIST FUNCTION ######

def cMCAAddSel1():
    global selSource
    selSource= sorted(cmds.ls( sl=1 ))
    for each in sorted(selSource):
        cmds.textScrollList( tsl1, edit= True, append= each )

###### ADD SELECTED OBJECTS TO INPUT LIST FUNCTION ######

def cMCAAddSel2():
    global selTarget
    selTarget= sorted(cmds.ls( sl=1 ))
    for each in sorted(selTarget):
        cmds.textScrollList( tsl2, edit= True, append= each ) 
           

###### REMOVE SELECTED OBJECTS FROM LIST FUNCTION ######

def cMACRemoveSel1():
    cmds.textScrollList( tsl1, edit= True, removeAll= True )
    
def cMACRemoveSel2():
    cmds.textScrollList( tsl2, edit= True, removeAll= True )

###### ONE TO ONE TRANSFER FUNCTION ######  
def cMACOneToOneTransfer():
      
    selObj= cmds.ls( sl=1 )
    cmds.transferShadingSets( spa= 1, sm= 3 )
    cmds.select( cl=1 )
    sys.stdout.write("Shaders Transfer Successfully!\n" )
            
###### TRANSFER SHADER FUNCTION ######

def cMACTransfer():
    
    numSource= cmds.textScrollList( tsl1, q= True, ni= True )
    numTarget= cmds.textScrollList( tsl2, q= True, ni= True )
    cmds.select( cl=1 )
    if cmds.radioButton( radioA, q= True, sl= True ) == True:
        if numSource == numTarget :
            for each in range(len(selSource)):
                cmds.select( selSource[each] )
                cmds.select( selTarget[each], add= True )
                cmds.transferShadingSets( spa= 1, sm= 3 )
                cmds.select( cl=1 )
                sys.stdout.write("Shaders Transfer Successfully!\n" )
        else:
            cmds.warning( 'Number of objetcs in source list and target list are not match!\n' )
    else:
        if numSource == 1 :
            for each in range(len(selTarget)):
                cmds.select( selSource[0] )
                cmds.select( selTarget[each], add= True )
                cmds.transferShadingSets( spa= 1, sm= 3 )
                cmds.select( cl=1 )
                sys.stdout.write("Shaders Transfer Successfully!\n" )
        else:
            cmds.warning( 'More than one objetc in source list!\n' )
        
                  
cMConnectAttr()
