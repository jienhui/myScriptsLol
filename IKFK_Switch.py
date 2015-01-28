######## IK/FK SWITCH ########

import maya.cmds as cmds

######## SELECT JOINT ########    
cmds.select( cmds.ls( sl=1), hi=1 )
selJnt= cmds.ls (sl=1)
numJnt= len(selJnt)

if selJnt[0].startswith( 'l_' ):
    rl= 'l_'
else:
    rl= 'r_'
    
###### GET PREFIX ######
dialog= cmds.promptDialog( title='IKFK Auto Setup', message='arm or leg ?', button=['OK', 'Cancel'], defaultButton= 'OK', cancelButton='Cancel', dismissString='Cancel')
prefix= cmds.promptDialog( query= True, text= True ) + '_'
print prefix
jntGrp= cmds.group( n= '%s%sjnt_hrc' % ( rl, prefix ), em=1 )
partsGrp= cmds.group( n= '%s%sparts_hrc' % ( rl, prefix ), em=0 )
ctrlGrp= cmds.group( n= '%s%sctrl_hrc' % ( rl, prefix ), em=1 )
mainGrp= cmds.group( n= '%s%sIKFK_hrc' % ( rl, prefix ), em=0 )
cmds.parent( partsGrp, mainGrp )
cmds.select( selJnt[0] )

######## DUPLICATE JOINT ########
######## IK jnt ########
dupIK= cmds.duplicate( selJnt[0], rc=1 )
while numJnt > 3 :
    cmds.delete(dupIK[-1])
    dupIK.remove(dupIK[-1])
    numJnt = numJnt - 1

for each in dupIK:
    jntNameIK= each.replace( 'jnt1', 'IK_drv' )
    newIK= cmds.rename( each, jntNameIK )
    cmds.select( newIK, add=1 )

ikJntSel= cmds.ls( sl=1 )

######## FK jnt ########
dupFK= cmds.duplicate( ikJntSel[0], rc=1 )

for each in dupFK:
    jntNameFK= each.replace( 'IK_drv1', 'FK_drv' )
    newFK= cmds.rename( each, jntNameFK )
    cmds.select( newFK, add=1 )

fkJntSel= cmds.ls( sl=1 )
cmds.parent( ikJntSel[0], jntGrp, a=1 )
cmds.parent( fkJntSel[0], jntGrp, a=1 )

######## IK/FK SWITCH CONTROLLER ########
###### create ikFk controller ######
text= cmds.textCurves( ch=0, f='Times New Roman', t= 'IkFk' )

for each in range(1,5):
    cmds.rename( 'curve%s' % each, 'ikFk_crv%s' % each )
    
cmds.select( text, hi=1 )
crvHrc= cmds.ls( '*crv*', s=0 )
crvShape= crvHrc[4:8]
crv= crvHrc[0:4]

for each in crvShape[1:4]:    
    cmds.parent( each, crv[0], r=1, s=1 )
    
cmds.move( 1.4,0,0, crvShape[1] + '.cv[*]', r=1, os=1, ws=1 )
cmds.move( 3.7,0,0, crvShape[2] + '.cv[*]', r=1, os=1, ws=1 )
cmds.move( 6.1,0,0, crvShape[3] + '.cv[*]', r=1, os=1, ws=1 )
cmds.select( crv[0], r=1 )
cmds.xform( crv[0], s=[0.1,0.1,0.1], cp=1 )
cmds.makeIdentity( crv[0], a=1, t=1, r=1, s=1, n=0 )
cmds.rename( str(crv[0]), rl + prefix + 'ikFk_ctrl' )
cmds.group( n= rl + prefix + 'ikFk_ctrl_sdk', em=0 )
alignGrp= cmds.group( n= rl + prefix + 'ikFk_ctrl_align', em=0 )
spaceGrp= cmds.group( n= rl + prefix + 'ikFk_ctrl_space', em=0 )
cmds.parent( spaceGrp, w=1 )
tmpCst= cmds.pointConstraint( selJnt[1], spaceGrp, mo=0 )
cmds.delete( tmpCst )
cmds.delete( text )
ikFKPos= cmds.getAttr( '%s.tz' % spaceGrp )
cmds.move( ikFKPos + (-1), alignGrp, z=True )
cmds.pointConstraint( selJnt[1], spaceGrp, mo=1 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.tx', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.ty', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.tz', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.rx', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.ry', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.rz', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.sx', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.sy', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.sz', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.v', l=1, k=0, cb=0 )
cmds.addAttr( rl + prefix + 'ikFk_ctrl', ln= 'ikFkSwitch', at= 'float', hnv=1, min=0, hxv=1, max=1, r=1, k=1, h=0 )
cmds.setAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', k=True, l=False )
cmds.parent( spaceGrp, ctrlGrp )

