import maya.cmds as cmds
import cCtrlHrc_Cl as CC

# Bendy Setup Class

class BendySetup_Cl():
    def __init__( self, crv, name ):
        self.crv= crv
        self.name=  name
        self.cBendySetup_Fn()
    #     Main Bendy Setup Function    
    def cBendySetup_Fn( self ):
    #     get CVs Position 
        self.cBendyCvsPos_Fn()
    
    def cBendyCvsPos_Fn( self ):
        crvShape= cmds.listRelatives( self.crv, s=1 )
        span= cmds.getAttr( '%s.spans' % crvShape[0] )
        deg= cmds.getAttr( '%s.degree' % crvShape[0] )
        numCV= span + deg
        
        self.cvPosList= []
            
        for each in range( numCV ):
            cv= '%s.cv[%s]' % ( crvShape[0], each )
            vertPos= cmds.xform( cv, q=1, t=1, ws=1 )
            self.cvPosList.append( vertPos )
            
        #     create Joint
        self.cBendyJoint_Fn()
    
    def cBendyJoint_Fn( self ):
        cmds.select(cl=1)
        
        self.bendyJntList= []
        jntList= []
        jntNum= [ '1', '3', '5' ]
                
        for i, each in enumerate( self.cvPosList ):
            cmds.select( cl=1 )
            bendyJnt= cmds.joint( n= '%s_bendy0%s_jnt' % ( self.name, jntNum[i] ) )
            cmds.xform( bendyJnt, t= each )
            cmds.select( cl=1 )
            jntList.append( bendyJnt )
                   
        #    Oreint Bendy Joint01 
        tmpAim01= cmds.aimConstraint( jntList[1], jntList[0], mo=0 )
        cmds.delete( tmpAim01 )
        cmds.makeIdentity( jntList[0], a=1, t=1, r=1, s=1 )
        self.bendyJntList.append( jntList[0] )
        
        #    Oreint Bendy Joint02
        tmpAim02= cmds.aimConstraint( jntList[2], jntList[1], mo=0 )
        cmds.delete( tmpAim02 )
        cmds.makeIdentity( jntList[1], a=1, t=1, r=1, s=1 )
        cmds.parent( jntList[1], jntList[0] )
        
        #    Oreint Bendy Joint03
        tmpAim03= cmds.aimConstraint( jntList[1], jntList[2], mo=0, aim= [-1,0,0], u= [0,1,0], wut= 'vector', wu= [0,1,0] )
        cmds.delete( tmpAim03 )
        cmds.makeIdentity( jntList[2], a=1, t=1, r=1, s=1 )
        cmds.parent( jntList[2], jntList[1] ) 
        
        jnt03XPos= cmds.getAttr( '%s.tx' % jntList[1] )
        jnt05XPos= cmds.getAttr( '%s.tx' % jntList[2] )
        jnt02XPos= jnt03XPos/2
        jnt04XPos= jnt05XPos/2
               
        #    BendyJnt02
        jnt02= cmds.joint( n= '%s_bendy02_jnt' % self.name )
        tmpConst01= cmds.parentConstraint ( jntList[0], jnt02, mo=0 )
        cmds.delete( tmpConst01 )
        cmds.makeIdentity( jnt02, a=1, t=1, r=1, s=1 )
        cmds.parent( jnt02, jntList[0] )
        cmds.xform( jnt02, t= [jnt02XPos,0,0] )
        cmds.parent( jntList[1], jnt02 )
        self.bendyJntList.append( jnt02 )
        self.bendyJntList.append( jntList[1] )
        cmds.select( cl=1)
        
        #    BendyJnt04
        jnt04= cmds.joint( n= '%s_bendy04_jnt' % self.name )
        tmpConst02= cmds.parentConstraint ( jntList[1], jnt04, mo=0 )
        cmds.delete( tmpConst02 )
        cmds.makeIdentity( jnt04, a=1, t=1, r=1, s=1 )
        cmds.parent( jnt04, jntList[1] )
        cmds.xform( jnt04, t= [jnt04XPos,0,0] )
        cmds.parent( jntList[2], jnt04 )
        self.bendyJntList.append( jnt04 )
        self.bendyJntList.append( jntList[2] )
        cmds.select( cl=1 )
        
        #    create controller
        self.cBendyController_Fn()
    
    def cBendyController_Fn( self ):
        c= CC.CCtrlHrc_Cl()
        self.bendyLocList=[]
        cmds.select( cl=1 )
        self.ctrlGrp= cmds.group( n= '%s_bendyCtrl_hrc' % self.name, em=1 )
        
        # controller01
        self.bendyCtrl01= c.cCtrlHrc_Fn( '%s_bendy01' % self.name )
        bendyCtrl01Shape= cmds.select( '%s_bendy01_ctrlShape.cv[0:7]' % self.name, r=1 )
        cmds.rotate( '90deg', r= 1, z=1 )
        cmds.select( cl=1 )
        bendyLoc01= cmds.spaceLocator( n= '%s_bendy01_loc' % self.name )
        self.bendyLocList.append( bendyLoc01 )
        cmds.parent( bendyLoc01, self.bendyCtrl01[0] )
        tmpCnt01= cmds.parentConstraint( self.bendyJntList[0], self.bendyCtrl01[-1], mo=0 )
        cmds.delete( tmpCnt01 )
        cmds.parent( self.bendyCtrl01[-1], self.ctrlGrp )
        cmds.connectAttr( '%sShape.worldPosition[0]' % bendyLoc01[0], '%sShape.controlPoints[0]' % self.crv )
        cmds.hide( bendyLoc01 )
        cmds.select( cl=1 )
        
        # controller02
        self.bendyCtrl02= c.cCtrlHrc_Fn( '%s_bendy02' % self.name )
        bendyCtrl02Shape= cmds.select( '%s_bendy02_ctrlShape.cv[0:7]' % self.name, r=1 )
        cmds.rotate( '90deg', r= 1, z=1 )
        cmds.select( cl=1 )
        bendyLoc02= cmds.spaceLocator( n= '%s_bendy02_loc' % self.name )
        self.bendyLocList.append( bendyLoc02 )
        cmds.parent( bendyLoc02[0], self.bendyCtrl02[0] )
        tmpCnt02= cmds.parentConstraint( self.bendyJntList[2], self.bendyCtrl02[-1], mo=0 )
        cmds.delete( tmpCnt02 )
        cmds.parent( self.bendyCtrl02[-1], self.ctrlGrp )
        cmds.connectAttr( '%sShape.worldPosition[0]' % bendyLoc02[0], '%sShape.controlPoints[1]' % self.crv )
        cmds.hide( bendyLoc02 )
        
        # controller03
        self.bendyCtrl03= c.cCtrlHrc_Fn( '%s_bendy03' % self.name )
        bendyCtrl03Shape= cmds.select( '%s_bendy03_ctrlShape.cv[0:7]' % self.name, r=1 )
        cmds.rotate( '90deg', r= 1, z=1 )
        cmds.select( cl=1 )
        bendyLoc03= cmds.spaceLocator( n= '%s_bendy03_loc' % self.name )
        self.bendyLocList.append( bendyLoc03 )
        cmds.parent( bendyLoc03[0], self.bendyCtrl03[0] )
        tmpCnt03= cmds.parentConstraint( self.bendyJntList[4], self.bendyCtrl03[-1], mo=0 )
        cmds.delete( tmpCnt03 )
        cmds.parent( self.bendyCtrl03[-1], self.ctrlGrp )
        cmds.connectAttr( '%sShape.worldPosition[0]' % bendyLoc03[0], '%sShape.controlPoints[2]' % self.crv )
        cmds.hide( bendyLoc03 )
        # add twist attr
        cmds.addAttr( self.bendyCtrl03[0], ln='EXTRA', at='enum', en='-' )
        cmds.setAttr( '%s.EXTRA' % self.bendyCtrl03[0][0], e=1, l=False, k=True, cb=True )
        cmds.addAttr( self.bendyCtrl03[0], ln='twist', at= 'float' )
        cmds.setAttr( '%s.twist' % self.bendyCtrl03[0][0], e=1, l=False, k=True )
        
        #     create xform and twist group
        self.cBendyGrp_Fn()
    
    def cBendyGrp_Fn( self ):
        self.xformGrp= cmds.group( n= '%s_xform_hrc' % self.name, em=1 )
        self.twistGrp= cmds.group( n= '%s_twist_hrc' % self.name, em=1 )
        
        self.xForm1= cmds.group( n= '%s_xform01_grp' % self.name, em=1 )
        self.twist1= cmds.group( n= '%s_twist01_grp' % self.name, em=1 )
        tmpC01= cmds.parentConstraint( self.bendyJntList[0], self.xForm1, mo=0 )
        tmpC02= cmds.parentConstraint( self.bendyJntList[0], self.twist1, mo=0  )
        cmds.delete( tmpC01, tmpC02 )
        cmds.parent( self.xForm1, self.xformGrp )
        cmds.parent( self.twist1, self.twistGrp )
        
        self.xForm2= cmds.group( n= '%s_xform02_grp' % self.name, em=1 )
        self.twist2= cmds.group( n= '%s_twist02_grp' % self.name, em=1 )
        tmpC03= cmds.parentConstraint( self.bendyJntList[1], self.xForm2, mo=0 )
        tmpC04= cmds.parentConstraint( self.bendyJntList[1], self.twist2, mo=0  )
        cmds.delete( tmpC03, tmpC04 )
        cmds.parent( self.xForm2, self.xformGrp )
        cmds.parent( self.twist2, self.twistGrp )
        
        self.xForm3= cmds.group( n= '%s_xform03_grp' % self.name, em=1 )
        self.twist3= cmds.group( n= '%s_twist03_grp' % self.name, em=1 )
        tmpC05= cmds.parentConstraint( self.bendyJntList[2], self.xForm3, mo=0 )
        tmpC06= cmds.parentConstraint( self.bendyJntList[2], self.twist3, mo=0  )
        cmds.delete( tmpC05, tmpC06 )
        cmds.parent( self.xForm3, self.xformGrp )
        cmds.parent( self.twist3, self.twistGrp )
        
        self.xForm4= cmds.group( n= '%s_xform04_grp' % self.name, em=1 )
        self.twist4= cmds.group( n= '%s_twist04_grp' % self.name, em=1 )
        tmpC07= cmds.parentConstraint( self.bendyJntList[3], self.xForm4, mo=0 )
        tmpC08= cmds.parentConstraint( self.bendyJntList[3], self.twist4, mo=0  )
        cmds.delete( tmpC07, tmpC08 )
        cmds.parent( self.xForm4, self.xformGrp )
        cmds.parent( self.twist4, self.twistGrp )
        
        self.xForm5= cmds.group( n= '%s_xform05_grp' % self.name, em=1 )
        self.twist5= cmds.group( n= '%s_twist05_grp' % self.name, em=1 )
        tmpC09= cmds.parentConstraint( self.bendyJntList[4], self.xForm5, mo=0 )
        tmpC10= cmds.parentConstraint( self.bendyJntList[4], self.twist5, mo=0  )
        cmds.delete( tmpC09, tmpC10 )
        cmds.parent( self.xForm5, self.xformGrp )
        cmds.parent( self.twist5, self.twistGrp )
        
        #     create poci node and make connection
        self.cBendyNodes_Fn()

    def cBendyNodes_Fn( self ):
        # poci01
        poci1= cmds.createNode( 'pointOnCurveInfo', n= '%s_poci01' % self.name )
        cmds.connectAttr( '%s_crvShape.worldSpace[0]' % self.name,  '%s.inputCurve' % poci1 )
        cmds.connectAttr( '%s.position' % poci1, '%s.translate' % self.xForm1 )
        cmds.pointConstraint( self.xForm1, self.bendyJntList[0] )
        cmds.tangentConstraint( self.crv, self.bendyJntList[0], wut= 'objectrotation', wuo= str(self.twist1) )
        # MD01
        MD01= cmds.createNode( 'multiplyDivide', n= '%s_MD01' % self.name )
        cmds.connectAttr( '%s.twist' % self.bendyCtrl03[0][0], '%s.input1X' % MD01 )
        cmds.connectAttr( '%s.outputX' % MD01,  '%s.rx' % self.twist1 )
        cmds.setAttr( '%s.input2X' % MD01, 0 )
        
        # poci02
        poci2= cmds.createNode( 'pointOnCurveInfo', n= '%s_poci02' % self.name )
        cmds.connectAttr( '%s_crvShape.worldSpace[0]' % self.name,  '%s.inputCurve' % poci2 )
        cmds.setAttr( '%s.parameter' % poci2, 0.25 )
        cmds.connectAttr( '%s.position' % poci2, '%s.translate' % self.xForm2 )
        cmds.pointConstraint( self.xForm2, self.bendyJntList[1] )
        cmds.tangentConstraint( self.crv, self.bendyJntList[1], wut= 'objectrotation', wuo= str(self.twist2) )
        # MD02
        MD02= cmds.createNode( 'multiplyDivide', n= '%s_MD02' % self.name )
        cmds.connectAttr( '%s.twist' % self.bendyCtrl03[0][0], '%s.input1X' % MD02 )
        cmds.connectAttr( '%s.outputX' % MD02,  '%s.rx' % self.twist2 )
        cmds.setAttr( '%s.input2X' % MD02, 0.25 )
        
        # poci03
        poci3= cmds.createNode( 'pointOnCurveInfo', n= '%s_poci03' % self.name )
        cmds.connectAttr( '%s_crvShape.worldSpace[0]' % self.name,  '%s.inputCurve' % poci3 )
        cmds.setAttr( '%s.parameter' % poci3, 0.5 )
        cmds.connectAttr( '%s.position' % poci3, '%s.translate' % self.xForm3 )
        cmds.pointConstraint( self.xForm3, self.bendyJntList[2] )
        cmds.tangentConstraint( self.crv, self.bendyJntList[2], wut= 'objectrotation', wuo= str(self.twist3) )
        # MD03
        MD03= cmds.createNode( 'multiplyDivide', n= '%s_MD03' % self.name )
        cmds.connectAttr( '%s.twist' % self.bendyCtrl03[0][0], '%s.input1X' % MD03 )
        cmds.connectAttr( '%s.outputX' % MD03,  '%s.rx' % self.twist3 )
        cmds.setAttr( '%s.input2X' % MD03, 0.5 )
        
        # poci04
        poci4= cmds.createNode( 'pointOnCurveInfo', n= '%s_poci04' % self.name )
        cmds.connectAttr( '%s_crvShape.worldSpace[0]' % self.name,  '%s.inputCurve' % poci4 )
        cmds.setAttr( '%s.parameter' % poci4, 0.75 )
        cmds.connectAttr( '%s.position' % poci4, '%s.translate' % self.xForm4 )
        cmds.pointConstraint( self.xForm4, self.bendyJntList[3] )
        cmds.tangentConstraint( self.crv, self.bendyJntList[3], wut= 'objectrotation', wuo= str(self.twist4) )
        # MD04
        MD04= cmds.createNode( 'multiplyDivide', n= '%s_MD04' % self.name )
        cmds.connectAttr( '%s.twist' % self.bendyCtrl03[0][0], '%s.input1X' % MD04 )
        cmds.connectAttr( '%s.outputX' % MD04,  '%s.rx' % self.twist4 )
        cmds.setAttr( '%s.input2X' % MD04, 0.75 )
        
        # poci05
        poci5= cmds.createNode( 'pointOnCurveInfo', n= '%s_poci05' % self.name )
        cmds.connectAttr( '%s_crvShape.worldSpace[0]' % self.name,  '%s.inputCurve' % poci5 )
        cmds.setAttr( '%s.parameter' % poci5, 1 )
        cmds.connectAttr( '%s.position' % poci5, '%s.translate' % self.xForm5 )
        cmds.pointConstraint( self.xForm5, self.bendyJntList[4] )
        cmds.tangentConstraint( self.crv, self.bendyJntList[4], wut= 'objectrotation', wuo= str(self.twist5) )
        # MD05
        MD05= cmds.createNode( 'multiplyDivide', n= '%s_MD05' % self.name )
        cmds.connectAttr( '%s.twist' % self.bendyCtrl03[0][0], '%s.input1X' % MD05 )
        cmds.connectAttr( '%s.outputX' % MD05,  '%s.rx' % self.twist5 )
        cmds.setAttr( '%s.input2X' % MD05, 1 )
        
        #     clean Up
        self.cBendyCleanUp_Fn()
    
    def cBendyCleanUp_Fn( self ):
        self.extraGrp= cmds.group(n='%s_extra_hrc' % self.name, em=1 )
        self.mainGrp= cmds.group(n='%s_bendySetUp' % self.name, em=0 )
        cmds.parent( self.ctrlGrp, self.mainGrp )
        cmds.parent( self.xformGrp, self.extraGrp )
        cmds.parent( self.twistGrp, self.extraGrp )
        cmds.parent( self.crv, self.extraGrp )
        cmds.parent( self.bendyJntList[0], self.extraGrp )
        cmds.parentConstraint( self.bendyCtrl03[0], self.bendyCtrl01[0], self.bendyCtrl02[-1], mo=1 )
        cmds.scaleConstraint( self.ctrlGrp, self.twistGrp, mo=1 )
        cmds.parentConstraint( self.ctrlGrp, self.twistGrp, mo=1 )
        return [ self.ctrlGrp, self.extraGrp, self.mainGrp ]
    
if __name__ == "__main__":
    abc = BendySetup_Cl("bendy_crv", "bendy")    
