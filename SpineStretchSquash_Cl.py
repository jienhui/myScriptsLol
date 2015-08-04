import pymel.core as pm
import CreateController as CC
import CreateGroups as CG
reload(CG)
#    Create Stretch and Squash setup using IKSpline and Gamma Node

class SplineStretchSquash_Cl():
    def __init__(self, startJoint, endJoint, name):
        
        self.startJoint = startJoint
        self.endJoint = endJoint
        self.name = name
        
    def createSSSsetup_Fn(self):
    #    Main function that will be used to create setup.
        self.ikSplineSetup_Fn()

    def ikSplineSetup_Fn(self):
    #    Create ikSpline setup using start joint and end joint
        self.spineIK = pm.ikHandle(name = '%s_IKH' % self.name, sj=self.startJoint, ee=self.endJoint, ccv=1, solver='ikSplineSolver', ns=1)
        eff = pm.rename(self.spineIK[1], '%s_eff' % self.name)
        self.splineCrv = pm.rename(self.spineIK[2], '%s_crv' % self.name)
        pm.select(cl=1)
        
    #    Create IK Controllers for spine setup
        self.ikController_Fn()

    def ikController_Fn(self):
    #    Create IK Controllers for spine setup
        createController = CC.CreateController_Cl()
        createGroups = CG.CreateGroups_Cl()
        
        self.upController = createController.createController_Fn('%s01_IK' % self.name)
        self.upControllerGroups = createGroups.createGroups_Fn(self.upController)

        pm.addAttr(self.upController, ln='stBias', at='double')
        pm.setAttr('%s.stBias' % self.upController, e=1, keyable=1)
        pm.addAttr(self.upController, ln='stVol', at='double', dv=1)
        pm.setAttr('%s.stVol' % self.upController, e=1, keyable=1)

        self.midController = createController.createController_Fn('%s02_IK' % self.name)
        self.midControllerGroups = createGroups.createGroups_Fn(self.midController)
        
        self.lowController = createController.createController_Fn('%s03_IK' % self.name)
        self.lowControllerGroups = createGroups.createGroups_Fn(self.lowController)
        
        upJointPos = pm.xform('%s.cv[4]' % self.splineCrv, q=1, t=1, ws=1)
        lowJointPos = pm.xform('%s.cv[0]' % self.splineCrv, q=1, t=1, ws=1)

        pm.setAttr(self.upControllerGroups[-1].t, upJointPos)
        pm.setAttr(self.lowControllerGroups[-1].t, lowJointPos)
        tmpConst = pm.pointConstraint(self.upControllerGroups[-1],self.lowControllerGroups[-1],
                                      self.midControllerGroups[-1], mo=0)
        pm.delete(tmpConst)
        pm.select(cl=1)
        
        self.lowDrvJoint = pm.joint(n = '%s01_IK_drv' % self.name)
        tmpConst = pm.parentConstraint('%s01_jnt' % self.name, self.lowDrvJoint, mo=0)
        pm.delete(tmpConst)
        pm.select(cl=1)
        
        self.midDrvJoint = pm.joint(n = '%s02_IK_drv' % self.name)
        tmpConst = pm.parentConstraint('%s02_jnt' % self.name, '%s03_jnt' % self.name, self.midDrvJoint, mo=0)
        pm.delete(tmpConst)
        pm.select(cl=1)
        
        self.upDrvJoint = pm.joint(n = '%s03_IK_drv' % self.name)
        tmpConst = pm.parentConstraint('%s04_end' % self.name, self.upDrvJoint, mo=0)
        pm.delete(tmpConst)
        pm.select(cl=1)
        
        self.crvSkinJoint = [self.upDrvJoint, self.midDrvJoint, self.lowDrvJoint]
        pm.select(self.crvSkinJoint, self.splineCrv)
        pm.skinCluster(bindMethod=0, toSelectedBones=1, skinMethod=0, normalizeWeights=1,
                       mi=5, dr=4, rui=1)

        pm.parentConstraint(self.upController, self.upDrvJoint, mo=1)
        pm.parentConstraint(self.midController, self.midDrvJoint, mo=1)
        pm.parentConstraint(self.lowController, self.lowDrvJoint, mo=1)

    #    Create stretchy setup
        self.ikSplineStretchSetup_Fn()

    def ikSplineStretchSetup_Fn(self):
    #    Create stretchy setup
        pm.select(self.splineCrv, r=1)
        crvInfo = pm.arclen(n='%s_curveInfo' % self.name, ch=1)
        crvInfo = pm.rename(crvInfo, '%s_curveInfo' % self.name)
        #    First multiplyDivide node
        mdStretch01 = pm.createNode('multiplyDivide', n='%s_SSS01_md' % self.name)
        pm.setAttr('%s.operation' % mdStretch01, 2)
        pm.setAttr('%s.input1Y' % mdStretch01, 1)
        pm.connectAttr('%s.arcLength' % crvInfo, '%s.input1X' % mdStretch01)
        pm.setAttr('%s.input2X' % mdStretch01, pm.getAttr('%s.arcLength' % crvInfo))
        
        pm.connectAttr('%s.outputX' % mdStretch01, '%s01_jnt.scaleX' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch01, '%s02_jnt.scaleX' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch01, '%s03_jnt.scaleX' % self.name, f=1)
        pm.select(cl=1)

        #    First plusMinusAverage node
        pmaStretch01 = pm.createNode('plusMinusAverage', n='%s_SSS01_pma' % self.name)
        pm.setAttr('%s.operation' % pmaStretch01, 2)
        pm.connectAttr('%s.outputX' % mdStretch01, '%s.input1D[1]' % pmaStretch01, f=1)
        pm.connectAttr('%s.outputY' % mdStretch01, '%s.input1D[0]' % pmaStretch01, f=1)

        mdStretch02 = pm.createNode('multiplyDivide', n='%s_SSS02_md' % self.name)
        pm.connectAttr('%s.output1D' % pmaStretch01, '%s.input2X' % mdStretch02)
        pm.connectAttr('%s.output1D' % pmaStretch01, '%s.input2Y' % mdStretch02)
        pm.connectAttr('%s.output1D' % pmaStretch01, '%s.input2Z' % mdStretch02)

        mdStretch03 = pm.createNode('multiplyDivide', n='%s_SSS03_md' % self.name)
        pm.setAttr('%s.input2X' % mdStretch03, 3)
        pm.setAttr('%s.input2Y' % mdStretch03, 3)
        pm.setAttr('%s.input2Z' % mdStretch03, 3)
        pm.connectAttr('%s.outputX' % mdStretch02, '%s.input1X' % mdStretch03)
        pm.connectAttr('%s.outputY' % mdStretch02, '%s.input1Y' % mdStretch03)
        pm.connectAttr('%s.outputZ' % mdStretch02, '%s.input1Z' % mdStretch03)

        mdStretch04 = pm.createNode('multiplyDivide', n='%s_SSS04_md' % self.name)

        mdStretch05 = pm.createNode('multiplyDivide', n='%s_SSS05_md' % self.name)
        pm.setAttr('%s.input1X' % mdStretch05, 1)
        pm.setAttr('%s.input1Y' % mdStretch05, 1)
        pm.setAttr('%s.input1Z' % mdStretch05, 1)
        pm.connectAttr('%s.stVol' % self.upController, '%s.input1X' % mdStretch05, f=1)
        pm.connectAttr('%s.outputX' % mdStretch05, '%s.input2X' % mdStretch04, f=1)
        pm.connectAttr('%s.outputX' % mdStretch05, '%s.input2Y' % mdStretch04, f=1)
        pm.connectAttr('%s.outputX' % mdStretch05, '%s.input2Z' % mdStretch04, f=1)

        pmaStretch02 = pm.createNode('plusMinusAverage', n='%s_SSS02_pma' % self.name)
        pm.connectAttr('%s.outputX' % mdStretch03, '%s.input1D[0]' % pmaStretch02, f=1)
        pm.connectAttr('%s.outputY' % mdStretch05, '%s.input1D[1]' % pmaStretch02, f=1)
        pm.connectAttr('%s.output1D' % pmaStretch02, '%s.input1X' % mdStretch04)

        pmaStretch03 = pm.createNode('plusMinusAverage', n='%s_SSS03_pma' % self.name)
        pm.connectAttr('%s.outputY' % mdStretch03, '%s.input1D[1]' % pmaStretch03, f=1)
        pm.connectAttr('%s.outputY' % mdStretch05, '%s.input1D[0]' % pmaStretch03, f=1)
        pm.connectAttr('%s.output1D' % pmaStretch03, '%s.input1Z' % mdStretch04)

        pmaStretch04 = pm.createNode('plusMinusAverage', n='%s_SSS04_pma' % self.name)
        pm.connectAttr('%s.outputZ' % mdStretch03, '%s.input1D[1]' % pmaStretch04, f=1)
        pm.connectAttr('%s.outputY' % mdStretch05, '%s.input1D[0]' % pmaStretch04, f=1)
        pm.connectAttr('%s.output1D' % pmaStretch04, '%s.input1Y' % mdStretch04)

        mdStretch06 = pm.createNode('multiplyDivide', n='%s_SSS06_md' % self.name)
        pm.setAttr('%s.input2X' % mdStretch06, -1)
        gammaCorrect = pm.createNode('gammaCorrect', n='%s_gammaCorrect' % self.name)
        pm.setAttr('%s.value' % gammaCorrect, (0.333, 0.667, 0))
        pm.connectAttr('%s.outValueY' % gammaCorrect, '%s.input1X' % mdStretch06, f=1)
        
        pmaStretch05 = pm.createNode('plusMinusAverage', n='%s_SSS05_pma' % self.name)
        pm.connectAttr('%s.outputX' % mdStretch06, '%s.input1D[1]' % pmaStretch05, f=1)
        pm.connectAttr('%s.outputY' % mdStretch06, '%s.input1D[0]' % pmaStretch05, f=1)

        pmaStretch06 = pm.createNode('plusMinusAverage', n='%s_SSS06_pma' % self.name)
        pm.setAttr('%s.operation' % pmaStretch06, 2)
        pm.connectAttr('%s.outValueX' % gammaCorrect, '%s.input1D[1]' % pmaStretch06, f=1)
        pm.connectAttr('%s.outValueY' % gammaCorrect, '%s.input1D[0]' % pmaStretch06, f=1)

        pm.connectAttr('%s.outValueX' % gammaCorrect, '%s.input1X' % mdStretch02, f=1)
        pm.connectAttr('%s.output1D' % pmaStretch06, '%s.input1Z' % mdStretch02, f=1)
        pm.connectAttr('%s.output1D' % pmaStretch05, '%s.input1Y' % mdStretch02, f=1)

        pm.connectAttr('%s.outputX' % mdStretch04, '%s01_jnt.scaleY' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch04, '%s01_jnt.scaleZ' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch04, '%s02_jnt.scaleY' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch04, '%s02_jnt.scaleZ' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch04, '%s03_jnt.scaleY' % self.name, f=1)
        pm.connectAttr('%s.outputX' % mdStretch04, '%s03_jnt.scaleZ' % self.name, f=1)

if __name__ == '__main__':
    sss = SplineStretchSquash_Cl('spine01_jnt', 'spine04_end', 'spine')
    sss.createSSSsetup_Fn()