######## BLEND JOINT ########
######## pairBlend 01 ########
blnNode1= cmds.pairBlend( nd= selJnt[0], at=['tx','ty','tz','rx','ry','rz'] )
cmds.connectAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', blnNode1 + '.weight' )
cmds.connectAttr( fkJntSel[0] + '.translate', blnNode1 + '.inTranslate1' )
cmds.connectAttr( fkJntSel[0] + '.rotate', blnNode1 + '.inRotate1' )
cmds.connectAttr( ikJntSel[0] + '.translate', blnNode1 + '.inTranslate2' )
cmds.connectAttr( ikJntSel[0] + '.rotate', blnNode1 + '.inRotate2' )
pb01= cmds.rename( blnNode1, str(selJnt[0]) + '_PB01' )

######## pairBlend 02 ########
blnNode2= cmds.pairBlend( nd= selJnt[1], at=['tx','ty','tz','rx','ry','rz'] )
cmds.connectAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', blnNode2 + '.weight' )
cmds.connectAttr( fkJntSel[1] + '.translate', blnNode2 + '.inTranslate1' )
cmds.connectAttr( fkJntSel[1] + '.rotate', blnNode2 + '.inRotate1' )
cmds.connectAttr( ikJntSel[1] + '.translate', blnNode2 + '.inTranslate2' )
cmds.connectAttr( ikJntSel[1] + '.rotate', blnNode2 + '.inRotate2' )
pb02= cmds.rename( blnNode2, str(selJnt[1]) + '_PB01' )

######## pairBlend 03 ########
blnNode3= cmds.pairBlend( nd= selJnt[2], at=['tx','ty','tz','rx','ry','rz'] )
cmds.connectAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', blnNode3 + '.weight' )
cmds.connectAttr( fkJntSel[2] + '.translate', blnNode3 + '.inTranslate1' )
cmds.connectAttr( fkJntSel[2] + '.rotate', blnNode3 + '.inRotate1' )
cmds.connectAttr( ikJntSel[2] + '.translate', blnNode3 + '.inTranslate2' )
cmds.connectAttr( ikJntSel[2] + '.rotate', blnNode3 + '.inRotate2' )
pb03= cmds.rename( blnNode3, str(selJnt[2]) + '_PB01' )

######## SETUP FK ########
######## create controller ########
for each in fkJntSel:
    fkCtrl= cmds.circle( n= str(each).replace( 'drv', 'ctrl' ), ch=0 )
    cmds.xform( fkCtrl, ro= [0,90,0] )
    cmds.makeIdentity( fkCtrl, a=1, t=1, r=1, s=1, n=0 )
    cmds.setAttr( str(each).replace( 'drv', 'ctrl' ) + '.sx', l=1, k=0, cb=0 )
    cmds.setAttr( str(each).replace( 'drv', 'ctrl' ) + '.sy', l=1, k=0, cb=0 )
    cmds.setAttr( str(each).replace( 'drv', 'ctrl' ) + '.sz', l=1, k=0, cb=0 )
    cmds.setAttr( str(each).replace( 'drv', 'ctrl' ) + '.v', l=1, k=0, cb=0 )
    cmds.group( n= str(each).replace( 'drv', 'ctrl' ) + '_sdk', em=0 )
    cmds.group( n= str(each).replace( 'drv', 'ctrl' ) + '_align', em=0 )
    fkSpace= cmds.group( n= str(each).replace( 'drv', 'ctrl' ) + '_space', em=0 )
    tmpCnt= cmds.parentConstraint( each, fkSpace, mo=0 )
    cmds.delete( tmpCnt )
    cmds.parentConstraint( fkCtrl, each, mo=0 )
    cmds.scaleConstraint( fkCtrl, each, mo=0 )
