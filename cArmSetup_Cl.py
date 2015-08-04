import maya.cmds as cmds
import cCtrlHrc_Cl as CC

# IK/FK arm setup

class ArmAutoRig_Cl():
    def __init__( self, jnt, clavicle, fingerJntList, name  ):
        self.jnt= jnt
        self.clavicle= clavicle
        self.fingerJntList=  fingerJntList
        self.name= name
        self.cArmAutoRig_Fn()
        
    # Main IK/FK arm Setup Function
    def cArmAutoRig_Fn( self):    
        
    # Identify & Creating Driven Joint Set Function
        cmds.select( self.jnt , hi=1 )
        self.selJnt= cmds.ls( sl=1 )
        self.numJnt= len(self.selJnt)
                
        # Duplicate IK Driven Joints
        dupIK= cmds.duplicate( self.selJnt[0], rc=1 )
        
        while self.numJnt > 3 :
            cmds.delete(dupIK[-1])
            dupIK.remove(dupIK[-1])
            self.numJnt = self.numJnt - 1
        
        for each in dupIK:
            jntNameIK= each.replace( 'jnt1', 'IK_drv' )
            newIK= cmds.rename( each, jntNameIK )
            cmds.select( newIK, add=1 )
        
        self.ikJntSel= cmds.ls( sl=1 )

        # Duplicate FK Driven Joints
        dupFK= cmds.duplicate( self.ikJntSel[0], rc=1 )        
        
        for each in dupFK:
            jntNameFK= each.replace( 'IK_drv1', 'FK_drv' )
            newFK= cmds.rename( each, jntNameFK )
            cmds.select( newFK, add=1 )        
        
        self.fkJntSel= cmds.ls( sl=1 )
        cmds.hide( self.ikJntSel[0], self.fkJntSel[0] )
        
        # Setup Pv Loc Group
        self.pvLoc= cmds.spaceLocator( n='%s_%s_pvLoc' % (self.jnt[0], self.name) )
        self.pvLocGrp= cmds.group( n= '%sGrp' % self.pvLoc[0], em=0 )
        tmpCnst= cmds.parentConstraint( self.ikJntSel[1], self.pvLocGrp, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parent( self.pvLocGrp, self.ikJntSel[1] )
        armLen= cmds.getAttr( '%s.tx' % self.ikJntSel[1] )
        pvPos= -( armLen/2 )
        cmds.setAttr( '%s.tz' % self.pvLocGrp, pvPos )
        cmds.parent( self.pvLocGrp, w=1 )
        cmds.hide( self.pvLocGrp )      
        
    # Create IK/FK Switch Controller & Blending IK/FK driven joints Funtion
        self.cIkFkSwitch_Fn()
        
    def cIkFkSwitch_Fn(self):

        # Create IK/FK Switch Controller
        text= cmds.textCurves( ch=0, f='Times New Roman', t= 'IkFk' )        
        
        for each in range(1,5):
            cmds.rename( 'curve%s' % each, 'ikFk_crv%s' % each )            
        cmds.select( text, hi=1 )
        crvHrc= cmds.ls( '*crv*', s=0 )
        crvShape= crvHrc[4:8]
        crv= crvHrc[0:4]        
        
        for each in crvShape[1:4]:    
            cmds.parent( each, crv[0], r=1, s=1 )            
        
        cmds.move( 1.4,0,0, '%s.cv[*]' % crvShape[1], r=1, os=1, ws=1 )
        cmds.move( 3.7,0,0, '%s.cv[*]' % crvShape[2], r=1, os=1, ws=1 )
        cmds.move( 6.1,0,0, '%s.cv[*]' % crvShape[3], r=1, os=1, ws=1 )
        cmds.select( crv[0], r=1 )
        cmds.xform( crv[0], s=[0.1,0.1,0.1], cp=1 )
        cmds.makeIdentity( crv[0], a=1, t=1, r=1, s=1, n=0 )
        self.IKFKSwitch= cmds.rename( str(crv[0]), '%s_%s_ikFk_ctrl' % (self.jnt[0], self.name) )
        cmds.group( n= '%s_sdk' % self.IKFKSwitch, em=0 )
        cmds.group( n= '%s_align' % self.IKFKSwitch, em=0 )
        self.IKFKSpace= cmds.group( n= '%s_space' % self.IKFKSwitch, em=0 )
        cmds.parent( self.IKFKSpace, w=1 )
        tmpCst= cmds.pointConstraint( self.selJnt[0], self.IKFKSpace, mo=0 )
        cmds.delete( tmpCst )
        cmds.delete( text )
        cmds.setAttr( '%s.tx' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.ty' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.tz' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.rx' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.ry' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.rz' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sx' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.IKFKSwitch, l=1, k=0, cb=0 )
        cmds.addAttr( self.IKFKSwitch, ln= 'ikFkSwitch', at= 'float', hnv=1, min=0, hxv=1, max=1, r=1, k=1, h=0 )
        cmds.setAttr( '%s.ikFkSwitch' % self.IKFKSwitch, k=True, l=False )
        
        # Create Pair Blend node & Blending Joints
        # pairBlend 01
        blnNode1= cmds.pairBlend( nd= self.selJnt[0], at=['tx','ty','tz','rx','ry','rz'] )
        cmds.connectAttr( '%s.ikFkSwitch' % self.IKFKSwitch, '%s.weight' % blnNode1 )
        cmds.connectAttr( '%s.translate' % self.fkJntSel[0], '%s.inTranslate1' % blnNode1 )
        cmds.connectAttr( '%s.rotate' % self.fkJntSel[0], '%s.inRotate1' % blnNode1 )
        cmds.connectAttr( '%s.translate' % self.ikJntSel[0], '%s.inTranslate2' % blnNode1 )
        cmds.connectAttr( '%s.rotate' % self.ikJntSel[0], '%s.inRotate2' % blnNode1 )
        pb01= cmds.rename( blnNode1, str(self.selJnt[0]) + '_PB01' )
        
        # pairBlend 02
        blnNode2= cmds.pairBlend( nd= self.selJnt[1], at=['tx','ty','tz','rx','ry','rz'] )
        cmds.connectAttr( '%s.ikFkSwitch' % self.IKFKSwitch, '%s.weight' % blnNode2 )
        cmds.connectAttr( '%s.translate' % self.fkJntSel[1], '%s.inTranslate1' % blnNode2 )
        cmds.connectAttr( '%s.rotate' % self.fkJntSel[1], '%s.inRotate1' % blnNode2 )
        cmds.connectAttr( '%s.translate' % self.ikJntSel[1], '%s.inTranslate2' % blnNode2 )
        cmds.connectAttr( '%s.rotate' % self.ikJntSel[1], '%s.inRotate2' % blnNode2 )
        pb02= cmds.rename( blnNode2, str(self.selJnt[1]) + '_PB02' )
        
        # pairBlend 03
        blnNode3= cmds.pairBlend( nd= self.selJnt[2], at=['tx','ty','tz','rx','ry','rz'] )
        cmds.connectAttr( '%s.ikFkSwitch' % self.IKFKSwitch, '%s.weight' % blnNode3 )
        cmds.connectAttr( '%s.translate' % self.fkJntSel[2], '%s.inTranslate1' % blnNode3 )
        cmds.connectAttr( '%s.rotate' % self.fkJntSel[2], '%s.inRotate1' % blnNode3 )
        cmds.connectAttr( '%s.translate' % self.ikJntSel[2], '%s.inTranslate2' % blnNode3 )
        cmds.connectAttr( '%s.rotate' % self.ikJntSel[2], '%s.inRotate2' % blnNode3 )
        pb01= cmds.rename( blnNode3, str(self.selJnt[2]) + '_PB03' )
        
    # Setup FK Controller Function
        self.cFkSetup_Fn()
        
    def cFkSetup_Fn(self):
        
        self.fkCtrlList=[]
        self.fkCtrlSpaceList= []
        
        # create clavicle controller
        self.clavicleC= cmds.curve( n= str(self.clavicle).replace( '_jnt','_ctrl' ), d=1, p=([-0.5,0,-1],[-0.9,0,-0.88],[-0.8,0,-0.8],[-1.074,0,-0.506],[-1.194,0,0],[-1.074,0,0.506],[-0.8,0,0.8],[-0.9,0,0.88],[-0.5,0,1],[-0.54,0,0.6],[-0.661,0,0.686],[-0.885,0,0.414],[-1,0,0],[-0.885,0,-0.414],[-0.661,0,-0.686],[-0.54,0,-0.6],[-0.5,0,-1]))
        cmds.xform( self.clavicleC, ro= [0,0,-90] )
        cmds.makeIdentity( self.clavicleC, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%s.sx' % str(self.clavicleC), l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % str(self.clavicleC), l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % str(self.clavicleC), l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % str(self.clavicleC), l=1, k=0, cb=0 )
        cmds.group( n= '%s_sdk' % self.clavicleC, em=0 )
        cmds.group( n= '%s_align' % self.clavicleC, em=0 )
        self.clavicleSpace= cmds.group( n= '%s_space' % self.clavicleC, em=0 )
        tmpCnst= cmds.parentConstraint( self.clavicle, self.clavicleSpace, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parentConstraint( self.clavicleC, self.clavicle, mo=1 )
        
        # create FK controller hierarchy
        for each in self.fkJntSel:
            fkCtrl= cmds.circle( n= str(each).replace( 'drv', 'ctrl' ), ch=0 )
            self.fkCtrlList.append( fkCtrl )
            cmds.xform( fkCtrl, ro= [0,90,0] )
            cmds.makeIdentity( fkCtrl, a=1, t=1, r=1, s=1, n=0 )
            cmds.setAttr( '%s.sx' % str(fkCtrl[0]), l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % str(fkCtrl[0]), l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % str(fkCtrl[0]), l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % str(fkCtrl[0]), l=1, k=0, cb=0 )
            cmds.group( n= '%s_sdk' % str(fkCtrl[0]), em=0 )
            cmds.group( n= '%s_align' % str(fkCtrl[0]), em=0 )
            fkSpace= cmds.group( n= '%s_space' % str(fkCtrl[0]), em=0 )
            self.fkCtrlSpaceList.append ( fkSpace )
            tmpCnt= cmds.parentConstraint( each, fkSpace, mo=0 )
            cmds.delete( tmpCnt )
            cmds.parentConstraint( fkCtrl, each, mo=0 )
        
        cmds.parent( self.fkCtrlSpaceList[2], self.fkCtrlList[1] )
        cmds.parent( self.fkCtrlSpaceList[1], self.fkCtrlList[0] )
        cmds.parentConstraint( self.clavicleC, self.fkCtrlSpaceList[0], mo=1 )
        R01= cmds.createNode( 'reverse', n='fk_ctrl_vis_R01' )
        cmds.connectAttr( '%s.ikFkSwitch' % self.IKFKSwitch, '%s.inputX' % R01 )
        cmds.connectAttr( '%s.outputX' % R01, '%s.v' % self.fkCtrlSpaceList[0] )
        
    # Setup IK Controller Function
        self.cIKSetup_Fn()
        
    def cIKSetup_Fn(self) :
        
        # create IK Controller
        self.extraAttrs = ['autoStretch', 'upperStretch', 'lowerStretch', 'kneeSlide']
        self.ikH= cmds.ikHandle( n= '%s_%s_ikHandle' % (self.jnt[0], self.name) , sj= self.ikJntSel[0], ee=self.ikJntSel[2], sol= 'ikRPsolver', p=1, w=1 )
        self.ikCtrl= cmds.curve( n= '%s_%s_IK_ctrl' % (self.jnt[0], self.name), d=1, 
        p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)] )
        cmds.setAttr( '%s.sx' % self.ikCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.ikCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.ikCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.ikCtrl, l=1, k=0, cb=0 )
        cmds.addAttr( self.ikCtrl, ln='EXTRA', at='enum', en='-' )
        cmds.setAttr( '%s.EXTRA' % self.ikCtrl,e=1, l=False, k=True, cb=True )
        cmds.addAttr( self.ikCtrl, ln='autoStretch', at= 'enum', en= 'Off:On'  )
        cmds.setAttr( '%s.autoStretch' % self.ikCtrl, e=1, l=False, k=True )
        cmds.addAttr( self.ikCtrl, ln='upperStretch', at='float' )
        cmds.setAttr( '%s.upperStretch' % self.ikCtrl, e=1, l=False, k=True )
        cmds.addAttr( self.ikCtrl, ln='lowerStretch', at='float' )
        cmds.setAttr( '%s.lowerStretch' % self.ikCtrl, e=1, l=False, k=True )
        cmds.addAttr( self.ikCtrl, ln='kneeSlide', at='float' )
        cmds.setAttr( '%s.kneeSlide' % self.ikCtrl, e=1, l=False, k=True )
        cmds.addAttr( self.ikCtrl, ln='twist', at='float' )
        cmds.setAttr( '%s.twist' % self.ikCtrl, e=1, l=False, k=True )
        cmds.connectAttr( '%s.twist' % self.ikCtrl, '%s.twist' % self.ikH[0] )
        cmds.group( n= '%s_sdk' % self.ikCtrl, em=0 )
        cmds.group( n= '%s_align' % self.ikCtrl, em=0 )
        self.ikSpace= cmds.group( n= '%s_ctrl' % self.ikCtrl + '_space', em=0 )
        tmpCnst= cmds.parentConstraint( self.ikJntSel[2], self.ikSpace, mo=0 )
        cmds.delete ( tmpCnst )
        cmds.orientConstraint( self.ikCtrl, self.ikJntSel[2], mo=1 )
        cmds.parent( self.ikH[0], self.ikCtrl )
        cmds.hide( self.ikH[0] )
        
        # Setup PV hrc
        self.pvCtrl= cmds.curve( n= '%s_%s_PV_ctrl' % (self.jnt[0], self.name), d=1, 
        p=[(0,0,1),(0,0.5,0.87),(0,0.87,0.5),(0,1,0),(0,0.87,-0.5),(0,0.5,-0.87),(0,0,-1),(0,-0.5,-0.87),(0,-0.87,-0.5),(0,-1,0),(0,-0.87,0.5),(0,-0.5,0.87),(0,0,1),(0.71,0,0.71),(1,0,0),(0.71,0,-0.71),(0,0,-1),(-0.71,0,-0.71),(-1,0,0),(-0.87,0.5,0),(-0.5,0.87,0),(0,1,0),(0.5,0.87,0),(0.87,0.5,0),(1,0,0),(0.87,-0.5,0),(0.5,-0.87,0),(0,-1,0),(-0.5,-0.87,0),(-0.87,-0.5,0),(-1,0,0),(-0.71,0,0.71),(0,0,1)] )
        cmds.setAttr( '%s.rx' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.ry' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.rz' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sx' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.pvCtrl, l=1, k=0, cb=0 )
        cmds.addAttr( self.pvCtrl, ln='SPACE', at='enum', en='-' )
        cmds.setAttr( '%s.SPACE' % self.pvCtrl, e=1, l=False, k=True, cb=True )
        cmds.addAttr( self.pvCtrl, ln='follow', at='enum', en='World:Auto:Lock:Ctrl' )
        cmds.setAttr( '%s.follow' % self.pvCtrl, e=1, l=False, k=True )
        cmds.setAttr( '%s.follow' % self.pvCtrl, 1 )
        cmds.group( n= '%s_sdk' % self.pvCtrl, em=0 )
        cmds.group( n= '%s_align' % self.pvCtrl, em=0 )
        self.pvSpace= cmds.group( n= '%s_space' % self.pvCtrl, em=0 )
        snapPos= cmds.pointConstraint( self.pvLoc, self.pvSpace, mo=0 )
        cmds.delete( snapPos )
        cmds.poleVectorConstraint( self.pvLoc, self.ikH[0] )
        cmds.pointConstraint( self.pvCtrl, self.pvLoc, mo=1 )
        cmds.hide( self.pvLoc )

        # Create Rotate Aim Up Hierarchy
        aimUp= cmds.group( n= '%s_%s_rotateAim_up' % (self.jnt[0], self.name), em=1 )
        aimGrp= cmds.group( n= '%s_%s_rotateAim_upGrp' % (self.jnt[0], self.name), em=0 )
        self.aimHrc= cmds.group( n= '%s_%s_rotateAim_hrc' % (self.jnt[0], self.name), em=0 )
        tmpCn= cmds.parentConstraint( self.ikJntSel[0], self.aimHrc, mo=0 )
        cmds.delete( tmpCn )
        aimLoc= cmds.spaceLocator( n= '%s_%s_aimLoc' % (self.jnt[0], self.name) )
        self.aimLocGrp= cmds.group( n= '%sGrp' % str(aimLoc[0]), em=0 )
        tmpCn= cmds.parentConstraint( self.ikJntSel[0], self.aimLocGrp, mo=0 )
        cmds.delete( tmpCn )
        cmds.xform( aimLoc[0], t= [0,1,0] )
        tmpAim= cmds.aimConstraint( self.ikCtrl, self.aimHrc, mo=1, aim=[1,0,0], u=[0,1,0], wut= "objectrotation", wuo= str(aimLoc[0]) )
        cmds.delete( tmpAim )
        aimFollow= cmds.aimConstraint( self.ikCtrl, aimGrp, mo=1, aim=[1,0,0], u=[0,1,0], wut= "objectrotation", wuo= str(aimLoc[0]) )
        cmds.parent( self.pvSpace, aimUp )
        ctrlFollow= cmds.parentConstraint( self.ikCtrl, self.pvSpace,  mo=1 )
        self.ikCtrlGrp= cmds.group( n= '%s_%s_IK_ctrlGrp' % (self.jnt[0], self.name), em=1 )
        cmds.parent( self.ikSpace, self.aimHrc, self.ikCtrlGrp )
        cmds.connectAttr( '%s.ikFkSwitch' % self.IKFKSwitch, '%s.v' % self.ikCtrlGrp )
        cmds.parentConstraint( self.clavicleC, self.aimLocGrp, mo=1 )
        
        
        # Create Condition node
        
        # Aim Lock Condition
        aimLockCon= cmds.createNode( 'condition', n= '%s_%s_aimLock_con01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.follow' % self.pvCtrl, '%s.firstTerm' % str(aimLockCon) )
        cmds.setAttr( '%s.operation' % str(aimLockCon) , 1 )
        cmds.setAttr( '%s.secondTerm' % str(aimLockCon), 1 )
        cmds.setAttr( '%s.colorIfTrueR' % str(aimLockCon), 0 )
        cmds.setAttr( '%s.colorIfFalseR' % str(aimLockCon), 1 )
        cmds.connectAttr( '%s.outColorR' % str(aimLockCon), str(aimFollow[0]) + '.%sW0' % self.ikCtrl )
        
        # Knee Lock Condition
        kneeLockCon= cmds.createNode( 'condition', n= '%s_%s_kneeLock_con01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.follow' % self.pvCtrl, str(kneeLockCon) + '.firstTerm' )
        cmds.setAttr( '%s.operation' % str(kneeLockCon), 0 )
        cmds.setAttr( '%s.secondTerm' % str(kneeLockCon), 2 )
        cmds.setAttr( '%s.colorIfTrueR' % str(kneeLockCon), 0 )
        cmds.setAttr( '%s.colorIfFalseR' % str(kneeLockCon), 1 )
        cmds.setAttr( '%s.colorIfTrueG' % str(kneeLockCon), 1 )
        cmds.setAttr( '%s.colorIfFalseG' % str(kneeLockCon), 0 )
       
        # Controller Follow Condition
        ctrlFollowCon= cmds.createNode( 'condition', n= '%s_%s_ctrlFollow_con01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.follow' % self.pvCtrl, str(ctrlFollowCon) + '.firstTerm' )
        cmds.setAttr( '%s.operation' % str(ctrlFollowCon), 3 )
        cmds.setAttr( '%s.secondTerm' % str(ctrlFollowCon), 2 )
        cmds.setAttr( '%s.colorIfTrueR' % str(ctrlFollowCon), 1 )
        cmds.setAttr( '%s.colorIfFalseR' % str(ctrlFollowCon), 0 )
        cmds.connectAttr( '%s.outColorR' % str(ctrlFollowCon), str(ctrlFollow[0]) + '.%sW0' % self.ikCtrl )
        
        # Knee/elbow Lock setup
       
        connExtraAttrs = ['upperStretch', 'kneeSlide', 'lowerStretch']
        self.ikLocList=[]
        self.ikLocGrpList=[]
        MD02List= []
        self.locGrp= cmds.group( n= '%s_%s_loc_hrc' % (self.jnt[0], self.name), em=1 )
        cmds.parent( self.aimLocGrp, self.pvLocGrp, self.locGrp )   
        
        for i, each in enumerate(self.ikJntSel):
            ikLoc= cmds.spaceLocator( n= str(each).replace( 'drv', 'loc' ) )
            self.ikLocList.append( ikLoc )
            ikLocGrp= cmds.group( n= '%s_grp' % str(ikLoc[0]), em=0 )
            self.ikLocGrpList.append( ikLocGrp )
            posLoc= cmds.parentConstraint( each, ikLocGrp, mo=0 )
            cmds.delete( posLoc )
            ikLocMD2= cmds.createNode( 'multiplyDivide', n= '%s_MD02' % str(ikLoc[0]) )
            MD02List.append(ikLocMD2)
            cmds.connectAttr( '%sShape.worldPosition' % str(ikLoc[0]), '%s.input1' % str(ikLocMD2) )
            ikLocPMA1= cmds.createNode( 'plusMinusAverage', n= '%s_pma01' % str(ikLoc[0]) )
            cmds.connectAttr( '%s.output1D' % str(ikLocPMA1), '%s.input2X' % str(ikLocMD2) )
            ikLocMD01= cmds.createNode( 'multiplyDivide', n= '%s_MD01' % str(ikLoc[0]) )
            cmds.setAttr( '%s.input2X' %ikLocMD01, 0.1 )
            cmds.connectAttr( '%s.%s' % (self.ikCtrl, connExtraAttrs[i]) , '%s.input1X' % str(ikLocMD01) )
            cmds.connectAttr( '%s.outputX' % str(ikLocMD01), '%s.input1D[0]' % str(ikLocPMA1) )
            cmds.setAttr( '%s.input1D[1]' % str(ikLocPMA1) , 1 )
            cmds.parent( ikLocGrp, self.locGrp )
            cmds.hide( self.locGrp )            
        
        cmds.setAttr( '%s_MD01.input2X' % self.ikLocList[0][0], -0.1 )
        kneeCnst= cmds.parentConstraint( self.ikLocList[0], self.ikLocList[2], self.ikLocGrpList[1], mo=1 )
        locFollow= cmds.parentConstraint( self.ikCtrl, self.ikLocList[1], mo=1 )
        ikFollow= cmds.parentConstraint( self.ikCtrl, self.ikLocGrpList[2], mo=1 )
        cogFollow= cmds.parentConstraint( self.ikJntSel[0], self.ikLocGrpList[0], mo=1 )
        cmds.connectAttr( '%s.outColorR' % str(kneeLockCon), '%s.' % str(kneeCnst[0]) + '%sW0' % str(self.ikLocList[0][0]) )
        cmds.connectAttr( '%s.outColorR' % str(kneeLockCon), '%s.' % str(kneeCnst[0]) + '%sW1' % str(self.ikLocList[2][0]) )
        cmds.connectAttr( '%s.outColorG' % str(kneeLockCon), '%s.' % str(locFollow[0])+ '%sW0' % self.ikCtrl )
        bln01= cmds.createNode( 'blendColors', n= '%s_%s_BLN01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.autoStretch' % self.ikCtrl, '%s.blender' % str(bln01) )
        cmds.connectAttr( '%s.outColorG' % str(kneeLockCon), '%s.color2R' % str(bln01) )
        cmds.connectAttr( '%s.outColorG' % str(kneeLockCon), '%s.color2G' % str(bln01) )
        cmds.setAttr( str(bln01) + '.color1R', 1 )
        cmds.setAttr( str(bln01) + '.color1G', 1 )
        cmds.connectAttr( str( bln01) + '.outputR', str(ikFollow[0]) + '.%sW0' % self.ikCtrl )
        cmds.connectAttr( str( bln01) + '.outputG', '%s.' % str(cogFollow[0]) + '%sW0' % self.ikJntSel[0] )
        
        # create distance node and stretchy setup
        DB01= cmds.createNode( 'distanceBetween', n= '%s_%s_DB01' % (self.jnt[0], self.name) )
        DB02= cmds.createNode( 'distanceBetween', n= '%s_%s_DB02' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.output' % MD02List[0], '%s.point1' % DB01 )
        cmds.connectAttr( '%s.output' % MD02List[1], '%s.point2' % DB01 )
        cmds.connectAttr( '%s.output' % MD02List[1], '%s.point1' % DB02 )
        cmds.connectAttr( '%s.output' % MD02List[2], '%s.point2' % DB02 )
        stretchPMA= cmds.createNode( 'plusMinusAverage', n= '%s_%s_stretch_pma01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.distance' % DB01, '%s.input1D[0]' % stretchPMA )
        cmds.connectAttr( '%s.distance' % DB02, '%s.input1D[1]' % stretchPMA )
        stretchMD= cmds.createNode( 'multiplyDivide', n= '%s_%s_stretch_MD01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.output1D' % stretchPMA, '%s.input1X' % stretchMD )
        totalLength= cmds.getAttr( '%s.output1D' % stretchPMA )
        cmds.setAttr( '%s.input2X' % stretchMD, totalLength )
        cmds.setAttr( '%s.operation' % stretchMD, 2 )

        if self.selJnt[0].startswith( 'l_' ):
            bta01= cmds.createNode( 'blendTwoAttr', n= '%s_%s_BTA01' % (self.jnt[0], self.name) )
            cmds.connectAttr( '%s.distance' % DB01, '%s.input[0]' % bta01 )
            cmds.connectAttr( '%s.outputX' % stretchMD,  '%s.input[1]' % bta01 )
            cmds.connectAttr(  '%s.output' % bta01, '%s.tx' % self.ikJntSel[1] )
            bta02= cmds.createNode( 'blendTwoAttr', n= '%s_%s_BTA02' % (self.jnt[0], self.name) )
            cmds.connectAttr( '%s.distance' % DB02, '%s.input[0]' % bta02 )
            cmds.connectAttr( '%s.outputX' % stretchMD,  '%s.input[1]' % bta02 )
            cmds.connectAttr(  '%s.output' % bta02, '%s.tx' % self.ikJntSel[2] )
            
        if self.selJnt[0].startswith( 'r_' ):
            negMD01= cmds.createNode( 'multiplyDivide', n= '%s_%s_Neg_MD01' % (self.jnt[0], self.name) )
            bta01= cmds.createNode( 'blendTwoAttr', n= '%s_%s_BTA01' % (self.jnt[0], self.name) )
            cmds.connectAttr( '%s.distance' % DB01, '%s.input[0]' % bta01 )
            cmds.connectAttr( '%s.outputX' % stretchMD,  '%s.input[1]' % bta01 )
            cmds.connectAttr( '%s.output' % bta01, '%s.input1X' % negMD01 )
            cmds.setAttr( '%s.input2X' % negMD01, -1 )
            cmds.connectAttr( '%s.outputX' % negMD01, '%s.tx' % self.ikJntSel[1] )
            bta02= cmds.createNode( 'blendTwoAttr', n= '%s_%s_BTA02' % (self.jnt[0], self.name) )
            cmds.connectAttr( '%s.distance' % DB02, '%s.input[0]' % bta02 )
            cmds.connectAttr( '%s.outputX' % stretchMD,  '%s.input[1]' % bta02 )
            cmds.connectAttr( '%s.output' % bta02, '%s.input1Y' % negMD01 )
            cmds.setAttr( '%s.input2Y' % negMD01, -1 )
            cmds.connectAttr( '%s.outputY' % negMD01, '%s.tx' % self.ikJntSel[2] )
            
        # Setup RotateAim_up
        self.distLoc1= cmds.spaceLocator( n= '%s_%s_dist_loc1' % (self.jnt[0], self.name) )
        loc1Snap= cmds.pointConstraint( self.ikJntSel[0], self.distLoc1[0], mo=0 )
        cmds.delete( loc1Snap )
        cmds.parent( self.distLoc1[0], self.locGrp )
        loc2= cmds.spaceLocator( n= '%s_%s_dist_loc2' % (self.jnt[0], self.name) )
        loc2Snap= cmds.pointConstraint( self.ikCtrl, loc2[0], mo=0 )
        cmds.delete( loc2Snap )
        cmds.parent( loc2[0], self.ikCtrl )
        ctrlDB= cmds.createNode( 'distanceBetween', n= '%s_%s_ctrl_DB01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.worldPosition' % self.distLoc1[0], '%s.point1' % ctrlDB )
        cmds.connectAttr( '%s.worldPosition' % loc2[0], '%s.point2' % ctrlDB )
        setR= cmds.createNode( 'setRange', n= '%s_%s_rotateAimUp_SR01' % (self.jnt[0], self.name) )
        distV= cmds.getAttr( '%s.distance' % ctrlDB )
        cmds.setAttr( '%s.minX' % setR, -60 )
        cmds.setAttr( '%s.oldMinX' % setR, -distV )
        cmds.setAttr( '%s.oldMaxX' % setR, distV )
        cmds.connectAttr( '%s.distance' % ctrlDB, '%s.valueX' % setR )
        ctrlMD= cmds.createNode( 'multiplyDivide', n= '%s_%s_IK_ctrl_MD01' % (self.jnt[0], self.name) )
        cmds.connectAttr( '%s.outValueX' % setR, '%s.input1X' % ctrlMD )
        cmds.setAttr( '%s.input2X' % ctrlMD, -2.5 )
        cmds.connectAttr( '%s.outputX' % ctrlMD, '%s.ry' % aimUp )
        cmds.hide( self.distLoc1, loc2 )
        cmds.parentConstraint( self.clavicleC, self.distLoc1[0], mo=1 )
        
        # Hand Setup
        self.cHandSetup_Fn()
        
    def cHandSetup_Fn(self):
        
        c= CC.CCtrlHrc_Cl()
        
        # Create Finger Controllers
        cmds.select( cl=1 )
        # Thumb List
        cmds.select( self.fingerJntList[0], hi=1 )
        thumb= cmds.ls( sl=1 )
        if len(thumb) > 3 :
            thumb.remove( thumb[-1] )     
        cmds.select( cl=1 )
        thumbCtrlList= []
        thumbSpaceList=[]
        # Thumb Ctrl
        for each in thumb:               
            thumbCtrl= c.cCtrlHrc_Fn( str(each).split( '_jnt' )[0] )
            thumbCtrlList.append( thumbCtrl[0] )
            thumbSpaceList.append( thumbCtrl[-1] )
            tmpCnst= cmds.parentConstraint( each, thumbCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.xform( '%s.cv[*]' % thumbCtrl[0][0], ro= [0,90,0] )
            cmds.parentConstraint( thumbCtrl[0], each, mo=1 )
        cmds.parent( thumbSpaceList[-1], thumbCtrlList[1] )
        cmds.parent( thumbSpaceList[1], thumbCtrlList[0] )
        
        # Index List
        cmds.select( self.fingerJntList[1], hi=1 )
        index= cmds.ls( sl=1 )
        if len(index) > 3 :
            index.remove( index[-1] )     
        cmds.select( cl=1 )
        indexCtrlList= []
        indexSpaceList=[]
        # Index Ctrl
        for each in index:               
            indexCtrl= c.cCtrlHrc_Fn( str(each).split( '_jnt' )[0] )
            indexCtrlList.append( indexCtrl[0] )
            indexSpaceList.append( indexCtrl[-1] )
            tmpCnst= cmds.parentConstraint( each, indexCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.xform( '%s.cv[*]' % indexCtrl[0][0], ro= [0,90,0] )
            cmds.parentConstraint( indexCtrl[0], each, mo=1 )
        cmds.parent( indexSpaceList[3], indexCtrlList[2] )
        cmds.parent( indexSpaceList[2], indexCtrlList[1] )
        cmds.parent( indexSpaceList[1], indexCtrlList[0] )
             
        # Middle List
        cmds.select( self.fingerJntList[2], hi=1 )
        middle= cmds.ls( sl=1 )
        if len(middle) > 3 :
            middle.remove( middle[-1] )     
        cmds.select( cl=1 )
        middleCtrlList= []
        middleSpaceList=[]
        # Middle Ctrl
        for each in middle:               
            middleCtrl= c.cCtrlHrc_Fn( str(each).split( '_jnt' )[0] )
            middleCtrlList.append( middleCtrl[0] )
            middleSpaceList.append( middleCtrl[-1] )
            tmpCnst= cmds.parentConstraint( each, middleCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.xform( '%s.cv[*]' % middleCtrl[0][0], ro= [0,90,0] )
            cmds.parentConstraint( middleCtrl[0], each, mo=1 )
        cmds.parent( middleSpaceList[3], middleCtrlList[2] )
        cmds.parent( middleSpaceList[2], middleCtrlList[1] )
        cmds.parent( middleSpaceList[1], middleCtrlList[0] )
        
        # Ring List
        cmds.select( self.fingerJntList[3], hi=1 )
        ring= cmds.ls( sl=1 )
        if len(ring) > 3 :
            ring.remove( ring[-1] )     
        cmds.select( cl=1 )
        ringCtrlList= []
        ringSpaceList=[]
        # Ring Ctrl
        for each in ring:               
            ringCtrl= c.cCtrlHrc_Fn( str(each).split( '_jnt' )[0] )
            ringCtrlList.append( ringCtrl[0] )
            ringSpaceList.append( ringCtrl[-1] )
            tmpCnst= cmds.parentConstraint( each, ringCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.xform( '%s.cv[*]' % ringCtrl[0][0], ro= [0,90,0] )
            cmds.parentConstraint( ringCtrl[0], each, mo=1 )
        cmds.parent( ringSpaceList[3], ringCtrlList[2] )
        cmds.parent( ringSpaceList[2], ringCtrlList[1] )
        cmds.parent( ringSpaceList[1], ringCtrlList[0] )
        
        # Pinky List
        cmds.select( self.fingerJntList[4], hi=1 )
        pinky= cmds.ls( sl=1 )
        if len(pinky) > 3 :
            pinky.remove( pinky[-1] )     
        cmds.select( cl=1 )
        pinkyCtrlList= []
        pinkySpaceList=[]
        # Pinky Ctrl
        for each in pinky:               
            pinkyCtrl= c.cCtrlHrc_Fn( str(each).split( '_jnt' )[0] )
            pinkyCtrlList.append( pinkyCtrl[0] )
            pinkySpaceList.append( pinkyCtrl[-1] )
            tmpCnst= cmds.parentConstraint( each, pinkyCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.xform( '%s.cv[*]' % pinkyCtrl[0][0], ro= [0,90,0] )
            cmds.parentConstraint( pinkyCtrl[0], each, mo=1 )
        cmds.parent( pinkySpaceList[3], pinkyCtrlList[2] )
        cmds.parent( pinkySpaceList[2], pinkyCtrlList[1] )
        cmds.parent( pinkySpaceList[1], pinkyCtrlList[0] )
        self.handGrp= cmds.group( n='%s_hand_ctrlGrp' % self.jnt[0], em=1 )
        cmds.parent( thumbSpaceList[0], indexSpaceList[0], middleSpaceList[0], ringSpaceList[0], pinkySpaceList[0], self.handGrp )
        cmds.parentConstraint( self.selJnt[3], self.handGrp, mo=1 )
             
                        
        return [ self.clavicleSpace, self.IKFKSpace, self.fkCtrlSpaceList[0], self.ikCtrlGrp, self.handGrp, self.locGrp, self.aimHrc ]
        
#if __name__ == '__main__':
#    abc= ArmAutoRig_Cl( 'l_shd01_jnt', 'l_clavicle01_jnt',[ 'l_thumb01_jnt', 'l_index00_jnt', 'l_middle00_jnt', 'l_ring00_jnt', 'l_pinky00_jnt'], 'arm' )
