import maya.cmds as cmds
import mpSpineSetup_Cl as mpS
reload( mpS )
import sIkFkArmSetup_Cl as sA
reload( sA )
import sIkFkLegSetup_Cl as sL
reload( sL )
import cReverseFootSetup_Cl as cR
reload( cR )
import cHeadSetup_Cl as cH
reload( cH )

# Master CTL Setup
mainCTL= []
jntRad= cmds.getAttr( "spine_Jnt01.radius" )
rootCTL= cmds.circle( n= "Root_CTL", nr= [0,1,0], r= jntRad*20, ch=0 )[0]
cmds.setAttr( "%s.v" % rootCTL, e=1, l=1, k=0, cb=0 )
cmds.setAttr( "%sShape.overrideEnabled" % rootCTL, 1 )
cmds.setAttr( "%sShape.overrideColor" % rootCTL, 17 )
rootCTLGrp= cmds.group( n="%s_GRP" % rootCTL, em=0 )
superCTL= cmds.circle( n= "SuperRoot_CTL", nr= [0,1,0], r= jntRad*30, ch=0 )[0]
mainCTL.append( superCTL )
superCTLGrp= cmds.group( n="%s_GRP" % superCTL, em=0 )
masterCTL= cmds.circle( n= "Master_CTL", nr= [0,1,0], r= jntRad*40, ch=0 )[0]
mainCTL.append( masterCTL )
masterCTLGrp= cmds.group( n="%s_GRP" % masterCTL, em=0 )

for each in mainCTL:
    cmds.setAttr( "%s.sx" % each, e=1, l=1, k=0, cb=0 )
    cmds.setAttr( "%s.sy" % each, e=1, l=1, k=0, cb=0 )
    cmds.setAttr( "%s.sz" % each, e=1, l=1, k=0, cb=0 )
    cmds.setAttr( "%s.v" % each, e=1, l=1, k=0, cb=0 )
    cmds.setAttr( "%sShape.overrideEnabled" % each, 1 )
    cmds.setAttr( "%sShape.overrideColor" % each, 17 )

cmds.setAttr( "%sShape.overrideColor" % masterCTL, 13 )
cmds.parent( rootCTLGrp, superCTL )
cmds.parent( superCTLGrp, masterCTL )

# Create Proper Hierachy
jntGrp= cmds.group( n="Jnt_GRP", em=1 )
extras= cmds.group( n="ExtraNodes", em=0 )
rigGrp= cmds.group( n="Rig_GRP", em=1 )
worldLoc= cmds.spaceLocator( n="world_loc" )[0]
cmds.parentConstraint( rootCTL, worldLoc, mo=0 )
cmds.scaleConstraint( rootCTL, worldLoc, mo=0 )

# Spine Setup
s= mpS.mpSpineSetup_Cl( "pelvis_Jnt01", "spine_Jnt01", "chest_Jnt01" )

# Head Setup
h= cH.cHeadSetup_Cl( "neck_Jnt01", "head_Jnt01", "jaw_Jnt01", "L_eye_Jnt01", "R_eye_Jnt01" )

# L_arm Setup
LA= sA.sIkFkArmSetup_Cl( "L_clavicle_Jnt01", "L_shoulder_Jnt01", "L_elbow_Jnt01", "L_wrist_Jnt01" )

# R_arm Setup
RA= sA.sIkFkArmSetup_Cl( "R_clavicle_Jnt01", "R_shoulder_Jnt01", "R_elbow_Jnt01", "R_wrist_Jnt01" )

# L_leg Setup
LL= sL.sIkFkLegSetup_Cl( "L_hip_Jnt01", "L_knee_Jnt01", "L_ankle_Jnt01" )

# L_foot Setup
LF= cR.cReverseFootSetup_Cl( ["L_ball_Jnt01", "L_toe_Jnt01"], ["L_leg_front_loc", "L_leg_back_loc", "L_leg_sideL_loc", "L_leg_sideR_loc"], "L_ankle_IK02", "L_ankle_FK01" )

# R_leg Setup
RL= sL.sIkFkLegSetup_Cl( "R_hip_Jnt01", "R_knee_Jnt01", "R_ankle_Jnt01" )

# R_foot Setup
RF= cR.cReverseFootSetup_Cl( ["R_ball_Jnt01", "R_toe_Jnt01"], ["R_leg_front_loc", "R_leg_back_loc", "R_leg_sideL_loc", "R_leg_sideR_loc"], "R_ankle_IK02", "R_ankle_FK01" )