cmds.parent( str(fkJntSel[2]).replace( 'drv', 'ctrl' ) + '_space', str(fkJntSel[1]).replace( 'drv', 'ctrl' ) )
cmds.parent( str(fkJntSel[1]).replace( 'drv', 'ctrl' ) + '_space', str(fkJntSel[0]).replace( 'drv', 'ctrl' ) )
cmds.parent( str(fkJntSel[0]).replace( 'drv', 'ctrl' ) + '_space', ctrlGrp )
R01= cmds.createNode( 'reverse', n='fk_ctrl_vis_R01' )
cmds.connectAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', R01 + '.inputX' )
cmds.connectAttr( R01 + '.outputX', str(fkJntSel[0]).replace( 'drv', 'ctrl' ) + '_space.v' )

######## SETUP IK ########
extraAttrs = ['autoStretch', 'upperStretch', 'lowerStretch', 'kneeSlide']
ikH= cmds.ikHandle( n= rl + prefix + 'ikHandle', sj=ikJntSel[0], ee=ikJntSel[2], sol= 'ikRPsolver', p=1, w=1 )
ikCtrl= cmds.curve( n= rl + prefix + 'IK_ctrl', d=1, 
p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)] )
cmds.setAttr( rl + prefix + 'IK_ctrl.sx', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'IK_ctrl.sy', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'IK_ctrl.sz', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'IK_ctrl.v', l=1, k=0, cb=0 )
cmds.addAttr( rl + prefix + 'IK_ctrl', ln='EXTRA', at='enum', en='-' )
cmds.setAttr( rl + prefix + 'IK_ctrl.EXTRA',e=1, l=False, k=True, cb=True )
cmds.addAttr( rl + prefix + 'IK_ctrl', ln='autoStretch', at= 'enum', en= 'Off:On'  )
cmds.setAttr( rl + prefix + 'IK_ctrl.autoStretch', e=1, l=False, k=True )
cmds.addAttr( rl + prefix + 'IK_ctrl', ln='upperStretch', at='float' )
cmds.setAttr( rl + prefix + 'IK_ctrl.upperStretch', e=1, l=False, k=True )
cmds.addAttr( rl + prefix + 'IK_ctrl', ln='lowerStretch', at='float' )
cmds.setAttr( rl + prefix + 'IK_ctrl.lowerStretch', e=1, l=False, k=True )
cmds.addAttr( rl + prefix + 'IK_ctrl', ln='kneeSlide', at='float' )
cmds.setAttr( rl + prefix + 'IK_ctrl.kneeSlide', e=1, l=False, k=True )
cmds.group( n= rl + prefix + 'IK_ctrl' + '_sdk', em=0 )
cmds.group( n= rl + prefix + 'IK_ctrl' + '_align', em=0 )
ikSpace= cmds.group( n= rl + prefix + 'IK_ctrl' + '_space', em=0 )
tmpCnst= cmds.pointConstraint( ikH[0], ikSpace, mo=0 )
cmds.delete ( tmpCnst )
cmds.parent( ikH[0], ikCtrl )
cmds.hide( ikH[0] )
cmds.connectAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', rl + prefix + 'IK_ctrl' + '_space.v' )
cmds.parent( ikSpace, ctrlGrp )

