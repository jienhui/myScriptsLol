import maya.cmds as cmds
import cCtrlHrc_Cl as CC
import cNailCtrlHrc_Cl as CN

# Spine Setup Class

class SpineSetup_Cl():
    def __init__( self, jnt, name ):
        self.jnt= jnt
        self.name= name
        self.cSpineSetup_Fn()
        
    # Main Spine Setup Function
    def cSpineSetup_Fn(self):
                
    # Create IK spine setup
        self.cSpineIK_Fn()
        
    def cSpineIK_Fn(self):
        b= CN.CNailCtrlHrc_Cl()
        c= CC.CCtrlHrc_Cl()
        cmds.select( self.jnt , hi=1 )
        jntChain= cmds.ls( sl=1 )
        self.selJnt= []
        
        for each in jntChain:
            if each.startswith( 'spine' ):
                self.selJnt.append( each )
     
        # find joint position
        self.jntAPos= cmds.xform( self.selJnt[0], q=1, t=1, ws=1 )
        self.jntEndPos= cmds.xform( self.selJnt[-1], q=1, t=1, ws=1 )
        midPosX= ( self.jntAPos[0] + self.jntEndPos[0] )/2
        midPosY= ( self.jntAPos[1] + self.jntEndPos[1] )/2
        midPosZ= ( self.jntAPos[2] + self.jntEndPos[2] )/2
        self.jntMidPos= [ midPosX, midPosY, midPosZ ]
        # create spine curve & spine IkHandle
        self.spineCrv= cmds.curve( n= 'spine_crv', d=2,  p= [(self.jntAPos),(self.jntMidPos),(self.jntEndPos)] )
        self.spineIK= cmds.ikHandle( n='spineIKH', sj= self.selJnt[0], ee= self.selJnt[-1], c= self.spineCrv, sol= 'ikSplineSolver', ccv=0, scv=0 )
        cmds.parent( self.spineCrv, w=1 )
        cmds.select( cl=1 )
        # find spine crurve cv position
        crvShape= cmds.listRelatives( self.spineCrv, s=1 )
        span= cmds.getAttr( '%s.spans' % crvShape[0] )
        deg= cmds.getAttr( '%s.degree' % crvShape[0] )
        numCv= span + deg
        self.drvJntList= []
        self.drvJntGrp= cmds.group( n= '%s_drvJntGrp' % self.name, em=1 )
        self.fkSpaceList= []
        self.fkCtrlList=[]
        numOrder= [ 01, 02, 03 ]
        
        for each,i in enumerate(range( numCv )):
            cv= '%s.cv[%s]' % (crvShape[0], each)
            cvPos= cmds.xform(cv, q=1, t=1, ws=1)
            # create driven joint 
            cmds.select( cl=1 )
            drvJnt= cmds.joint( n='%s0%s_drv' % (self.name, numOrder[i] ), p= cvPos, rad= 3 )
            self.drvJntList.append( drvJnt )
            cmds.select( cl=1 )
            # create IK Controller
            ikCtrl= c.cCtrlHrc_Fn( '%s0%s_IK' % ( self.name, numOrder[i] ) )
            cmds.xform( '%s.cv[*]' % ikCtrl[0][0], ro= [90,0,0] )
            tmpCnst= cmds.parentConstraint( drvJnt, ikCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.parentConstraint( ikCtrl[0], drvJnt, mo=0 )
            # create Fk Controller
            fkCtrl= b.cNailCtrlHrc_Fn( '%s0%s_FK' % ( self.name, numOrder[i] ) )
            self.fkSpaceList.append( fkCtrl[-1] )
            self.fkCtrlList.append( fkCtrl[0] )
            tmpCnst= cmds.parentConstraint( drvJnt, fkCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.parent( ikCtrl[-1], fkCtrl[0] )          
        cmds.skinCluster( self.drvJntList[0], self.drvJntList[1], self.drvJntList[2], self.spineCrv, tsb=1, mi=1, dr=4 )
        cmds.parent( self.fkSpaceList[2], self.fkCtrlList[1] )
        cmds.parent( self.fkSpaceList[1], self.fkCtrlList[0] )
        cmds.parent( self.drvJntList[0], self.drvJntList[1], self.drvJntList[2], self.drvJntGrp )
        cmds.hide( self.drvJntGrp )
        # create curve info node
        crvInfoNode= cmds.arclen( self.spineCrv, ch=1 )
        spineMD01= cmds.createNode( 'multiplyDivide', n= '%s_stretchy_MD01' % self.name )
        cmds.connectAttr( '%s.arcLength' % crvInfoNode, '%s.input1X' % spineMD01 )
        arcLen= cmds.getAttr( '%s.arcLength' % crvInfoNode )
        cmds.setAttr( '%s.input2X' % spineMD01, arcLen )
        cmds.setAttr( '%s.operation' % spineMD01, 2 )
        for each in self.selJnt:
            cmds.connectAttr( '%s.outputX' % spineMD01, '%s.sx' % each )
        # Advanced Twist Setup
        cmds.setAttr( '%s.dTwistControlEnable' % self.spineIK[0], 1 )
        cmds.setAttr( '%s.dWorldUpType' % self.spineIK[0], 4 )
        cmds.setAttr( '%s.dWorldUpAxis' % self.spineIK[0], 0 )
        cmds.setAttr( '%s.dWorldUpVectorX' % self.spineIK[0], 1 )
        cmds.setAttr( '%s.dWorldUpVectorY' % self.spineIK[0], 0 )
        cmds.setAttr( '%s.dWorldUpVectorZ' % self.spineIK[0], 0 )
        cmds.setAttr( '%s.dWorldUpVectorEndX' % self.spineIK[0], 1 )
        cmds.setAttr( '%s.dWorldUpVectorEndY' % self.spineIK[0], 0 )
        cmds.setAttr( '%s.dWorldUpVectorEndZ' % self.spineIK[0], 0 )
        cmds.connectAttr( '%s.worldMatrix' % str(self.drvJntList[0]), '%s.dWorldUpMatrix' % self.spineIK[0] )
        cmds.connectAttr( '%s.worldMatrix' % str(self.drvJntList[2]), '%s.dWorldUpMatrixEnd' % self.spineIK[0] )
        
        return [ self.fkSpaceList[0], self.drvJntGrp, self.spineIK[0], self.spineCrv ]

if __name__ == "__main__":
    abc =SpineSetup_Cl( "spine01_jnt", "spine"  )
