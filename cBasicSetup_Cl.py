import maya.cmds as cmds

# AutoRig Class
class BasicSetup_Cl():
    def __init__( object ):
        
        pass

    # Main Auto Rig Function    
    def BasicSetup_Fn( self, root, pelvis, chest, name ):
        
        self.root= root
        self.pelvis= pelvis
        self.chest= chest
        self.name= name
        
        # Create World Controller
        self.worldCtrl= cmds.circle( n= 'world_ctrl', nr= (0,1,0), ch=0, d=3, r=1)
        cmds.group( n= '%s_sdk' % self.worldCtrl[0], em=0 )
        cmds.group( n= '%s_align' % self.worldCtrl[0], em=0 )
        self.worldSpace= cmds.group( n= '%s_space' % self.worldCtrl[0], em=0 )
        
        # Create Mover Controller
        self.moverCtrl= cmds.circle( n= 'mover_ctrl', nr= (0,1,0), ch=0, d=3, r=0.8 )
        cmds.group( n= '%s_sdk' % self.moverCtrl[0], em=0 )
        cmds.group( n= '%s_align' % self.moverCtrl[0], em=0 )
        cmds.group( n= '%s_space' % self.moverCtrl[0], em=0 )
        cmds.parent( '%s_space' % self.moverCtrl[0], self.worldCtrl )
        
        # create Arrow Helper Controller
        arrowa01= cmds.curve( d=1, p=( [0,0,-0.33],[-0.66,0,0],[-0.44,0,0],[-0.44,0,0.11],[0.44,0,0.11],[0.44,0,0],[0.66,0,0],[0,0,-0.33]) )
        wa01= cmds.rename( str(arrowa01), 'worldArrow1' )
        cmds.xform( wa01, t= [0,0,-1.2] )
        cmds.move( 0, '%s.scalePivot' % wa01, '%s.rotatePivot' % wa01, z=1 )
        cmds.makeIdentity( wa01, a=1, t=1, r=1, s=1 )
        wa02= cmds.duplicate( wa01 )
        cmds.xform( wa02, ro= [0,90,0] )
        wa03= cmds.duplicate( wa01 )
        cmds.xform( wa03, ro= [0,180,0] )
        wa04= cmds.duplicate( wa01 )
        cmds.xform( wa04, ro= [0,-90,0] )
        arrows= [ wa01, wa02[0], wa03[0], wa04[0] ]
        for each in arrows:
            cmds.setAttr( '%s.template' % str(each), 1 )
            cmds.parent( each, self.worldCtrl )
        
        # Create Root Controller
        self.rootCtrl= cmds.curve( n='root_ctrl', d=1, p=([0,0,-1],[-0.433,0,-0.797],[-0.217,0,-0.797],[-0.592,0,-0.592],[-0.797,0,-0.217],[-0.797,0,-0.433],[-1,0,0],[-0.797,0,0.433],[-0.797,0,0.217],[-0.592,0,0.592],[-0.217,0,0.797],[-0.433,0,0.797],[0,0,1],[0.433,0,0.797],[0.217,0,0.797],[0.592,0,0.592],[0.797,0,0.217],[0.797,0,0.433],[1,0,0],[0.797,0,-0.433],[0.797,0,-0.217],[0.592,0,-0.592],[0.217,0,-0.797],[0.433,0,-0.747],[0,0,-1]) )
        cmds.xform( '%s.cv[*]' % self.rootCtrl, s= [2,2,2] )
        cmds.group( n= '%s_sdk' % self.rootCtrl, em=0 )
        cmds.group( n= '%s_align' % self.rootCtrl, em=0 )
        cmds.group( n= '%s_space' % self.rootCtrl, em=0 )
        tmpCnst= cmds.parentConstraint( self.root, '%s_space' % self.rootCtrl, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parentConstraint( self.rootCtrl, self.root )
        cmds.parent( '%s_space' % self.rootCtrl, self.moverCtrl )
        
        # Create Pelivs Controller
        self.pelvisCtrl= cmds.curve( n= str(self.pelvis).replace( '_jnt', '_ctrl' ), d=1, 
        p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)] )
        cmds.setAttr( '%s.sx' % self.pelvisCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.pelvisCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.pelvisCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.pelvisCtrl, l=1, k=0, cb=0 ) 
        cmds.group( n= '%s_sdk' % self.pelvisCtrl, em=0 )
        cmds.group( n= '%s_align' % self.pelvisCtrl, em=0 )
        self.pelvisSpace= cmds.group( n= '%s_space' % self.pelvisCtrl, em=0 )
        tmpCnst= cmds.parentConstraint( self.pelvis, self.pelvisSpace, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parentConstraint( self.pelvisCtrl, self.pelvis, mo=1 )
        cmds.parent( self.pelvisSpace, self.rootCtrl )
        
        # Create Chest Controller
        self.chestCtrl= cmds.curve( n= str(self.chest).replace( '_jnt', '_ctrl' ), d=1, 
        p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)] )
        cmds.setAttr( '%s.sx' % self.chestCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.chestCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.chestCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.chestCtrl, l=1, k=0, cb=0 ) 
        cmds.group( n= '%s_sdk' % self.chestCtrl, em=0 )
        cmds.group( n= '%s_align' % self.chestCtrl, em=0 )
        self.chestSpace= cmds.group( n= '%s_space' % self.chestCtrl, em=0 )
        tmpCnst= cmds.parentConstraint( self.chest, self.chestSpace, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parentConstraint( self.chestCtrl, self.chest, mo=1 )
        
        # Create Groups & Clean Up
        self.rigGrp= cmds.group( n= 'rig_grp', em=1 )
        self.ikGrp= cmds.group( n='ikHandle_grp', em=1 )
        self.extraGrp= cmds.group( n= 'extra_grp', em=0 )
        cmds.parent( self.worldSpace, self.rigGrp )
        
        return [ self.rigGrp, self.ikGrp, self.extraGrp, self.chestSpace, self.chestCtrl, self.pelvisSpace, self.pelvisCtrl, self.rootCtrl, self.moverCtrl, self.worldCtrl ]
        
if __name__ == '__main__' :
    autoRig= BasicSetup_Cl()
    c= autoRig.BasicSetup_Fn('root_jnt', 'pelvis01_jnt', 'chest01_jnt', 'AutoRig' )
    print c