######## Setup PV hrc ########
pvCtrl= cmds.curve( n= rl + prefix + 'PV_ctrl', d=1, 
p=[(0,0,1),(0,0.5,0.87),(0,0.87,0.5),(0,1,0),(0,0.87,-0.5),(0,0.5,-0.87),(0,0,-1),(0,-0.5,-0.87),(0,-0.87,-0.5),(0,-1,0),(0,-0.87,0.5),(0,-0.5,0.87),(0,0,1),(0.71,0,0.71),(1,0,0),(0.71,0,-0.71),(0,0,-1),(-0.71,0,-0.71),(-1,0,0),(-0.87,0.5,0),(-0.5,0.87,0),(0,1,0),(0.5,0.87,0),(0.87,0.5,0),(1,0,0),(0.87,-0.5,0),(0.5,-0.87,0),(0,-1,0),(-0.5,-0.87,0),(-0.87,-0.5,0),(-1,0,0),(-0.71,0,0.71),(0,0,1)] )
cmds.xform( pvCtrl, s=[0.3,0.3,0.3] )
cmds.makeIdentity( pvCtrl, a=1, t=1, r=1, s=1, n=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.rx', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.ry', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.rz', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.sx', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.sy', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.sz', l=1, k=0, cb=0 )
cmds.setAttr( rl + prefix + 'PV_ctrl.v', l=1, k=0, cb=0 )
cmds.addAttr( rl + prefix + 'PV_ctrl', ln='SPACE', at='enum', en='-' )
cmds.setAttr( rl + prefix + 'PV_ctrl.SPACE',e=1, l=False, k=True, cb=True )
cmds.addAttr( rl + prefix + 'PV_ctrl', ln='follow', at='enum', en='World:Auto:Lock:Ctrl' )
cmds.setAttr( rl+ prefix + 'PV_ctrl.follow', e=1, l=False, k=True )
cmds.setAttr( rl+ prefix + 'PV_ctrl.follow', 1 )
cmds.group( n= rl + prefix + 'PV_ctrl_sdk', em=0 )
cmds.group( n= rl + prefix + 'PV_ctrl_align', em=0 )
pvSpace= cmds.group( n= rl + prefix + 'PV_ctrl_space', em=0 )
snapPos= cmds.pointConstraint( selJnt[1], pvSpace, mo=0 )
cmds.delete( snapPos )
cmds.connectAttr( rl + prefix + 'ikFk_ctrl.ikFkSwitch', rl + prefix + 'PV_ctrl' + '_space.v' )
cmds.poleVectorConstraint( pvCtrl, ikH[0] )

######## Setup Rotate Aim Hrc ########
aimUp= cmds.group( n= rl + prefix + 'rotateAim_up', em=1 )
aimGrp= cmds.group( n= rl + prefix + 'rotateAim_up_grp', em=0 )
aimHrc= cmds.group( n= rl + prefix + 'rotateAim_hrc', em=0 )
tmpCn= cmds.parentConstraint( ikJntSel[0], aimHrc, mo=0 )
cmds.delete( tmpCn )
aimLoc= cmds.spaceLocator( n= '%s%saimLoc' % ( rl, prefix ) )
tmpCn= cmds.parentConstraint( ikJntSel[0], aimLoc[0], mo=0 )
cmds.delete( tmpCn )
locPos= cmds.getAttr( '%s.ty' % aimLoc[0] )
cmds.move( locPos +1, aimLoc, y=True )
tmpAim= cmds.aimConstraint( ikCtrl, aimHrc, mo=1, aim=[1,0,0], u=[0,1,0], wut= "objectrotation", wuo= str(aimLoc[0]) )
cmds.delete( tmpAim )
aimFollow= cmds.aimConstraint( ikCtrl, aimGrp, mo=1, aim=[1,0,0], u=[0,1,0], wut= "objectrotation", wuo= str(aimLoc[0]) )
cmds.parent( pvSpace, aimUp )
ctrlFollow= cmds.parentConstraint( ikCtrl, pvSpace,  mo=1 )
cmds.parent( aimHrc, ctrlGrp )

######## create condition node ########
aimLockCon= cmds.createNode( 'condition', n= rl + prefix + 'aimLock_con01' )
cmds.connectAttr( rl+ prefix + 'PV_ctrl.follow', str(aimLockCon) + '.firstTerm' )
cmds.setAttr( str(aimLockCon) + '.operation', 1 )
cmds.setAttr( str(aimLockCon) + '.secondTerm', 1 )
cmds.setAttr( str(aimLockCon) + '.colorIfTrueR', 0 )
cmds.setAttr( str(aimLockCon) + '.colorIfFalseR', 1 )
cmds.connectAttr( str(aimLockCon) + '.outColorR', str(aimFollow[0]) + '.' + rl + prefix + 'IK_ctrlW0' )
kneeLockCon= cmds.createNode( 'condition', n= rl + prefix + 'kneeLock_con01' )
cmds.connectAttr( rl+ prefix + 'PV_ctrl.follow', str(kneeLockCon) + '.firstTerm' )
cmds.setAttr( str(kneeLockCon) + '.operation', 0 )
cmds.setAttr( str(kneeLockCon) + '.secondTerm', 2 )
cmds.setAttr( str(kneeLockCon) + '.colorIfTrueR', 1 )
cmds.setAttr( str(kneeLockCon) + '.colorIfFalseR', 0 )
ctrlFollowCon= cmds.createNode( 'condition', n= rl + prefix + 'ctrlFollow_con01' )
cmds.connectAttr( rl+ prefix + 'PV_ctrl.follow', str(ctrlFollowCon) + '.firstTerm' )
cmds.setAttr( str(ctrlFollowCon) + '.operation', 3 )
cmds.setAttr( str(ctrlFollowCon) + '.secondTerm', 2 )
cmds.setAttr( str(ctrlFollowCon) + '.colorIfTrueR', 1 )
cmds.setAttr( str(ctrlFollowCon) + '.colorIfFalseR', 0 )
cmds.connectAttr( str(ctrlFollowCon) + '.outColorR', str(ctrlFollow[0]) + '.' + rl + prefix + 'IK_ctrlW0' )