# Constraint Contoller
cmds.parentConstraint( s.chest, LA.clvCTLGRP, mo=1 )
cmds.scaleConstraint( s.ikCTLList[2], LA.clvCTLGRP, mo=1 )
cmds.parentConstraint( s.chest, RA.clvCTLGRP, mo=1 )
cmds.scaleConstraint( s.ikCTLList[2], RA.clvCTLGRP, mo=1 )
cmds.parentConstraint( s.chest, h.neckLocGrp, mo=1 )
cmds.scaleConstraint( s.ikCTLList[2], h.headCTLGrp, mo=1 )
cmds.parentConstraint( s.ikCTLList[0], LL.hipIkCTLGRP, mo=1 )
cmds.parentConstraint( s.ikCTLList[0], RL.hipIkCTLGRP, mo=1 )
cmds.parentConstraint( s.centerCTL, LL.legRootJnt, mo=1 )
cmds.scaleConstraint( s.centerCTL, LL.legRootJnt, mo=1 )
cmds.parentConstraint( s.centerCTL, RL.legRootJnt, mo=1 )
cmds.scaleConstraint( s.centerCTL, RL.legRootJnt, mo=1 )

# Neck Space Setup
cmds.parentConstraint( s.chest, h.neckCTLGrp, mo=1, sr= ["x", "y", "z"] )
neckOrient= cmds.orientConstraint( s.chest, worldLoc, h.neckCTLGrp, mo=1 )[0]
neckFollowR= cmds.createNode( "reverse", n= "neckFollow_reverse01" )
cmds.connectAttr( "%s.followBody" % h.neckCTL, "%s.inputX" % neckFollowR )
cmds.connectAttr( "%s.outputX" % neckFollowR, "%s.%sW1" % (neckOrient, worldLoc) )
cmds.connectAttr( "%s.followBody" % h.neckCTL, "%s.%sW0" % (neckOrient, s.chest) )

# eye Space Setup
eyeCnst= cmds.parentConstraint( worldLoc, h.head, h.mainEyeCTLGrp, mo=1 )[0]
eyeFollowR= cmds.createNode( "reverse", n= "eyeFollow_reverse01" )
cmds.connectAttr( "%s.followHead" % h.mainEyeCTL, "%s.inputX" % eyeFollowR )
cmds.connectAttr( "%s.outputX" % eyeFollowR, "%s.%sW0" % (eyeCnst, worldLoc) )
cmds.connectAttr( "%s.followHead" % h.mainEyeCTL, "%s.%sW1" % (eyeCnst, h.head) )

# IK Arm Space
LArmCnst= cmds.parentConstraint( worldLoc, s.centerCTL, s.ikCTLList[0], s.ikCTLList[2], LA.clvCTL, h.headCTL, LA.armIkCTLSpace, mo=1 )[0]
RArmCnst= cmds.parentConstraint( worldLoc, s.centerCTL, s.ikCTLList[0], s.ikCTLList[2], RA.clvCTL, h.headCTL, RA.armIkCTLSpace, mo=1 )[0]
armSpace= [ "World", "Center", "Pelvis", "Chest", "Shoulder","Head" ]
LarmSpace= [ worldLoc, s.centerCTL, s.ikCTLList[0], s.ikCTLList[2], LA.clvCTL, h.headCTL ]
RarmSpace= [ worldLoc, s.centerCTL, s.ikCTLList[0], s.ikCTLList[2], RA.clvCTL, h.headCTL ]
numList= [0,1,2,3,4,5]

for i,each in enumerate(armSpace):
    lCon= cmds.createNode( "condition", n="%s_%sSpace_con01" % (LA.prefix,each) )
    cmds.setAttr( "%s.secondTerm" % lCon, numList[i] )
    cmds.setAttr( "%s.operation" % lCon, 0 )
    cmds.setAttr( "%s.colorIfTrueR" % lCon, 1 )
    cmds.setAttr( "%s.colorIfFalseR" % lCon, 0 )
    cmds.connectAttr( "%s.space" % LA.armIkCTL, "%s.firstTerm" % lCon )
    cmds.connectAttr( "%s.outColorR" % lCon, "%s.%sW%d" % (LArmCnst,LarmSpace[i], numList[i] ) )
    rCon= cmds.createNode( "condition", n="%s_%sSpace_con01" % (RA.prefix,each) )
    cmds.setAttr( "%s.secondTerm" % rCon, numList[i] )
    cmds.setAttr( "%s.operation" % rCon, 0 )
    cmds.setAttr( "%s.colorIfTrueR" % rCon, 1 )
    cmds.setAttr( "%s.colorIfFalseR" % rCon, 0 )
    cmds.connectAttr( "%s.space" % RA.armIkCTL, "%s.firstTerm" % rCon )
    cmds.connectAttr( "%s.outColorR" % rCon, "%s.%sW%d" % (RArmCnst,RarmSpace[i], numList[i] ) )

