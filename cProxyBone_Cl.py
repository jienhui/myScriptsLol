import maya.cmds as cmds

# Proxy Bone Class
class ProxyBone_Cl():
    def __init__( self ):

        # Proxy Bone Function
        self.cProxyBone_Fn()
        
    def cProxyBone_Fn( self ):
        # Create Proxy Arm Bone Loc
        self.L_armGrp= cmds.group( n= 'L_proxyArm_grp', em=1 )
        self.R_armGrp= cmds.group( n= 'R_proxyArm_grp', em=1 )
        self.armList= ['L_clavicle', 'L_shoulder', 'L_elbow', 'L_wrist', 'R_clavicle', 'R_shoulder', 'R_elbow', 'R_wrist']
        self.L_armLoc= []
        self.R_armLoc= []
        self.L_armSpace= []
        self.R_armSpace= []
        for each in self.armList:
            loc= cmds.spaceLocator( n= '%s_loc' % each )
            armSpace= cmds.group( n= '%s_grp' % loc[0], em=0 )
            if str(loc[0]).startswith('L_'):
                self.L_armLoc.append(loc)
                self.L_armSpace.append( armSpace )
                cmds.parent( armSpace, self.L_armGrp )
            else :
                self.R_armLoc.append(loc)
                self.R_armSpace.append( armSpace )
                cmds.parent( armSpace, self.R_armGrp )
            cmds.setAttr( '%sShape.localScaleX' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleY' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleZ' % loc[0], 3 )
            cmds.setAttr( '%s.rx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % loc[0], l=1, k=0, cb=0 )
        for i, each in enumerate( self.L_armLoc ):
            MD= cmds.createNode( 'multiplyDivide', n= '%s_neg_MD01' % each[0] )
            cmds.setAttr( '%s.input2X' % MD, -1 )
            cmds.setAttr( '%s.input2Y' % MD, -1 )
            cmds.connectAttr( '%s.tx' % each[0], '%s.input1X' % MD )
            cmds.connectAttr( '%s.tx' % self.L_armSpace[i], '%s.input1Y' % MD )
            cmds.connectAttr( '%s.outputX' % MD, '%s.tx' % self.R_armLoc[i][0] )
            cmds.connectAttr( '%s.outputY' % MD, '%s.tx' % self.R_armSpace[i] )
            cmds.connectAttr( '%s.ty' % each[0], '%s.ty' % self.R_armLoc[i][0] )
            cmds.connectAttr( '%s.tz' % each[0], '%s.tz' % self.R_armLoc[i][0] )
            cmds.connectAttr( '%s.ty' % self.L_armSpace[i], '%s.ty' % self.R_armSpace[i] )
            cmds.connectAttr( '%s.tz' % self.L_armSpace[i], '%s.tz' % self.R_armSpace[i] )
        # Create Proxy Arm Annotation
        L_clvAnnt= cmds.annotate( self.L_armLoc[1], tx= self.armList[0] )
        cmds.setAttr( '%s.template' % L_clvAnnt, 1 )
        cmds.parent( L_clvAnnt, self.L_armLoc[0] ) 
        L_shdAnnt= cmds.annotate( self.L_armLoc[2], tx= self.armList[1] )
        cmds.setAttr( '%s.template' % L_shdAnnt, 1 )
        cmds.parent( L_shdAnnt, self.L_armLoc[1] )
        L_elbAnnt= cmds.annotate( self.L_armLoc[3], tx= self.armList[2] )
        cmds.setAttr( '%s.template' % L_elbAnnt, 1 ) 
        cmds.parent( L_elbAnnt, self.L_armLoc[2] )
        L_wstAnnt= cmds.annotate( self.L_armLoc[3], tx= self.armList[3] )
        cmds.setAttr( '%s.template' % L_wstAnnt, 1 )
        cmds.parent( L_wstAnnt, self.L_armLoc[3] )
        R_clvAnnt= cmds.annotate( self.R_armLoc[1], tx= self.armList[4] )
        cmds.setAttr( '%s.template' % R_clvAnnt, 1 )
        cmds.parent( R_clvAnnt, self.R_armLoc[0] ) 
        R_shdAnnt= cmds.annotate( self.R_armLoc[2], tx= self.armList[5] )
        cmds.setAttr( '%s.template' % R_shdAnnt, 1 )
        cmds.parent( R_shdAnnt, self.R_armLoc[1] )
        R_elbAnnt= cmds.annotate( self.R_armLoc[3], tx= self.armList[6] )
        cmds.setAttr( '%s.template' % R_elbAnnt, 1 ) 
        cmds.parent( R_elbAnnt, self.R_armLoc[2] )
        R_wstAnnt= cmds.annotate( self.R_armLoc[3], tx= self.armList[7] )
        cmds.setAttr( '%s.template' % R_wstAnnt, 1 )
        cmds.parent( R_wstAnnt, self.R_armLoc[3] )
        # Proxy Bone Position
        cmds.xform( self.L_armSpace[0], t= [ 5.241,142.186,-5.638], a=1 )
        cmds.xform( self.L_armSpace[1], t= [ 16.625,140.633,-7.713], a=1 )
        cmds.xform( self.L_armSpace[2], t= [ 33.337,122.821,-9.709 ], a=1 )
        cmds.xform( self.L_armSpace[3], t= [ 47.712,107.011,-7.058 ], a=1 )
        
        # Create Proxy Leg Bone Loc
        self.L_legGrp= cmds.group( n= 'L_proxyLeg_grp', em=1 )
        self.R_legGrp= cmds.group( n= 'R_proxyLeg_grp', em=1 )
        self.LegList= ['L_hip', 'L_knee', 'L_ankle', 'L_ball', 'L_toe', 'L_heel', 'L_sideL', 'L_sideR', 'L_toeTip', 'R_hip', 'R_knee', 'R_ankle', 'R_ball', 'R_toe', 'R_heel', 'R_sideL', 'R_sideR', 'R_toeTip']
        self.L_legLoc= []
        self.R_legLoc= []
        self.L_legSpace= []
        self.R_legSpace= []
        for each in self.LegList:
            loc= cmds.spaceLocator( n= '%s_loc' % each )
            legSpace= cmds.group( n='%s_space' % loc[0], em=0 )
            if str(loc[0]).startswith('L_'):
                self.L_legLoc.append(loc)
                self.L_legSpace.append(legSpace)
                cmds.parent( legSpace, self.L_legGrp )
            else :
                self.R_legLoc.append(loc)
                self.R_legSpace.append(legSpace)
                cmds.parent( legSpace, self.R_legGrp )
            cmds.setAttr( '%sShape.localScaleX' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleY' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleZ' % loc[0], 3 )
            cmds.setAttr( '%s.rx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % loc[0], l=1, k=0, cb=0 )
        for i, each in enumerate( self.L_legLoc ):
            MD= cmds.createNode( 'multiplyDivide', n= '%s_neg_MD01' % each[0] )
            cmds.setAttr( '%s.input2X' % MD, -1 )
            cmds.setAttr( '%s.input2Y' % MD, -1 )
            cmds.connectAttr( '%s.tx' % each[0], '%s.input1X' % MD )
            cmds.connectAttr( '%s.tx' % self.L_legSpace[i], '%s.input1Y' % MD )
            cmds.connectAttr( '%s.outputX' % MD, '%s.tx' % self.R_legLoc[i][0] )
            cmds.connectAttr( '%s.ty' % each[0], '%s.ty' % self.R_legLoc[i][0] )
            cmds.connectAttr( '%s.tz' % each[0], '%s.tz' % self.R_legLoc[i][0] )
            cmds.connectAttr( '%s.outputY' % MD, '%s.tx' % self.R_legSpace[i] )
            cmds.connectAttr( '%s.ty' % self.L_legSpace[i], '%s.ty' % self.R_legSpace[i])
            cmds.connectAttr( '%s.tz' % self.L_legSpace[i], '%s.tz' % self.R_legSpace[i] )
        # Create Proxy Leg Annotation
        L_hipAnnt= cmds.annotate( self.L_legLoc[1], tx= self.LegList[0] )
        cmds.setAttr( '%s.template' % L_hipAnnt, 1 )
        cmds.parent( L_hipAnnt, self.L_legLoc[0] ) 
        L_kneeAnnt= cmds.annotate( self.L_legLoc[2], tx= self.LegList[1] )
        cmds.setAttr( '%s.template' % L_kneeAnnt, 1 )
        cmds.parent( L_kneeAnnt, self.L_legLoc[1] )
        L_ankleAnnt= cmds.annotate( self.L_legLoc[3], tx= self.LegList[2] )
        cmds.setAttr( '%s.template' % L_ankleAnnt, 1 ) 
        cmds.parent( L_ankleAnnt, self.L_legLoc[2] )
        L_ballAnnt= cmds.annotate( self.L_legLoc[4], tx= self.LegList[3] )
        cmds.setAttr( '%s.template' % L_ballAnnt, 1 )
        cmds.parent( L_ballAnnt, self.L_legLoc[3] )
        L_toeAnnt= cmds.annotate( self.L_legLoc[8], tx= self.LegList[4] )
        cmds.setAttr( '%s.template' % L_toeAnnt, 1 )
        cmds.parent( L_toeAnnt, self.L_legLoc[4] )
        L_heel01Annt= cmds.annotate( self.L_legLoc[5] )
        cmds.setAttr( '%s.template' % L_heel01Annt, 1 )
        cmds.parent( L_heel01Annt, self.L_legLoc[2] )
        L_heel02Annt= cmds.annotate( self.L_legLoc[5], tx= self.LegList[5] )
        cmds.setAttr( '%s.template' % L_heel02Annt, 1 )
        cmds.parent( L_heel02Annt, self.L_legLoc[5] )
        L_sideL01Annt= cmds.annotate( self.L_legLoc[6] )
        cmds.setAttr( '%s.template' % L_sideL01Annt, 1 )
        cmds.parent( L_sideL01Annt, self.L_legLoc[3] )
        L_sideL02Annt= cmds.annotate( self.L_legLoc[6], tx= self.LegList[6] )
        cmds.setAttr( '%s.template' % L_sideL02Annt, 1 )
        cmds.parent( L_sideL02Annt, self.L_legLoc[6] )
        L_sideR01Annt= cmds.annotate( self.L_legLoc[7] )
        cmds.setAttr( '%s.template' % L_sideR01Annt, 1 )
        cmds.parent( L_sideR01Annt, self.L_legLoc[3] )
        L_sideR02Annt= cmds.annotate( self.L_legLoc[7], tx= self.LegList[7] )
        cmds.setAttr( '%s.template' % L_sideR02Annt, 1 )
        cmds.parent( L_sideR02Annt, self.L_legLoc[7] )
        L_toeTipAnnt= cmds.annotate( self.L_legLoc[8], tx= self.LegList[8] )
        cmds.setAttr( '%s.template' % L_toeTipAnnt, 1 )
        cmds.parent( L_toeTipAnnt, self.L_legLoc[8] )
        R_hipAnnt= cmds.annotate( self.R_legLoc[1], tx= self.LegList[0] )
        cmds.setAttr( '%s.template' % R_hipAnnt, 1 )
        cmds.parent( R_hipAnnt, self.R_legLoc[0] ) 
        R_kneeAnnt= cmds.annotate( self.R_legLoc[2], tx= self.LegList[1] )
        cmds.setAttr( '%s.template' % R_kneeAnnt, 1 )
        cmds.parent( R_kneeAnnt, self.R_legLoc[1] )
        R_ankleAnnt= cmds.annotate( self.R_legLoc[3], tx= self.LegList[2] )
        cmds.setAttr( '%s.template' % R_ankleAnnt, 1 ) 
        cmds.parent( R_ankleAnnt, self.R_legLoc[2] )
        R_ballAnnt= cmds.annotate( self.R_legLoc[4], tx= self.LegList[3] )
        cmds.setAttr( '%s.template' % R_ballAnnt, 1 )
        cmds.parent( R_ballAnnt, self.R_legLoc[3] )
        R_toeAnnt= cmds.annotate( self.R_legLoc[8], tx= self.LegList[4] )
        cmds.setAttr( '%s.template' % R_toeAnnt, 1 )
        cmds.parent( R_toeAnnt, self.R_legLoc[4] )
        R_heel01Annt= cmds.annotate( self.R_legLoc[5] )
        cmds.setAttr( '%s.template' % R_heel01Annt, 1 )
        cmds.parent( R_heel01Annt, self.R_legLoc[2] )
        R_heel02Annt= cmds.annotate( self.R_legLoc[5], tx= self.LegList[5] )
        cmds.setAttr( '%s.template' % R_heel02Annt, 1 )
        cmds.parent( R_heel02Annt, self.R_legLoc[5] )
        R_sideL01Annt= cmds.annotate( self.R_legLoc[6] )
        cmds.setAttr( '%s.template' % R_sideL01Annt, 1 )
        cmds.parent( R_sideL01Annt, self.R_legLoc[3] )
        R_sideL02Annt= cmds.annotate( self.R_legLoc[6], tx= self.LegList[6] )
        cmds.setAttr( '%s.template' % R_sideL02Annt, 1 )
        cmds.parent( R_sideL02Annt, self.R_legLoc[6] )
        R_sideR01Annt= cmds.annotate( self.R_legLoc[7] )
        cmds.setAttr( '%s.template' % R_sideR01Annt, 1 )
        cmds.parent( R_sideR01Annt, self.R_legLoc[3] )
        R_sideR02Annt= cmds.annotate( self.R_legLoc[7], tx= self.LegList[7] )
        cmds.setAttr( '%s.template' % R_sideR02Annt, 1 )
        cmds.parent( R_sideR02Annt, self.R_legLoc[7] )
        R_toeTipAnnt= cmds.annotate( self.R_legLoc[8], tx= self.LegList[8] )
        cmds.setAttr( '%s.template' % R_toeTipAnnt, 1 )
        cmds.parent( R_toeTipAnnt, self.R_legLoc[8] )
        # Proxy Bone Position
        cmds.xform( self.L_legSpace[0], t= [ 8.969,97.822,-2.366], a=1 )
        cmds.xform( self.L_legSpace[1], t= [ 13.494,54.601,-2.366], a=1 )
        cmds.xform( self.L_legSpace[2], t= [ 17.934,12.185,-6.603 ], a=1 )
        cmds.xform( self.L_legSpace[3], t= [ 20.205,4.179,8.082 ], a=1 )
        cmds.xform( self.L_legSpace[4], t= [ 21.809,3.983,15.173 ], a=1 )
        cmds.xform( self.L_legSpace[5], t= [ 17.238,0,-9.685 ], a=1 )
        cmds.xform( self.L_legSpace[6], t= [ 25.192,0,7.221 ], a=1 )
        cmds.xform( self.L_legSpace[7], t= [ 15.819,0,8.944 ], a=1 )
        cmds.xform( self.L_legSpace[8], t= [ 22.014,-0.342,16.29 ], a=1 )
        
        # Create Proxy Spine Bone Loc
        self.spineGrp= cmds.group( n= 'proxySpine_grp', em=1 )
        self.spineList= ['Pelvis', 'Spine',  'Chest']
        self.spineLoc= []
        self.spineSpace= []
        for each in self.spineList:
            loc= cmds.spaceLocator( n= '%s_loc' % each )
            spineSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.spineLoc.append( loc )
            self.spineSpace.append( spineSpace )
            cmds.parent( spineSpace, self.spineGrp )
            cmds.setAttr( '%sShape.localScaleX' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleY' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleZ' % loc[0], 3 )
            cmds.setAttr( '%s.rx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % loc[0], l=1, k=0, cb=0 )
        # Create Proxy Spine Annotation
        L_hipLocFake= cmds.spaceLocator( n= 'L_hipParentLoc' )
        R_hipLocFake= cmds.spaceLocator( n= 'R_hipParentLoc' )
        L_clvLocFake= cmds.spaceLocator( n= 'L_clvParentLoc' )
        R_clvLocFake= cmds.spaceLocator( n= 'R_clvParentLoc' )
        cmds.setAttr( '%s.template' % L_hipLocFake[0], 1 ) 
        cmds.setAttr( '%s.template' % R_hipLocFake[0], 1 ) 
        cmds.setAttr( '%s.template' % L_clvLocFake[0], 1 ) 
        cmds.setAttr( '%s.template' % R_clvLocFake[0], 1 ) 
        cmds.select( cl=1 )
        pelvisAnnt= cmds.annotate( self.spineLoc[1], tx= self.spineList[0] )
        cmds.setAttr( '%s.template' % pelvisAnnt, 1 )
        cmds.parent( pelvisAnnt, self.spineLoc[0] )
        pelvisAnnt1= cmds.annotate( L_hipLocFake )
        cmds.setAttr( '%s.template' % pelvisAnnt1, 1 )
        cmds.parent( pelvisAnnt1, self.spineLoc[0] ) 
        pelvisAnnt2= cmds.annotate( R_hipLocFake )
        cmds.setAttr( '%s.template' % pelvisAnnt2, 1 )
        cmds.parent( pelvisAnnt2, self.spineLoc[0] )
        spineAnnt= cmds.annotate( self.spineLoc[2], tx= self.spineList[1] )
        cmds.setAttr( '%s.template' % spineAnnt, 1 )
        cmds.parent( spineAnnt, self.spineLoc[1] )
        chestAnnt= cmds.annotate( self.spineLoc[2], tx= self.spineList[2] )
        cmds.setAttr( '%s.template' % chestAnnt, 1 ) 
        cmds.parent( chestAnnt, self.spineLoc[2] )
        chestAnnt1= cmds.annotate( L_clvLocFake )
        cmds.setAttr( '%s.template' % chestAnnt1, 1 ) 
        cmds.parent( chestAnnt1, self.spineLoc[2] )
        chestAnnt2= cmds.annotate( R_clvLocFake )
        cmds.setAttr( '%s.template' % chestAnnt2, 1 ) 
        cmds.parent( chestAnnt2, self.spineLoc[2] )
        # Proxy Bone Position
        cmds.xform( self.spineSpace[0], t= [ 0,102.333,0 ], a=1 )
        cmds.xform( self.spineSpace[1], t= [ 0,105.813,0 ], a=1 )
        cmds.xform( self.spineSpace[2], t= [ 0,131.458,0 ], a=1 )
        cmds.xform( L_hipLocFake, t= [ 8.969,97.822,-2.366], a=1 )
        cmds.xform( R_hipLocFake, t= [ -8.969,97.822,-2.366], a=1 )
        cmds.xform( L_clvLocFake, t= [ 5.241,142.186,-5.638], a=1 )
        cmds.xform( R_clvLocFake, t= [ -5.241,142.186,-5.638], a=1 )
        cmds.parent( L_hipLocFake, self.L_legLoc[0] )
        cmds.parent( R_hipLocFake, self.R_legLoc[0] )
        cmds.parent( L_clvLocFake, self.L_armLoc[0] )
        cmds.parent( R_clvLocFake, self.R_armLoc[0] )
        
        # Create Proxy Head Bone Loc
        self.headGrp= cmds.group( n= 'proxyhead_grp', em=1 )
        self.headList= ['neck', 'head', 'headEnd', 'L_eye01', 'L_eye02', 'R_eye01', 'R_eye02', 'jaw01', 'jawEnd', 'tongue01', 'tongue02', 'tongue03', 'tongueEnd', 'upTeeth01', 'upTeethEnd', 'dnTeeth01', 'dnTeethEnd' ]
        self.headLoc= []
        self.headSpace= []
        for each in self.headList:
            loc= cmds.spaceLocator( n= '%s_loc' % each )
            headSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.headLoc.append( loc )
            self.headSpace.append( headSpace )
            cmds.parent( headSpace, self.headGrp )
            cmds.setAttr( '%sShape.localScaleX' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleY' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleZ' % loc[0], 3 )
            cmds.setAttr( '%s.rx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % loc[0], l=1, k=0, cb=0 )
        # Create Proxy head Annotation
        neckLocFake= cmds.spaceLocator( n= 'neckLocFake' )
        cmds.setAttr( '%s.template' % neckLocFake[0], 1 ) 
        cmds.select( cl=1 )
        neckAnnt= cmds.annotate( self.headLoc[1], tx= self.headList[0] )
        cmds.setAttr( '%s.template' % neckAnnt, 1 )
        cmds.parent( neckAnnt, self.headLoc[0] )
        neckAnnt1= cmds.annotate( neckLocFake )
        cmds.setAttr( '%s.template' % neckAnnt1, 1 )
        cmds.parent( neckAnnt1, self.headLoc[0] ) 
        headAnnt= cmds.annotate( self.headLoc[2], tx= self.headList[1] )
        cmds.setAttr( '%s.template' % headAnnt, 1 )
        cmds.parent( headAnnt, self.headLoc[1] )
        headEndAnnt= cmds.annotate( self.headLoc[2],tx= self.headList[2] )
        cmds.setAttr( '%s.template' % headEndAnnt, 1 )
        cmds.parent( headEndAnnt, self.headLoc[2] )
        lEyeAnnt= cmds.annotate( self.headLoc[4], tx= self.headList[3] )
        cmds.setAttr( '%s.template' % lEyeAnnt, 1 ) 
        cmds.parent( lEyeAnnt, self.headLoc[3] )
        lEyeEndAnnt= cmds.annotate( self.headLoc[4], tx= self.headList[4] )
        cmds.setAttr( '%s.template' % lEyeEndAnnt, 1 ) 
        cmds.parent( lEyeEndAnnt, self.headLoc[4] )
        rEyeAnnt= cmds.annotate( self.headLoc[6], tx= self.headList[5] )
        cmds.setAttr( '%s.template' % rEyeAnnt, 1 ) 
        cmds.parent( rEyeAnnt, self.headLoc[5] )
        rEyeEndAnnt= cmds.annotate( self.headLoc[6], tx= self.headList[6] )
        cmds.setAttr( '%s.template' % rEyeEndAnnt, 1 ) 
        cmds.parent( rEyeEndAnnt, self.headLoc[6] )
        jawAnnt= cmds.annotate( self.headLoc[8], tx= self.headList[7] )
        cmds.setAttr( '%s.template' % jawAnnt, 1 ) 
        cmds.parent( jawAnnt, self.headLoc[7] )
        jawEndAnnt= cmds.annotate( self.headLoc[8], tx= self.headList[8] )
        cmds.setAttr( '%s.template' % jawEndAnnt, 1 ) 
        cmds.parent( jawEndAnnt, self.headLoc[8] )
        tongue01Annt= cmds.annotate( self.headLoc[10], tx= self.headList[9] )
        cmds.setAttr( '%s.template' % tongue01Annt, 1 ) 
        cmds.parent( tongue01Annt, self.headLoc[9] )
        tongue02Annt= cmds.annotate( self.headLoc[11], tx= self.headList[10] )
        cmds.setAttr( '%s.template' % tongue02Annt, 1 ) 
        cmds.parent( tongue02Annt, self.headLoc[10] )
        tongue03Annt= cmds.annotate( self.headLoc[12], tx= self.headList[11] )
        cmds.setAttr( '%s.template' % tongue03Annt, 1 ) 
        cmds.parent( tongue03Annt, self.headLoc[11] )
        tongueEndAnnt= cmds.annotate( self.headLoc[12], tx= self.headList[12] )
        cmds.setAttr( '%s.template' % tongueEndAnnt, 1 ) 
        cmds.parent( tongueEndAnnt, self.headLoc[12] )
        upTeeth01Annt= cmds.annotate( self.headLoc[14], tx= self.headList[13] )
        cmds.setAttr( '%s.template' % upTeeth01Annt, 1 ) 
        cmds.parent( upTeeth01Annt, self.headLoc[13] )
        upTeethEndAnnt= cmds.annotate( self.headLoc[14], tx= self.headList[14] )
        cmds.setAttr( '%s.template' % upTeethEndAnnt, 1 ) 
        cmds.parent( upTeethEndAnnt, self.headLoc[14] )
        dnTeeth01Annt= cmds.annotate( self.headLoc[16], tx= self.headList[15] )
        cmds.setAttr( '%s.template' % dnTeeth01Annt, 1 ) 
        cmds.parent( dnTeeth01Annt, self.headLoc[15] )
        dnTeethEndAnnt= cmds.annotate( self.headLoc[16], tx= self.headList[16] )
        cmds.setAttr( '%s.template' % dnTeethEndAnnt, 1 ) 
        cmds.parent( dnTeethEndAnnt, self.headLoc[16] )
        # Setup Proxy Eyes
        l_eyes= [ self.headLoc[3], self.headLoc[4] ]
        r_eyes= [ self.headLoc[5], self.headLoc[6] ]
        l_eyeSpace= [ self.headSpace[3], self.headSpace[4] ]
        r_eyeSpace= [ self.headSpace[5], self.headSpace[6] ]
        for i, each in enumerate(l_eyes):
            MD= cmds.createNode( 'multiplyDivide', n= '%s_neg_MD01' % each[0] )
            cmds.setAttr( '%s.input2X' % MD, -1 )
            cmds.setAttr( '%s.input2Y' % MD, -1 )
            cmds.connectAttr( '%s.tx' % each[0], '%s.input1X' % MD )
            cmds.connectAttr( '%s.tx' % l_eyeSpace[i], '%s.input1Y' % MD )
            cmds.connectAttr( '%s.outputX' % MD, '%s.tx' % r_eyes[i][0] )
            cmds.connectAttr( '%s.ty' % each[0], '%s.ty' % r_eyes[i][0] )
            cmds.connectAttr( '%s.tz' % each[0], '%s.tz' % r_eyes[i][0] )
            cmds.connectAttr( '%s.outputY' % MD, '%s.tx' % r_eyeSpace[i] )
            cmds.connectAttr( '%s.ty' % l_eyeSpace[i], '%s.ty' % r_eyeSpace[i] )
            cmds.connectAttr( '%s.tz' % l_eyeSpace[i], '%s.tz' % r_eyeSpace[i] )
        # Proxy Bone Position
        cmds.xform( self.headSpace[0], t= [ 0,150.475,-4.663 ], a=1 )
        cmds.xform( neckLocFake, t= [ 0,131.458,0  ], a=1 )
        cmds.xform( self.headSpace[1], t= [ 0,158.642,-1.492 ], a=1 )
        cmds.xform( self.headSpace[2], t= [ 0,174.112,-1.492 ], a=1 )
        cmds.xform( self.headSpace[3], t= [ 2.889,164.238,4.629 ], a=1 )
        cmds.xform( self.headSpace[4], t= [ 2.889,164.238,6.387 ], a=1 )
        cmds.xform( self.headSpace[7], t= [ 0,158.216,0.138 ], a=1 )
        cmds.xform( self.headSpace[8], t= [ 0,155.8478,7.889 ], a=1 )
        cmds.xform( self.headSpace[9], t= [ 0,157.953,1.498 ], a=1 )
        cmds.xform( self.headSpace[10], t= [ 0,158.037,3.564 ], a=1 )
        cmds.xform( self.headSpace[11], t= [ 0,157.779,5.609 ], a=1 )
        cmds.xform( self.headSpace[12], t= [ 0,157.158,7.581 ], a=1 )
        cmds.xform( self.headSpace[13], t= [ 0,159.276,1.261 ], a=1 )
        cmds.xform( self.headSpace[14], t= [ 0,157.95,8.676 ], a=1 )
        cmds.xform( self.headSpace[15], t= [ 0,157.941,1.038 ], a=1 )
        cmds.xform( self.headSpace[16], t= [ 0,156.767,7.874 ], a=1 )
        cmds.parent( neckLocFake, self.spineLoc[2] )

        # Create Proxy L_finger Bone Loc
        self.L_fingerGrp= cmds.group( n= 'L_proxy_finger_grp', em=1 )
        self.ThumbList= ['thumb01', 'thumb02', 'thumb03', 'thumbEnd' ]
        self.indexList= [ 'index01', 'index02', 'index03', 'index04', 'indexEnd' ]
        self.midList= [ 'mid01', 'mid02', 'mid03', 'mid04', 'midEnd' ]
        self.pinkList= [ 'pink01', 'pink02', 'pink03', 'pink04', 'pinkEnd' ]
        self.ringList= [ 'ring01', 'ring02', 'ring03', 'ring04', 'ringEnd' ]
        self.L_fingerLoc= []
        self.L_fingerSpace= []
        thumbAim= ['02','03','End','End']
        L_fingersAim=[ '02','03','04','End','End']
        # Thumb Loc % Annt
        for each in self.ThumbList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('l', each) )
            L_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.L_fingerLoc.append( loc )
            self.L_fingerSpace.append( L_fingerSpace )
            cmds.parent( L_fingerSpace, self.L_fingerGrp )
        for i,each in enumerate(self.ThumbList):
            thumbAnnt= cmds.annotate( '%s%s_loc' % ('l_thumb', thumbAim[i]), tx= 'L_%s' % each )
            cmds.setAttr( '%s.template' % thumbAnnt, 1 )
            cmds.parent( thumbAnnt, '%s_%s_loc' % ('l', each) )        
        # Index Loc % Annt    
        for each in self.indexList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('l', each) )
            L_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.L_fingerLoc.append( loc )
            self.L_fingerSpace.append( L_fingerSpace )
            cmds.parent( L_fingerSpace, self.L_fingerGrp )
        for i,each in enumerate(self.indexList):
            indexAnnt= cmds.annotate( '%s%s_loc' % ('l_index', L_fingersAim[i]), tx= 'L_%s' % each )
            cmds.setAttr( '%s.template' % indexAnnt, 1 )
            cmds.parent( indexAnnt, '%s_%s_loc' % ('l', each) ) 
        # Mid Loc % Annt    
        for each in self.midList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('l', each) )
            L_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.L_fingerLoc.append( loc )
            self.L_fingerSpace.append( L_fingerSpace )
            cmds.parent( L_fingerSpace, self.L_fingerGrp )
        for i,each in enumerate(self.midList):
            midAnnt= cmds.annotate( '%s%s_loc' % ('l_mid', L_fingersAim[i]), tx= 'L_%s' % each )
            cmds.setAttr( '%s.template' % midAnnt, 1 )
            cmds.parent( midAnnt, '%s_%s_loc' % ('l', each) )   
        # Pink Loc % Annt    
        for each in self.pinkList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('l', each) )
            L_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.L_fingerLoc.append( loc )
            self.L_fingerSpace.append( L_fingerSpace )
            cmds.parent( L_fingerSpace, self.L_fingerGrp )
        for i,each in enumerate(self.pinkList):
            pinkAnnt= cmds.annotate( '%s%s_loc' % ('l_pink', L_fingersAim[i]), tx= 'L_%s' % each )
            cmds.setAttr( '%s.template' % pinkAnnt, 1 )
            cmds.parent( pinkAnnt, '%s_%s_loc' % ('l', each) )     
        # Ring Loc % Annt    
        for each in self.ringList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('l', each) )
            L_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.L_fingerLoc.append( loc )
            self.L_fingerSpace.append( L_fingerSpace )
            cmds.parent( L_fingerSpace, self.L_fingerGrp )
        for i,each in enumerate(self.ringList):
            ringAnnt= cmds.annotate( '%s%s_loc' % ('l_ring', L_fingersAim[i]), tx= 'L_%s' % each )
            cmds.setAttr( '%s.template' % ringAnnt, 1 )
            cmds.parent( ringAnnt, '%s_%s_loc' % ('l', each) )                          
        for each in self.L_fingerLoc:
            cmds.setAttr( '%sShape.localScaleX' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleY' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleZ' % loc[0], 3 )
            cmds.setAttr( '%s.rx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % loc[0], l=1, k=0, cb=0 )
            
        # Proxy Bone Position
        cmds.xform( self.L_fingerSpace[0], t= [ 49.526,102.943,-2.4 ], a=1 )
        cmds.xform( self.L_fingerSpace[1], t= [ 49.744,101.237,0.567 ], a=1 )
        cmds.xform( self.L_fingerSpace[2], t= [ 49.7,98.276,2.131 ], a=1 )
        cmds.xform( self.L_fingerSpace[3], t= [ 49.602,95.292,3.306 ], a=1 )
        cmds.xform( self.L_fingerSpace[4], t= [ 51.021,104.366,-3.978 ], a=1 )
        cmds.xform( self.L_fingerSpace[5], t= [ 53.559,100.075,-2.685], a=1 )
        cmds.xform( self.L_fingerSpace[6], t= [ 55.767,96.343,-1.56 ], a=1 )
        cmds.xform( self.L_fingerSpace[7], t= [ 56.813,93.969,-0.702 ], a=1 )
        cmds.xform( self.L_fingerSpace[8], t= [ 57.512,91.686,0.115 ], a=1 )
        cmds.xform( self.L_fingerSpace[9], t= [ 51.291,103.495,-5.209 ], a=1 )
        cmds.xform( self.L_fingerSpace[10], t= [ 53.785,99.003,-4.856 ], a=1 )
        cmds.xform( self.L_fingerSpace[11], t= [ 55.954,95.096,-4.549], a=1 )
        cmds.xform( self.L_fingerSpace[12], t= [ 57.045,92.62,-4.167 ], a=1 )
        cmds.xform( self.L_fingerSpace[13], t= [ 57.765,90.217,-3.89 ], a=1 )
        cmds.xform( self.L_fingerSpace[14], t= [ 51.472,103.312,-6.947 ], a=1 )
        cmds.xform( self.L_fingerSpace[15], t= [ 53.541,98.666,-7.293 ], a=1 )
        cmds.xform( self.L_fingerSpace[16], t= [ 54.724,94.662,-7.311 ], a=1 )
        cmds.xform( self.L_fingerSpace[17], t= [ 55.189,92.208,-7.151 ], a=1 )
        cmds.xform( self.L_fingerSpace[18], t= [ 55.396,89.935,-6.985 ], a=1 )
        cmds.xform( self.L_fingerSpace[19], t= [ 51.013,103.367,-8.187 ], a=1 )
        cmds.xform( self.L_fingerSpace[20], t= [ 52.385,98.469,-9.055  ], a=1 )
        cmds.xform( self.L_fingerSpace[21], t= [ 52.891,95.205,-9.316 ], a=1 )
        cmds.xform( self.L_fingerSpace[22], t= [ 53.123,93.533,-9.422 ], a=1 )
        cmds.xform( self.L_fingerSpace[23], t= [ 53.22,91.5,-9.413 ], a=1 )

        # Create Proxy R_finger Bone Loc
        self.R_fingerGrp= cmds.group( n= 'R_proxy_finger_grp', em=1 )
        self.ThumbList= ['thumb01', 'thumb02', 'thumb03', 'thumbEnd' ]
        self.indexList= [ 'index01', 'index02', 'index03', 'index04', 'indexEnd' ]
        self.midList= [ 'mid01', 'mid02', 'mid03', 'mid04', 'midEnd' ]
        self.pinkList= [ 'pink01', 'pink02', 'pink03', 'pink04', 'pinkEnd' ]
        self.ringList= [ 'ring01', 'ring02', 'ring03', 'ring04', 'ringEnd' ]
        self.R_fingerLoc= []
        self.R_fingerSpace= []
        thumbAim= ['02','03','End','End']
        R_fingersAim=[ '02','03','04','End','End']
        # Thumb Loc % Annt
        for each in self.ThumbList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('r', each) )
            R_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.R_fingerLoc.append( loc )
            self.R_fingerSpace.append( R_fingerSpace )
            cmds.parent( R_fingerSpace, self.R_fingerGrp )
        for i,each in enumerate(self.ThumbList):
            thumbAnnt= cmds.annotate( '%s%s_loc' % ('r_thumb', thumbAim[i]), tx= 'R_%s' % each )
            cmds.setAttr( '%s.template' % thumbAnnt, 1 )
            cmds.parent( thumbAnnt, '%s_%s_loc' % ('r', each) )        
        # Index Loc % Annt    
        for each in self.indexList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('r', each) )
            R_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.R_fingerLoc.append( loc )
            self.R_fingerSpace.append( R_fingerSpace )
            cmds.parent( R_fingerSpace, self.R_fingerGrp )
        for i,each in enumerate(self.indexList):
            indexAnnt= cmds.annotate( '%s%s_loc' % ('r_index', R_fingersAim[i]), tx= 'R_%s' % each )
            cmds.setAttr( '%s.template' % indexAnnt, 1 )
            cmds.parent( indexAnnt, '%s_%s_loc' % ('r', each) ) 
        # Mid Loc % Annt    
        for each in self.midList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('r', each) )
            R_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.R_fingerLoc.append( loc )
            self.R_fingerSpace.append( R_fingerSpace )
            cmds.parent( R_fingerSpace, self.R_fingerGrp )
        for i,each in enumerate(self.midList):
            midAnnt= cmds.annotate( '%s%s_loc' % ('r_mid', R_fingersAim[i]), tx= 'R_%s' % each )
            cmds.setAttr( '%s.template' % midAnnt, 1 )
            cmds.parent( midAnnt, '%s_%s_loc' % ('r', each) )   
        # Pink Loc % Annt    
        for each in self.pinkList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('r', each) )
            R_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.R_fingerLoc.append( loc )
            self.R_fingerSpace.append( R_fingerSpace )
            cmds.parent( R_fingerSpace, self.R_fingerGrp )
        for i,each in enumerate(self.pinkList):
            pinkAnnt= cmds.annotate( '%s%s_loc' % ('r_pink', R_fingersAim[i]), tx= 'R_%s' % each )
            cmds.setAttr( '%s.template' % pinkAnnt, 1 )
            cmds.parent( pinkAnnt, '%s_%s_loc' % ('r', each) )     
        # Ring Loc % Annt    
        for each in self.ringList:
            loc= cmds.spaceLocator( n= '%s_%s_loc' % ('r', each) )
            R_fingerSpace= cmds.group( n='%s_loc' % loc[0], em=0 )
            self.R_fingerLoc.append( loc )
            self.R_fingerSpace.append( R_fingerSpace )
            cmds.parent( R_fingerSpace, self.R_fingerGrp )
        for i,each in enumerate(self.ringList):
            ringAnnt= cmds.annotate( '%s%s_loc' % ('r_ring', R_fingersAim[i]), tx= 'R_%s' % each )
            cmds.setAttr( '%s.template' % ringAnnt, 1 )
            cmds.parent( ringAnnt, '%s_%s_loc' % ('r', each) )                          
        for each in self.R_fingerLoc:
            cmds.setAttr( '%sShape.localScaleX' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleY' % loc[0], 3 )
            cmds.setAttr( '%sShape.localScaleZ' % loc[0], 3 )
            cmds.setAttr( '%s.rx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % loc[0], l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % loc[0], l=1, k=0, cb=0 )
            
        # Proxy Bone Position
        for i, each in enumerate( self.L_fingerLoc ):
            MD= cmds.createNode( 'multiplyDivide', n= '%s_neg_MD01' % each[0] )
            cmds.setAttr( '%s.input2X' % MD, -1 )
            cmds.setAttr( '%s.input2Y' % MD, -1 )
            cmds.connectAttr( '%s.tx' % each[0], '%s.input1X' % MD )
            cmds.connectAttr( '%s.tx' % self.L_fingerSpace[i], '%s.input1Y' % MD )
            cmds.connectAttr( '%s.outputX' % MD, '%s.tx' % self.R_fingerLoc[i][0] )
            cmds.connectAttr( '%s.ty' % each[0], '%s.ty' % self.R_fingerLoc[i][0] )
            cmds.connectAttr( '%s.tz' % each[0], '%s.tz' % self.R_fingerLoc[i][0] )
            cmds.connectAttr( '%s.outputY' % MD, '%s.tx' % self.R_fingerSpace[i] )
            cmds.connectAttr( '%s.ty' % self.L_fingerSpace[i], '%s.ty' % self.R_fingerSpace[i])
            cmds.connectAttr( '%s.tz' % self.L_fingerSpace[i], '%s.tz' % self.R_fingerSpace[i] ) 
        
if __name__ == '__main__' :
    abc= ProxyBone_Cl()
