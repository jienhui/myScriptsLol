import maya.cmds as cmds
import cCtrlHrc_Cl as CC
import cNailCtrlHrc_Cl as CN
import ArmAutoRig_Cl as AA
import cSpineSetup_Cl as CS
import HeadSetup_Cl as HS
import LegAutoRig_Cl as LA

# AutoRig Class
class AutoRig_Cl():
    def __init__( self, root, pelvis, chest ):
        
        self.root= root
        self.pelvis= pelvis
        self.chest= chest

    # Main Auto Rig Function        
        self.cAutoRig_Fn()
    
    def cAutoRig_Fn( self ):
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
        cmds.parentConstraint( self.pelvisSpace, self.pelvis, mo=1 )
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
        cmds.parentConstraint( self.chestSpace, self.chest, mo=1 )
        
        # Create Groups & Clean Up
        self.rigGrp= cmds.group( n= 'rig_grp', em=1 )
        self.ikGrp= cmds.group( n='ikHandle_grp', em=1 )
        self.extraGrp= cmds.group( n= 'extra_grp', em=0 )
        cmds.parent( self.worldSpace, self.rigGrp )
        
        # Implement Spine Setup
        spine= CS.SpineSetup_Cl( "spine01_jnt", "spine" )
        cmds.parent( self.chestSpace, spine.fkCtrlList[-1] )
        cmds.parent( spine.fkSpaceList[0], self.rootCtrl )
        cmds.parent( spine.drvJntGrp, spine.spineCrv, self.extraGrp )
        cmds.parent( spine.spineIK[0], self.ikGrp )
        
        # Implement Head Setup
        head= HS.HeadSetup_Cl( 'neck01_jnt', 'head01_jnt', 'jaw01_jnt', 'l_eye01_jnt', 'r_eye01_jnt', 'tongue01_jnt', 'upper_teeth01_jnt', 'lower_teeth01_jnt', 'head')
        cmds.parent( head.neckCtrl[-1], self.chestCtrl )
        cmds.parent( head.headSpace, head.jawSpace, head.innerMouth, head.mainEye[-1], self.rootCtrl )
        cmds.parent( head.neckIK[0], self.ikGrp )
        worldCnst1= cmds.parentConstraint( self.moverCtrl, head.headSpace, mo=1 )
        headReverse= cmds.createNode( 'reverse', n= 'head_eye_follow_R01' )
        cmds.connectAttr( '%s.follow' % head.headCtrl, '%s.inputX' % headReverse )
        cmds.connectAttr( '%s.outputX' % headReverse, str(worldCnst1[0]) + '.%sW1' % self.moverCtrl[0] )
        worldCnst2= cmds.parentConstraint( self.moverCtrl, head.mainEye[-1], mo=1 )
        cmds.connectAttr( '%s.follow' % head.mainEye[0][0], '%s.inputY' % headReverse )
        cmds.connectAttr( '%s.outputX' % headReverse, str(worldCnst2[0]) + '.%sW1' % self.moverCtrl[0] )
        
        # Implement Arm Setup
        # Left Arm
        l_arm= AA.ArmAutoRig_Cl( 'l_shd01_jnt', 'l_clavicle01_jnt',[ 'l_thumb01_jnt', 'l_index00_jnt', 'l_middle00_jnt', 'l_ring00_jnt', 'l_pinky00_jnt'], 'arm' )
        cmds.parentConstraint( self.chestCtrl, l_arm.clavicleSpace, mo=1 )
        cmds.parentConstraint( self.chestCtrl, l_arm.IKFKSpace, mo=1 )
        cmds.parent( l_arm.IKFKSpace, l_arm.clavicleSpace, l_arm.fkCtrlSpaceList[0], l_arm.handGrp, self.rootCtrl )
        cmds.parent( l_arm.ikCtrlGrp, self.moverCtrl )
        cmds.parent( l_arm.locGrp, self.extraGrp )
        # Right Arm
        r_arm= AA.ArmAutoRig_Cl( 'r_shd01_jnt', 'r_clavicle01_jnt',[ 'r_thumb01_jnt', 'r_index00_jnt', 'r_middle00_jnt', 'r_ring00_jnt', 'r_pinky00_jnt'], 'arm' )
        cmds.parentConstraint( self.chestCtrl, r_arm.clavicleSpace, mo=1 )
        cmds.parentConstraint( self.chestCtrl, r_arm.IKFKSpace, mo=1 )
        cmds.parent( r_arm.IKFKSpace, r_arm.clavicleSpace, r_arm.fkCtrlSpaceList[0], r_arm.handGrp, self.rootCtrl )
        cmds.parent( r_arm.ikCtrlGrp, self.moverCtrl )
        cmds.parent( r_arm.locGrp, self.extraGrp )
        
        # Implement Leg Setup
        # Left Leg
        l_leg= LA.LegAutoRig_Cl( 'l_hip01_jnt',['l_heel_jnt', 'l_ball01_jnt', 'l_toe01_jnt', 'l_toeTip_jnt', 'l_sideR_jnt', 'l_sideL_jnt'], 'leg' )
        cmds.parentConstraint( self.pelvisCtrl, l_leg.aimLocGrp, mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, l_leg.distLoc1[0], mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, l_leg.IKFKSpace, mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, l_leg.aimHrc, mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, l_leg.fkCtrlSpaceList[0], mo=1 )
        cmds.parent( l_leg.IKFKSpace, l_leg.fkCtrlSpaceList[0], self.rootCtrl )
        cmds.parent( l_leg.ikCtrlGrp, self.moverCtrl )
        cmds.parent( l_leg.locGrp, self.extraGrp )
        # Right Leg
        r_leg= LA.LegAutoRig_Cl( 'r_hip01_jnt',['r_heer_jnt', 'r_ball01_jnt', 'r_toe01_jnt', 'r_toeTip_jnt', 'r_sideR_jnt', 'r_sideL_jnt'], 'leg' )
        cmds.parentConstraint( self.pelvisCtrl, r_leg.aimLocGrp, mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, r_leg.distLoc1[0], mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, r_leg.IKFKSpace, mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, r_leg.aimHrc, mo=1 )
        cmds.parentConstraint( self.pelvisCtrl, r_leg.fkCtrlSpaceList[0], mo=1 )
        cmds.parent( r_leg.IKFKSpace, r_leg.fkCtrlSpaceList[0], self.rootCtrl )
        cmds.parent( r_leg.ikCtrlGrp, self.moverCtrl )
        cmds.parent( r_leg.locGrp, self.extraGrp )
        
        # Implement Bendy Setup

        
if __name__ == '__main__' :
    autoRig= AutoRig_Cl( 'root_jnt', 'pelvis01_jnt', 'chest01_jnt' )