######## Knee/Elbow Lock Setup ########
######## autoStretch, KneeSlide, UpperLength & lowerLength ########
connExtraAttrs = ['upperStretch', 'kneeSlide', 'lowerStretch']
MD02List= []
locGrp= cmds.group( n= '%s%sloc_hrc' % ( rl, prefix ), em=1 )

for i, each in enumerate(ikJntSel):
    ikLoc= cmds.spaceLocator( n= str(each).replace( 'drv', 'loc' ) )
    ikLocGrp= cmds.group( n= str(ikLoc[0]) + '_grp', em=0 )
    posLoc= cmds.parentConstraint( each, ikLocGrp, mo=0 )
    cmds.delete( posLoc )
    ikLocMD2= cmds.createNode( 'multiplyDivide', n= str(ikLoc[0]) + '_MD02' )
    MD02List.append(ikLocMD2)
    cmds.connectAttr( str(ikLoc[0]) + 'Shape' + '.worldPosition', str(ikLocMD2) + '.input1' )
    ikLocPMA1= cmds.createNode( 'plusMinusAverage', n= str(ikLoc[0]) + '_pma01' )
    cmds.connectAttr( str(ikLocPMA1) + '.output1D', str(ikLocMD2) + '.input2X' )
    ikLocMD01= cmds.createNode( 'multiplyDivide', n= str(ikLoc[0]) + '_MD01' )
    cmds.setAttr( '%s.input2X' %ikLocMD01, 0.1 )
    cmds.connectAttr( '%s.%s' % (ikCtrl, connExtraAttrs[i]) , str(ikLocMD01) + '.input1X' )
    cmds.connectAttr( str(ikLocMD01) + '.outputX',  str(ikLocPMA1) + '.input1D[0]' )
    cmds.setAttr( str(ikLocPMA1) + '.input1D[1]' , 1 )
    cmds.parent( ikLocGrp, locGrp )
    
cmds.parentConstraint( str(ikJntSel[0]).replace( 'drv', 'loc' ), str(ikJntSel[1]).replace( 'drv', 'loc' ) + '_grp', mo=1 )
cmds.parentConstraint( str(ikJntSel[2]).replace( 'drv', 'loc' ), str(ikJntSel[1]).replace( 'drv', 'loc' ) + '_grp', mo=1 )
locFollow= cmds.parentConstraint( ikCtrl, str(ikJntSel[1]).replace( 'drv', 'loc' ), mo=1 )
ikFollow= cmds.parentConstraint( ikCtrl, str(ikJntSel[2]).replace( 'drv', 'loc' ) + '_grp', mo=1 )
cmds.connectAttr( str(kneeLockCon) + '.outColorR', str(locFollow[0]) + '.' + rl + prefix + 'IK_ctrlW0' )
bln01= cmds.createNode( 'blendColors', n= rl + prefix + 'BLN01' )
cmds.connectAttr( str(ikCtrl) + '.autoStretch', str(bln01) + '.blender' )
cmds.connectAttr( str(kneeLockCon) + '.outColorR', str(bln01) + '.color2R' )
cmds.setAttr( str(bln01) + '.color1R', 1 )
cmds.connectAttr( str( bln01) + '.outputR', str(ikFollow[0]) + '.' + rl + prefix + 'IK_ctrlW0' )