cmds.setAttr( "%s.space" % LA.armIkCTL, 3 )
cmds.setAttr( "%s.space" % RA.armIkCTL, 3 )

# IK Leg Space
LLegCnst= cmds.parentConstraint( worldLoc, s.ikCTLList[0], LL.legIkCTLSpace, mo=1 )[0]
RLegCnst= cmds.parentConstraint( worldLoc, s.ikCTLList[0], RL.legIkCTLSpace, mo=1 )[0]
legSpace= [ "World", "Pelvis" ]
LarmSpace= [ worldLoc, s.ikCTLList[0] ]
RarmSpace= [ worldLoc, s.ikCTLList[0] ]

legSpaceR= cmds.createNode( "reverse", n= "legSpace_reverse01" )
cmds.connectAttr( "%s.space" % LL.legIkCTL, "%s.inputX" % legSpaceR )
cmds.connectAttr( "%s.space" % RL.legIkCTL, "%s.inputY" % legSpaceR )
cmds.connectAttr( "%s.outputX" % legSpaceR, "%s.%sW0" % (LLegCnst,worldLoc) )
cmds.connectAttr( "%s.outputY" % legSpaceR, "%s.%sW0" % (RLegCnst,worldLoc) )
cmds.connectAttr( "%s.space" % LL.legIkCTL, "%s.%sW1" % (LLegCnst,s.ikCTLList[0]) )
cmds.connectAttr( "%s.space" % RL.legIkCTL, "%s.%sW1" % (RLegCnst,s.ikCTLList[0]) )

# cleaning Hierachy
cmds.parent( h.neck, s.spineJntGrp, LA.armJntGRP, RA.armJntGRP, LL.legJntGRP, RL.legJntGRP, jntGrp )
cmds.parent( h.headExtGrp, s.spineExtra, LA.armExtra, RA.armExtra , LL.legExtra, RL.legExtra, worldLoc, extras )
cmds.parent( h.headCTLGrp, LA.armCTLGRP, RA.armCTLGRP , s.centerCTL )
cmds.parent( s.centerCTLGrp, LL.legCTLGRP, RL.legCTLGRP, rigGrp )
cmds.parent( rigGrp, rootCTL )
cmds.hide( h.neck )

# Connecting Global Scale
globalScaleMDList= [ s.globalScaleMD, LA.globalScaleMD01, RA.globalScaleMD01, LL.globalScaleMD01, RL.globalScaleMD01 ]
for each in globalScaleMDList:
    cmds.connectAttr( "%s.sx" % rootCTL, "%s.input2X" % each )
    cmds.connectAttr( "%s.sy" % rootCTL, "%s.input2Y" % each )
    cmds.connectAttr( "%s.sz" % rootCTL, "%s.input2Z" % each )
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % LF.ankleIK )
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % RF.ankleIK )
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % LF.locGRP )
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % RF.locGRP )
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % s.jntAxList[0])
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % s.jntAxList[1])
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % s.jntAxList[2])
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % s.drvJntList[0])
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % s.drvJntList[1])
cmds.connectAttr( "%s.scale" % rootCTL, "%s.scale" % s.drvJntList[2])
cmds.setAttr( "%s.segmentScaleCompensate" % LA.shdJnt, 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % RA.shdJnt, 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % LL.hipJnt, 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % RL.hipJnt, 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % LL.legJnt[3], 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % RL.legJnt[3], 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % LF.legIkJnt[0], 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % RF.legIkJnt[0], 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % LF.footJnt[0], 0 )
cmds.setAttr( "%s.segmentScaleCompensate" % RF.footJnt[0], 0 )

# Lock Controller Attributes
ctlList= [ LA.armIkCTLSpace, LA.clvCTLGRP, LA.armCTLGRP, LA.armExtCTLGRP, RA.armIkCTLSpace, RA.clvCTLGRP, RA.armCTLGRP, RA.armExtCTLGRP, LL.hipIkCTLGRP, LL.legIkCTLSpace, LL.legIKCTLGRP, LL.legExtCTLGRP, RL.hipIkCTLGRP, RL.legIkCTLSpace, RL.legIKCTLGRP, RL.legExtCTLGRP, h.mainEyeCTLGrp, h.neckCTLGrp, masterCTLGrp, superCTLGrp, rootCTLGrp, s.spineCTLGrp, h.headCTLGrp ]

for each in ctlList:
    cmds.setAttr( "%s.tx" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.ty" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.tz" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.rx" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.ry" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.rz" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.sx" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.sy" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.sz" % each, e=1, l=1, cb=1 )
    cmds.setAttr( "%s.v" % each, e=1, l=1, cb=1 )


print "Auto Rig Setup Completed."