######## distanceNode & stretchy setup ########
DB01= cmds.createNode( 'distanceBetween', n= '%s%sDB01' % (rl, prefix) )
DB02= cmds.createNode( 'distanceBetween', n= '%s%sDB02' % (rl, prefix) )
cmds.connectAttr( '%s.output' % MD02List[0], '%s.point1' % DB01 )
cmds.connectAttr( '%s.output' % MD02List[1], '%s.point2' % DB01 )
cmds.connectAttr( '%s.output' % MD02List[1], '%s.point1' % DB02 )
cmds.connectAttr( '%s.output' % MD02List[2], '%s.point2' % DB02 )
stretchPMA= cmds.createNode( 'plusMinusAverage', n= '%s%sstretch_pma01' % (rl, prefix) )
cmds.connectAttr( '%s.distance' % DB01, '%s.input1D[0]' % stretchPMA )
cmds.connectAttr( '%s.distance' % DB02, '%s.input1D[1]' % stretchPMA )
stretchMD= cmds.createNode( 'multiplyDivide', n= '%s%sstretch_MD01' % (rl, prefix) )
cmds.connectAttr( '%s.output1D' % stretchPMA, '%s.input1X' % stretchMD )
totalLength= cmds.getAttr( '%s.output1D' % stretchPMA )
cmds.setAttr( '%s.input2X' % stretchMD, totalLength )
cmds.setAttr( '%s.operation' % stretchMD, 2 )
bta01= cmds.createNode( 'blendTwoAttr', n= '%s%sBTA01' % (rl, prefix) )
cmds.connectAttr( '%s.distance' % DB01, '%s.input[0]' % bta01 )
cmds.connectAttr( '%s.outputX' % stretchMD,  '%s.input[1]' % bta01 )
cmds.connectAttr(  '%s.output' % bta01, '%s.tx' % ikJntSel[1] )
bta02= cmds.createNode( 'blendTwoAttr', n= '%s%sBTA02' % (rl, prefix) )
cmds.connectAttr( '%s.distance' % DB02, '%s.input[0]' % bta02 )
cmds.connectAttr( '%s.outputX' % stretchMD,  '%s.input[1]' % bta02 )
cmds.connectAttr(  '%s.output' % bta02, '%s.tx' % ikJntSel[2] )

######## setup rotateAim_up  ########
loc1= cmds.spaceLocator( n= '%s%sdist_loc1' % (rl, prefix) )
loc1Snap= cmds.pointConstraint( str(ikJntSel[0]).replace( 'drv', 'loc' ), loc1[0], mo=0 )
cmds.delete( loc1Snap )
cmds.parent( loc1[0], locGrp )
loc2= cmds.spaceLocator( n= '%s%sdist_loc2' % (rl, prefix) )
loc2Snap= cmds.pointConstraint( ikCtrl, loc2[0], mo=0 )
cmds.delete( loc2Snap )
cmds.parent( loc2[0], ikCtrl )
ctrlDB= cmds.createNode( 'distanceBetween', n= '%s%sctrl_DB01' % (rl, prefix) )
cmds.connectAttr( '%s.worldPosition' % loc1[0], '%s.point1' % ctrlDB )
cmds.connectAttr( '%s.worldPosition' % loc2[0], '%s.point2' % ctrlDB )
setR= cmds.createNode( 'setRange', n= '%s%srotateAimUp_SR01' % (rl, prefix) )
distV= cmds.getAttr( '%s.distance' % ctrlDB )
cmds.setAttr( '%s.minX' % setR, -60 )
cmds.setAttr( '%s.oldMinX' % setR, -distV )
cmds.setAttr( '%s.oldMaxX' % setR, distV )
cmds.connectAttr( '%s.distance' % ctrlDB, '%s.valueX' % setR )
ctrlMD= cmds.createNode( 'multiplyDivide', n= '%s%sIK_ctrl_MD01' % (rl,prefix) )
cmds.connectAttr( '%s.outValueX' % setR, '%s.input1X' % ctrlMD )
cmds.setAttr( '%s.input2X' % ctrlMD, 2.5 )
cmds.connectAttr( '%s.outputX' % ctrlMD, '%s.ry' % aimUp )

######## FINAL CLEAN UP  ########
cmds.parent( locGrp, partsGrp )
cmds.parent( selJnt[0], jntGrp, a=1 )
cmds.parent( aimLoc[0], locGrp )
cmds.hide( ikJntSel[0] )
cmds.hide( fkJntSel[0] )
cmds.hide( locGrp )
cmds.hide( loc2[0] )