import maya.cmds as cmds

class proxyBipedJoint_Cl():
    def __init__(self, jntRad, jntLabel ):
        
    # List of proxy joint setup function
        self.proxyHead_Fn
        self.proxyEyes_Fn
        self.proxyJaw_Fn
        self.proxyTongue_Fn
        self.proxyTeeths_Fn
        self.proxyTorso_Fn
        self.proxyArm_Fn
        self.proxyFingers_Fn
        self.proxyLeg_Fn
        '''self.extraJnt_Fn'''
        self.jntRad= jntRad
        self.jntLabel= jntLabel
        self.worldLoc= cmds.spaceLocator( n="skeleton01" )[0]
        cmds.setAttr( "%sShape.localScaleX" % self.worldLoc, 3 )
        cmds.setAttr( "%sShape.localScaleY" % self.worldLoc, 3 )
        cmds.setAttr( "%sShape.localScaleZ" % self.worldLoc, 3 )
        cmds.setAttr( "%sShape.overrideEnabled"  % self.worldLoc,1 )
        cmds.setAttr( '%sShape.overrideColor' % self.worldLoc, 13 )
    
    # Proxy Head Function
    def proxyHead_Fn(self):
        # Create Joint Chain
        cmds.select( cl=1 )
        self.neckJnt= cmds.joint( n="neck_Jnt01", rad=self.jntRad, p=[0,158,-8], o=[11,0,0] )
        cmds.setAttr( "%s.side" % self.neckJnt, 0 )
        cmds.setAttr( "%s.type" % self.neckJnt, 7 )
        self.headJnt01= cmds.joint( n= "head_Jnt01", rad=self.jntRad, p=[0,169.779,-5.71], o=[-5,0,0] )
        cmds.setAttr( "%s.side" % self.headJnt01, 0 )
        cmds.setAttr( "%s.type" % self.headJnt01, 8 )
        headEnd= cmds.joint( n= "head_End01", rad=self.jntRad, p=[0,185.6916,-4.038], o=[0,0,0] )
        cmds.setAttr( "%s.side" % headEnd, 0 )
        cmds.setAttr( "%s.type" % headEnd, 18 )
        cmds.setAttr( "%s.otherType" % headEnd, "HeadEnd", type= "string" )
        cmds.select( cl=1 )
        self.headJnt02= cmds.duplicate( headEnd, n= str(headEnd).replace( "End01", "Jnt02" ))[0]
        cmds.setAttr( "%s.side" % self.headJnt02, 0 )
        cmds.setAttr( "%s.type" % self.headJnt02, 18 )
        cmds.setAttr( "%s.otherType" % self.headJnt02, "Head02", type= "string" )
        self.headEndTY= cmds.getAttr( "%s.ty" % headEnd )
        cmds.setAttr( "%s.ty" % self.headJnt02, self.headEndTY/2 )
        cmds.parent( headEnd, self.headJnt02 )
        cmds.parent( self.neckJnt, self.worldLoc )
        cmds.select( cl=1 )
        proxyHeadJnt= [ self.neckJnt, self.headJnt01, self.headJnt02, headEnd ]
        proxyHeadEnd= [ self.headJnt02, headEnd ]
        for each in proxyHeadJnt:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
        for each in proxyHeadEnd:
            cmds.setAttr( "%s.tx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.tz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.ry" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rz" % each, l=1, ch=1 )
        # Collecting Joints Default Value
        self.headDVdict= { "neck":[(0,158,-8),(11,0,0)], "head01":[(0,12,0),(-5,0,0)], "head02":[(0,8,0),(0,0,0)], "headEnd":[(0,8,0),(0,0,0)] }
                                                                                                                                                
    # Proxy Eyes Function    
    def proxyEyes_Fn(self, head01, head02):
        self.head01= head01
        self.head02= head02
        # Left Eye
        self.lEyeJnt= cmds.joint( n="L_eye_Jnt01", rad=self.jntRad, p=[3,174.8055,3.86755], o=[0,5,0] )
        cmds.setAttr( "%s.side" % self.lEyeJnt, 1 )
        cmds.setAttr( "%s.type" % self.lEyeJnt, 18 )
        cmds.setAttr( "%s.otherType" % self.lEyeJnt, "Eye", type= "string" )
        self.lEyelidJnt= cmds.joint( n="L_eyelid_Jnt01", rad=self.jntRad*0.5, p=[3,174.805,3.8675], o=[0,5,0] )
        cmds.setAttr( "%s.side" % self.lEyelidJnt, 1 )
        cmds.setAttr( "%s.type" % self.lEyelidJnt, 18 )
        cmds.setAttr( "%s.otherType" % self.lEyelidJnt, "Eyelid", type= "string" )
        lEyeEnd= cmds.duplicate( self.lEyeJnt, n=str(self.lEyeJnt).replace( "Jnt", "End" ), rc=1 )[0]
        duplicatedChild= cmds.listRelatives( lEyeEnd, c=1 )
        cmds.delete( duplicatedChild )
        cmds.setAttr( "%s.side" % lEyeEnd, 1 )
        cmds.setAttr( "%s.type" % lEyeEnd, 18 )
        cmds.setAttr( "%s.otherType" % lEyeEnd, "EyeEnd", type= "string" )
        cmds.parent( lEyeEnd, self.lEyeJnt )
        cmds.setAttr( "%s.tz" % lEyeEnd, 2 )
        cmds.select(cl=1)
        # Right Eye
        self.rEyeJnt= cmds.joint( n="R_eye_Jnt01", rad=self.jntRad, p=[-3,174.8055,3.86755], o=[0,5,0] )
        cmds.setAttr( "%s.side" % self.rEyeJnt, 2 )
        cmds.setAttr( "%s.type" % self.rEyeJnt, 18 )
        cmds.setAttr( "%s.otherType" % self.rEyeJnt, "Eye", type= "string" )
        self.rEyelidJnt= cmds.joint( n="R_eyelid_Jnt01", rad=self.jntRad*0.5, p=[-3,174.805,3.8675], o=[0,5,0] )
        cmds.setAttr( "%s.side" % self.rEyelidJnt, 2 )
        cmds.setAttr( "%s.type" % self.rEyelidJnt, 18 )
        cmds.setAttr( "%s.otherType" % self.rEyelidJnt, "Eyelid", type= "string" )
        rEyeEnd= cmds.duplicate( self.rEyeJnt, n=str(self.rEyeJnt).replace( "Jnt", "End" ), rc=1 )[0]
        duplicatedChild= cmds.listRelatives( rEyeEnd, c=1 )
        cmds.delete( duplicatedChild )
        cmds.setAttr( "%s.side" % rEyeEnd, 2 )
        cmds.setAttr( "%s.type" % rEyeEnd, 18 )
        cmds.setAttr( "%s.otherType" % rEyeEnd, "EyeEnd", type= "string" )
        cmds.parent( rEyeEnd, self.rEyeJnt )
        cmds.setAttr( "%s.tz" % rEyeEnd, 2 )
        if cmds.objExists( self.head02 ) == True:
            cmds.parent( self.lEyeJnt, self.rEyeJnt, self.head02 )
            cmds.select( cl=1 )
        proxyFaceJnt= [ self.lEyeJnt, self.lEyelidJnt, self.rEyeJnt, self.rEyelidJnt, lEyeEnd, rEyeEnd ]
        proxyFaceEnd= [ self.lEyelidJnt, self.rEyelidJnt, lEyeEnd, rEyeEnd ]
        for each in proxyFaceJnt:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
        for each in proxyFaceEnd:
            cmds.setAttr( "%s.tx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.ty" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.ry" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rz" % each, l=1, ch=1 )
        cmds.setAttr( "%s.jointOrient" % self.lEyeJnt, 0,5,0 )
        cmds.setAttr( "%s.jointOrient" % self.rEyeJnt, 0,-5,0 )
        cmds.setAttr( "%s.jointOrient" % self.lEyelidJnt, 0,0,0 )
        cmds.setAttr( "%s.jointOrient" % self.rEyelidJnt, 0,0,0 )
        cmds.select( cl=1 )
        # Collecting Joints Default Value
        self.eyesDVdict= { "lEye01":[(3,-2,9), (0,5,0)], "lEyelid":[(0,0,0), (0,0,0)], "lEyeEnd":[(0,0,2), (0,0,0)], "rEye01":[(-3,-2,9), (0,5,0)], "rEyelid":[(0,0,0), (0,0,0)], "rEyeEnd":[(0,0,2), (0,0,0)] }

    # Proxy Jaw Function
    def proxyJaw_Fn(self, head01):
        self.head01= head01
        # Create Joint Chain
        cmds.select(cl=1)
        self.jawJnt= cmds.joint( n="jaw_Jnt01", rad=self.jntRad, p=[0,171.009,-3.067], o=[21,0,0] )
        cmds.setAttr( "%s.side" % self.jawJnt, 0 )
        cmds.setAttr( "%s.type" % self.jawJnt, 18 )
        cmds.setAttr( "%s.otherType" % self.jawJnt, "Jaw", type= "string" )
        jawEnd= cmds.duplicate( self.jawJnt, n=str(self.jawJnt).replace( "Jnt", "End" ) )[0]
        cmds.parent( jawEnd, self.jawJnt )
        cmds.setAttr( "%s.tz" % jawEnd, 10 )
        cmds.setAttr( "%s.side" % jawEnd, 0 )
        cmds.setAttr( "%s.type" % jawEnd, 18 )
        cmds.setAttr( "%s.otherType" % jawEnd, "JawEnd", type= "string" )
        if cmds.objExists( self.head01 ) == True:
            cmds.parent( self.jawJnt, self.head01 )
            cmds.select( cl=1 )
        proxyFaceJnt= [ self.jawJnt, jawEnd ]
        proxyFaceEnd= [ jawEnd ]
        for each in proxyFaceJnt:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
        for each in proxyFaceEnd:
            cmds.setAttr( "%s.tx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.ty" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.ry" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rz" % each, l=1, ch=1 )
        cmds.select( cl=1 )
        # Collecting Joints Default Value
        self.jawDVdict= { "jaw":[(0,1.5,2.5), (15,0,0)], "jawEnd":[(0,0,10), (0,0,0)] }
    
    # Proxy Tongue Function
    def proxyTongue_Fn(self, jaw):
        self.jaw= jaw
        self.tongueJnt=[]
        cmds.select(cl=1)
        jntA= cmds.joint( n="tongue_Jnt01", rad=self.jntRad, p=[0,166.916,-3.567] )
        self.tongueJnt.append( jntA )
        
        for each in range(2, 6):
            cmds.select(cl=1)
            jnt= cmds.joint( n= "tongue_Jnt0%s" % each, rad=self.jntRad, p=[0,166.916,-3.567] )
            self.tongueJnt.append( jnt )
            cmds.select(cl=1)
        
        for each in reversed(range(1, 5)):
            n= each
            cmds.parent( self.tongueJnt[n], self.tongueJnt[(n-1)] )
            n= n-1
            cmds.setAttr( "%s.translate" % self.tongueJnt[each], 0,0,2 )
            cmds.setAttr( "%s.jointOrientX" % self.tongueJnt[each], 15 )
            cmds.setAttr( "%s.side" % self.tongueJnt[each], 0 )
            cmds.setAttr( "%s.type" % self.tongueJnt[each], 18 )
            cmds.setAttr( "%s.otherType" % self.tongueJnt[each], "tongue0%s" % each, type= "string" )
            cmds.setAttr( "%s.sx" % self.tongueJnt[each], l=1, ch=1 )
            cmds.setAttr( "%s.sy" % self.tongueJnt[each], l=1, ch=1 )
            cmds.setAttr( "%s.sz" % self.tongueJnt[each], l=1, ch=1 )
            cmds.setAttr( "%s.v" % self.tongueJnt[each], l=1, ch=1 )
        cmds.setAttr( "%s.jointOrientX" % self.tongueJnt[0], -29 )
        cmds.setAttr( "%s.tx" % self.tongueJnt[-1], l=1, ch=1 )
        cmds.setAttr( "%s.ty" % self.tongueJnt[-1], l=1, ch=1 )
        cmds.setAttr( "%s.rx" % self.tongueJnt[-1], l=1, ch=1 )
        cmds.setAttr( "%s.ry" % self.tongueJnt[-1], l=1, ch=1 )
        cmds.setAttr( "%s.rz" % self.tongueJnt[-1], l=1, ch=1 )
        if cmds.objExists(self.jaw):
            cmds.parent( self.tongueJnt[0], self.jaw )
        else:
            pass
        cmds.select(cl=1)
        # Collecting Joints Default Value
        self.tongueDVdict= { "tongue01":[(0,-4,1), (-50,0,0)], "tongueElse":[(0,0,2), (15,0,0)] }
        
    # Proxy Teeths Function
    def proxyTeeths_Fn(self, head01, jaw):
        self.head01= head01
        self.jaw= jaw
        self.upTeeth= cmds.joint( n="upTeeth_Jnt01", rad=self.jntRad, p=[0,169.833,3.345], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.upTeeth, 0 )
        cmds.setAttr( "%s.type" % self.upTeeth, 18 )
        cmds.setAttr( "%s.otherType" % self.upTeeth, "upTeeth", type= "string" )
        self.dnTeeth= cmds.joint( n="dnTeeth_Jnt01", rad=self.jntRad, p=[0,166.633,2.751], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.dnTeeth, 0 )
        cmds.setAttr( "%s.type" % self.dnTeeth, 18 )
        cmds.setAttr( "%s.otherType" % self.dnTeeth, "dnTeeth", type= "string" )
        proxyTeeth= [ self.upTeeth, self.dnTeeth ]
        for each in proxyTeeth:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
        if cmds.objExists(self.jaw):
            cmds.parent( self.dnTeeth, self.jaw )
        else:
            pass
        if cmds.objExists(self.head01):
            cmds.parent( self.upTeeth, self.head01 )
        else:
            pass
        cmds.select(cl=1)
        # Collecting Joints Default Value
        self.teethDVdict= { "upTeeth":[(0,1,9), (0,0,0)], "jawEnd":[(0,-2,7), (0,0,0)] }
        
    # Proxy Torso Function
    def proxyTorso_Fn(self):
        cmds.select(cl=1)
        self.pelvis= cmds.joint( n="pelvis_Jnt01", rad=self.jntRad, p=[0,110,-1.3], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.pelvis, 0 )
        cmds.setAttr( "%s.type" % self.pelvis, 18 )
        cmds.setAttr( "%s.otherType" % self.pelvis, "Pelvis", type= "string" )
        cmds.select(cl=1)
        self.spine= cmds.joint( n="spine_Jnt01", rad=self.jntRad, p=[0,125,-1.3], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.pelvis, 0 )
        cmds.setAttr( "%s.type" % self.pelvis, 6 )
        cmds.select(cl=1)
        self.chest= cmds.joint( n="chest_Jnt01", rad=self.jntRad, p=[0,140,-1.3], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.pelvis, 0 )
        cmds.setAttr( "%s.type" % self.pelvis, 18 )
        cmds.setAttr( "%s.otherType" % self.chest, "Chest", type= "string" )
        cmds.select(cl=1)
        proxyTorso= [ self.pelvis, self.spine, self.chest ]
        for each in proxyTorso:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
            cmds.parent( each, self.worldLoc )
            cmds.select(cl=1)
        # Collecting Joints Default Value
        self.torsoDVdict= { "pelvis":[(0,110,-1.3), (0,0,0)], "spine":[(0,125,-1.3), (0,0,0)], "chest":[(0,140,-1.3),(0,0,0)] }
    
    # Proxy Arm Function
    def proxyArm_Fn(self):
        cmds.select(cl=1)
        self.clavicle= cmds.joint( n="L_clavicle_Jnt01", rad=self.jntRad, p=[3,150,0], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.clavicle, 1 )
        cmds.setAttr( "%s.type" % self.clavicle, 9 )
        cmds.select(cl=1)
        self.shoulder= cmds.joint( n="L_shoulder_Jnt01", rad=self.jntRad, p=[23,145,-5], o=[0,2,-35] )
        cmds.setAttr( "%s.side" % self.shoulder, 1 )
        cmds.setAttr( "%s.type" % self.shoulder, 10 )
        cmds.select(cl=1)
        self.elbow= cmds.joint( n="L_elbow_Jnt01", rad=self.jntRad, p=[43.46625,130.66937,-5.872], o=[0,-3,-35] )
        cmds.setAttr( "%s.side" % self.elbow, 1 )
        cmds.setAttr( "%s.type" % self.elbow, 11 )
        cmds.select(cl=1)
        self.wrist01= cmds.joint( n="L_wrist_Jnt01", rad=self.jntRad*0.5, p=[63.9169,116.3496,-4.5636], o=[0,-3,-35] )
        cmds.setAttr( "%s.side" % self.wrist01, 1 )
        cmds.setAttr( "%s.type" % self.wrist01, 18 )
        cmds.setAttr( "%s.otherType" % self.wrist01, "Wrist01", type= "string" )
        cmds.select(cl=1)
        self.wrist02= cmds.joint( n="L_wrist_Jnt02", rad=self.jntRad, p=[63.9169,116.3496,-4.5636], o=[0,-3,-35] )
        cmds.setAttr( "%s.side" % self.wrist02, 1 )
        cmds.setAttr( "%s.type" % self.wrist02, 18 )
        cmds.setAttr( "%s.otherType" % self.wrist02, "Wrist02", type= "string" )
        cmds.select(cl=1)
        self.palm= cmds.joint( n="L_palm_Jnt01", rad=self.jntRad, p=[70.4611,111.76727,-4.1449], o=[0,-3,-35] )
        cmds.setAttr( "%s.side" % self.palm, 1 )
        cmds.setAttr( "%s.type" % self.palm, 18 )
        cmds.setAttr( "%s.otherType" % self.palm, "Palm", type= "string" )
        cmds.select(cl=1)
        # Rearrange Hierachy
        cmds.parent( self.palm, self.wrist02 )
        cmds.parent( self.wrist02, self.wrist01 )
        cmds.parent( self.wrist01, self.elbow )
        cmds.parent( self.elbow, self.shoulder )
        cmds.parent( self.shoulder, self.clavicle )
        cmds.parent( self.clavicle, self.worldLoc )
        proxyArm= [ self.clavicle, self.shoulder, self.elbow, self.wrist01, self.wrist02, self.palm ]
        proxyDnArm= [ self.elbow, self.wrist01, self.palm ]
        for each in proxyArm:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
        for each in proxyDnArm:
            cmds.setAttr( "%s.ty" % each, l=1, ch=1 )
            cmds.setAttr( "%s.tz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rz" % each, l=1, ch=1 )  
        cmds.setAttr( "%s.ry" % self.wrist01, l=1, ch=1 ) 
        cmds.setAttr( "%s.tx" % self.wrist02, l=1, ch=1 ) 
        cmds.setAttr( "%s.ty" % self.wrist02, l=1, ch=1 ) 
        cmds.setAttr( "%s.tz" % self.wrist02, l=1, ch=1 ) 
        cmds.select(cl=1)
        # Collecting Joints Default Value
        self.lArmDVdict= { "clavicle":[(3,150,0), (0,0,0)], "shoulder":[(20,-5,-5), (0,2,-35)], "elbow":[(25,0,0),(0,-5,0)], "wrist01":[(25,0,0),(0,0,0)], "wrist02":[(0,0,0),(0,0,0)], "palm":[(8,0,0),(0,0,0)] }
        self.rArmDVdict= { "clavicle":[(-3,150,0), (-180,0,0)], "shoulder":[(-20,5,5), (0,2,-35)], "elbow":[(-25,0,0),(0,-5,0)], "wrist01":[(-25,0,0),(0,0,0)], "wrist02":[(0,0,0),(0,0,0)], "palm":[(-8,0,0),(0,0,0)] }
        
    # Proxy Fingers Function
    def proxyFingers_Fn(self, wrist02, palm, fingerNum, fingerJntNum ):
        self.wrist02= wrist02
        self.palm= palm
        self.fingerNum= fingerNum
        self.fingerJntNum= fingerJntNum
        # Collecting Joints Default Value
        self.lFingerDVdict= { "thumbA":[(0,0,0), (0,0,0)], "IndexA":[(0,0,0), (0,0,0)], "MiddleA":[(0,0,0),(0,0,0)], "RingA":[(0,0,0),(0,0,0)], "PinkyA":[(0,0,0),(0,0,0)], "Fingers":[(3,0,0),(0,0,0)] }
        self.rFingerDVdict= { "thumbA":[(0,0,0), (0,0,0)], "IndexA":[(0,0,0), (0,0,0)], "MiddleA":[(0,0,0),(0,0,0)], "RingA":[(0,0,0),(0,0,0)], "PinkyA":[(0,0,0),(0,0,0)], "Fingers":[(-3,0,0),(0,0,0)] }
        # Thumb Fingers
        if self.fingerNum >= 3:
            self.thumbJnt= []
            cmds.select(self.wrist02)
            thumbA= cmds.joint( n="L_thumb_Jnt01", rad=self.jntRad, p=[66.1566,114.7813,0.5865], o=[0,0,0] )
            cmds.setAttr( "%s.side" % thumbA, 1 )
            cmds.setAttr( "%s.type" % thumbA, 18 )
            cmds.setAttr( "%s.otherType" % thumbA, "Thumb", type= "string" )
            cmds.setAttr( "%s.jointOrientY" % thumbA, -30 )
            self.thumbJnt.append( thumbA )
            cmds.select(cl=1)
            for each in range(2, (self.fingerJntNum +1)):
                cmds.select(cl=1)
                jnt= cmds.duplicate( thumbA )
                thumb= cmds.rename( jnt, str(thumbA).replace( "1", "%s" ) % each )
                self.thumbJnt.append( thumb )
                cmds.select(cl=1)
            for each in reversed(range(0, (self.fingerJntNum -1))):
                cmds.select(cl=1)
                n= each
                cmds.parent( self.thumbJnt[n], self.thumbJnt[(n-1)] )
                n= n-1
                cmds.select(cl=1)
            cmds.parent( thumbA, self.wrist02 )
            cmds.parent( self.thumbJnt[-1], self.thumbJnt[-2] )
            for each in self.thumbJnt:
                cmds.setAttr( "%s.tx" % each, 3 )
                cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
                cmds.setAttr( "%s.v" % each, l=1, ch=1 )
            for each in range(1, self.fingerJntNum):
                cmds.setAttr( "%s.ty" % self.thumbJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.tz" % self.thumbJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.rx" % self.thumbJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.ry" % self.thumbJnt[each], l=1, ch=1 )
            # Collecting Joints Default Value
            thumbAtx= cmds.getAttr( "%s.tx" % thumbA )
            thumbAtz= cmds.getAttr( "%s.tz" % thumbA )
            self.lFingerDVdict['thumbA'] = [(thumbAtx,0,thumbAtz), (0,0,0)]
            self.rFingerDVdict['thumbA'] = [(-thumbAtx,0,-thumbAtz), (0,0,0)]
        else:
            pass
        # Index Fingers
        if self.fingerNum >= 1:
            self.indexJnt= []
            cmds.select(self.palm)
            indexA= cmds.joint( n="L_Index_Jnt01", rad=self.jntRad, p=[72.72226,110.18398, 0.50594], o=[0,0,0] )
            cmds.setAttr( "%s.side" % indexA, 1 )
            cmds.setAttr( "%s.type" % indexA, 18 )
            cmds.setAttr( "%s.otherType" % indexA, "Index", type= "string" )
            fingersTX= 4
            fingersTZ= 1.5
            self.indexJnt.append( indexA )
            cmds.setAttr( "%s.tx" % indexA, fingersTX )
            if self.fingerNum == 1:
                cmds.setAttr( "%s.tz" % indexA, 0 )
            elif 2 <= self.fingerNum <= 3 :
                cmds.setAttr( "%s.tz" % indexA, fingersTZ*2 )
            cmds.select(cl=1)
            for each in range(2, (self.fingerJntNum +1)):
                cmds.select(cl=1)
                jnt= cmds.duplicate( indexA )
                index= cmds.rename( jnt, str(indexA).replace( "1", "%s" ) % each )
                self.indexJnt.append( index )
                cmds.select(cl=1)
            for each in reversed(range(0, (self.fingerJntNum -1))):
                cmds.select(cl=1)
                n= each
                cmds.parent( self.indexJnt[n], self.indexJnt[(n-1)] )
                n= n-1
                cmds.select(cl=1)
            cmds.parent( indexA, self.palm )
            cmds.parent( self.indexJnt[-1], self.indexJnt[-2] )
            for each in self.indexJnt:
                cmds.setAttr( "%s.tx" % each, 3 )
                cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
                cmds.setAttr( "%s.v" % each, l=1, ch=1 )
            for each in range(1, self.fingerJntNum):
                cmds.setAttr( "%s.ty" % self.indexJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.tz" % self.indexJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.rx" % self.indexJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.ry" % self.indexJnt[each], l=1, ch=1 )
            # Collecting Joints Default Value
            indexAtx= cmds.getAttr( "%s.tx" % indexA )
            indexAtz= cmds.getAttr( "%s.tz" % indexA )
            self.lFingerDVdict['indexA'] = [(indexAtx,0,indexAtz), (0,0,0)]
            self.rFingerDVdict['indexA'] = [(-indexAtx,0,-indexAtz), (0,0,0)]
        else:
            print "Zero finger number. No finger joint will be create.",
        # Middle Finger
        if self.fingerNum >= 4:
            self.middleJnt= []
            cmds.select(self.palm)
            middleA= cmds.joint( n="L_middle_Jnt01", rad=self.jntRad, p=[72.8508,110.0939,-2.48994], o=[0,0,0] )
            cmds.setAttr( "%s.side" % middleA, 1 )
            cmds.setAttr( "%s.type" % middleA, 18 )
            cmds.setAttr( "%s.otherType" % middleA, "Middle", type= "string" )
            self.middleJnt.append( middleA )
            cmds.select(cl=1)
            if self.fingerNum == 4:
                cmds.setAttr( "%s.tz" % middleA, 0 )
            for each in range(2, (self.fingerJntNum +1)):
                cmds.select(cl=1)
                jnt= cmds.duplicate( middleA )
                middle= cmds.rename( jnt, str(middleA).replace( "1", "%s" ) % each )
                self.middleJnt.append( middle )
                cmds.select(cl=1)
            for each in reversed(range(0, (self.fingerJntNum -1))):
                cmds.select(cl=1)
                n= each
                cmds.parent( self.middleJnt[n], self.middleJnt[(n-1)] )
                n= n-1
                cmds.select(cl=1)
            cmds.parent( middleA, self.palm )
            cmds.parent( self.middleJnt[-1], self.middleJnt[-2] )
            for each in self.middleJnt:
                cmds.setAttr( "%s.tx" % each, 3 )
                cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
                cmds.setAttr( "%s.v" % each, l=1, ch=1 )
            for each in range(1, self.fingerJntNum):
                cmds.setAttr( "%s.ty" % self.middleJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.tz" % self.middleJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.rx" % self.middleJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.ry" % self.middleJnt[each], l=1, ch=1 )
            # Collecting Joints Default Value
            middleAtx= cmds.getAttr( "%s.tx" % middleA )
            middleAtz= cmds.getAttr( "%s.tz" % middleA )
            self.lFingerDVdict['middleA'] = [(middleAtx,0,middleAtz), (0,0,0)]
            self.rFingerDVdict['middleA'] = [(-middleAtx,0,-middleAtz), (0,0,0)]       
        else:
            pass
        # Ring Finger
        if self.fingerNum >= 5:
            self.ringJnt= []
            cmds.select(self.palm)
            ringA= cmds.joint( n="L_ring_Jnt01", rad=self.jntRad, p=[72.9794,110.0038,-5.48583], o=[0,0,0] )
            cmds.setAttr( "%s.side" % ringA, 1 )
            cmds.setAttr( "%s.type" % ringA, 18 )
            cmds.setAttr( "%s.otherType" % ringA, "Ring", type= "string" )
            self.ringJnt.append( ringA )
            cmds.select(cl=1)
            for each in range(2, (self.fingerJntNum +1)):
                cmds.select(cl=1)
                jnt= cmds.duplicate( ringA )
                ring= cmds.rename( jnt, str(ringA).replace( "1", "%s" ) % each )
                self.ringJnt.append( ring )
                cmds.select(cl=1)
            for each in reversed(range(0, (self.fingerJntNum -1))):
                cmds.select(cl=1)
                n= each
                cmds.parent( self.ringJnt[n], self.ringJnt[(n-1)] )
                n= n-1
                cmds.select(cl=1)
            cmds.parent( ringA, self.palm )
            cmds.parent( self.ringJnt[-1], self.ringJnt[-2] )
            for each in self.ringJnt:
                cmds.setAttr( "%s.tx" % each, 3 )
                cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
                cmds.setAttr( "%s.v" % each, l=1, ch=1 )
            for each in range(1, self.fingerJntNum):
                cmds.setAttr( "%s.ty" % self.ringJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.tz" % self.ringJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.rx" % self.ringJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.ry" % self.ringJnt[each], l=1, ch=1 )   
            # Collecting Joints Default Value
            ringAtx= cmds.getAttr( "%s.tx" % ringA )
            ringAtz= cmds.getAttr( "%s.tz" % ringA )
            self.lFingerDVdict['ringA'] = [(ringAtx,0,ringAtz), (0,0,0)]
            self.rFingerDVdict['ringA'] = [(-ringAtx,0,-ringAtz), (0,0,0)]
        else:
            pass
        # Pinky Finger
        if self.fingerNum >= 2:
            self.pinkyJnt= []
            cmds.select(self.palm)
            pinkyA= cmds.joint( n="L_pinky_Jnt01", rad=self.jntRad, p=[73.1080,109.9137,-8.4817], o=[0,0,0] )
            cmds.setAttr( "%s.side" % pinkyA, 1 )
            cmds.setAttr( "%s.type" % pinkyA, 18 )
            cmds.setAttr( "%s.otherType" % pinkyA, "Pinky", type= "string" )
            self.pinkyJnt.append( pinkyA )
            cmds.select(cl=1)
            if 2 <= self.fingerNum <= 3 :
                cmds.setAttr( "%s.tz" % pinkyA, -(fingersTZ*2) )
            for each in range(2, (self.fingerJntNum +1)):
                cmds.select(cl=1)
                jnt= cmds.duplicate( pinkyA )
                pinky= cmds.rename( jnt, str(pinkyA).replace( "1", "%s" ) % each )
                self.pinkyJnt.append( pinky )
                cmds.select(cl=1)
            for each in reversed(range(0, (self.fingerJntNum -1))):
                cmds.select(cl=1)
                n= each
                cmds.parent( self.pinkyJnt[n], self.pinkyJnt[(n-1)] )
                n= n-1
                cmds.select(cl=1)
            cmds.parent( pinkyA, self.palm )
            cmds.parent( self.pinkyJnt[-1], self.pinkyJnt[-2] )
            for each in self.pinkyJnt:
                cmds.setAttr( "%s.tx" % each, 3 )
                cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
                cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
                cmds.setAttr( "%s.v" % each, l=1, ch=1 )
            for each in range(1, self.fingerJntNum):
                cmds.setAttr( "%s.ty" % self.pinkyJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.tz" % self.pinkyJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.rx" % self.pinkyJnt[each], l=1, ch=1 )
                cmds.setAttr( "%s.ry" % self.pinkyJnt[each], l=1, ch=1 ) 
            # Collecting Joints Default Value
            pinkyAtx= cmds.getAttr( "%s.tx" % pinkyA )
            pinkyAtz= cmds.getAttr( "%s.tz" % pinkyA )
            self.lFingerDVdict['pinkyA'] = [(pinkyAtx,0,pinkyAtz), (0,0,0)]
            self.rFingerDVdict['pinkyA'] = [(-pinkyAtx,0,-pinkyAtz), (0,0,0)]
        else:
            pass
        
        cmds.select(cl=1)
   
   # Proxy Leg Function
    def proxyLeg_Fn(self):
        self.hip= cmds.joint( n="L_hip_Jnt01", rad=self.jntRad, p=[11,100,-1.5], o=[0,0,0] )
        cmds.setAttr( "%s.side" % self.hip, 1 )
        cmds.setAttr( "%s.type" % self.hip, 3 )
        cmds.select(cl=1)
        self.knee= cmds.joint( n="L_knee_Jnt01", rad=self.jntRad, p=[10.9998,55.0001,-1.4999], o=[4,0,0] )
        cmds.setAttr( "%s.side" % self.knee, 1 )
        cmds.setAttr( "%s.type" % self.knee, 4 )
        cmds.select(cl=1)
        self.ankle01= cmds.joint( n="L_ankle_Jnt01", rad=self.jntRad, p=[10.9999,10.1095,-4.6390], o=[4,0,0] )
        cmds.setAttr( "%s.side" % self.ankle01, 1 )
        cmds.setAttr( "%s.type" % self.ankle01, 18 )
        cmds.setAttr( "%s.otherType" % self.ankle01, "Ankle01", type= "string" )
        cmds.select(cl=1)
        self.ankle02= cmds.joint( n="L_ankle_Jnt02", rad=self.jntRad, p=[10.9999,10.1095,-4.6390], o=[4,0,0] )
        cmds.setAttr( "%s.side" % self.ankle02, 1 )
        cmds.setAttr( "%s.type" % self.ankle02, 18 )
        cmds.setAttr( "%s.otherType" % self.ankle02, "Ankle02", type= "string" )
        cmds.select(cl=1)
        self.ball= cmds.joint( n="L_ball_Jnt01", rad=self.jntRad, p=[11, 1.7314,14.8239], o=[4,0,0] )
        cmds.setAttr( "%s.side" % self.ball, 1 )
        cmds.setAttr( "%s.type" % self.ball, 18 )
        cmds.setAttr( "%s.otherType" % self.ball, "Ball", type= "string" )
        cmds.select(cl=1)
        self.toe= cmds.joint( n="L_toe_Jnt01", rad=self.jntRad, p=[10.9999, 1.0340,24.7994], o=[4,0,0] )
        cmds.setAttr( "%s.side" % self.ball, 1 )
        cmds.setAttr( "%s.type" % self.ball, 6 )
        cmds.select(cl=1)
        # Rearrange Hierachy
        cmds.parent( self.toe, self.ball )
        cmds.parent( self.ball, self.ankle02 )
        cmds.parent( self.ankle02, self.ankle01 )
        cmds.parent( self.ankle01, self.knee )
        cmds.parent( self.knee, self.hip )
        # Create Foot Locators
        self.frontLoc= cmds.spaceLocator( n="L_leg_front_loc" )[0]
        cmds.xform( self.frontLoc, t= [12,0,26] )
        self.backLoc= cmds.spaceLocator( n="L_leg_back_loc" )[0]
        cmds.xform( self.backLoc, t= [11,0,-12] )
        self.sideLfLoc= cmds.spaceLocator( n="L_leg_sideLf_loc" )[0]
        cmds.xform( self.sideLfLoc, t= [18,0,9] )
        self.sideRtLoc= cmds.spaceLocator( n="L_leg_sideRt_loc" )[0]
        cmds.xform( self.sideRtLoc, t= [5,0,9] )
        self.tmpLocGRP= cmds.group( n="L_tmpLocGRP", em=1 )
        cmds.parent( self.frontLoc, self.backLoc, self.sideLfLoc, self.sideRtLoc, self.tmpLocGRP )
        cmds.parentConstraint( self.ankle02, self.tmpLocGRP, mo=1 )
        cmds.parent( self.hip, self.tmpLocGRP, self.worldLoc )
        proxyLeg= [ self.hip, self.knee, self.ankle01, self.ankle02, self.ball, self.toe, self.frontLoc, self.backLoc, self.sideLfLoc, self.sideRtLoc ]
        proxyDnLeg= [ self.knee, self.ankle01 ]
        proxyFeet= [ self.ball, self.toe ]
        for each in proxyLeg:
            cmds.setAttr( "%s.sx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sy" % each, l=1, ch=1 )
            cmds.setAttr( "%s.sz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.v" % each, l=1, ch=1 )
        for each in proxyDnLeg:
            cmds.setAttr( "%s.tx" % each, l=1, ch=1 )
            cmds.setAttr( "%s.tz" % each, l=1, ch=1 )
            cmds.setAttr( "%s.ry" % each, l=1, ch=1 )
            cmds.setAttr( "%s.rz" % each, l=1, ch=1 )
        for each in proxyFeet:
            cmds.setAttr( "%s.tx" % each, l=1, ch=1  )
            cmds.setAttr( "%s.rx" % each, l=1, ch=1  )
            cmds.setAttr( "%s.ry" % each, l=1, ch=1  )
            cmds.setAttr( "%s.rz" % each, l=1, ch=1  )
        cmds.setAttr( "%s.ty" % self.toe, l=1, ch=1 )  
        cmds.setAttr( "%s.tx" % self.ankle02, l=1, ch=1 ) 
        cmds.setAttr( "%s.ty" % self.ankle02, l=1, ch=1 ) 
        cmds.setAttr( "%s.tz" % self.ankle02, l=1, ch=1 ) 
        cmds.select(cl=1)
        # Collecting Joints Default Value
        self.lLegDVdict= { "Hip":[(11,100,-1.5), (0,0,0)], "knee":[(0,-45,0), (4,0,0)], "ankle01":[(0,-45,0),(0,0,0)], "ankle02":[(0,0,0),(0,0,0)], "ball":[(0,-7,20),(0,0,0)], "toe":[(0,0,10),(0,0,0)] }
        self.lfootLocDVdict= { "frontLoc": [(12,0,26), (0,0,0)], "backLoc": [(11,0,-12), (0,0,0)], "sideLf": [(18,0,9), (0,0,0)], "sideRt":[(5,0,9),(0,0,0)] }
        self.rLegDVdict= { "Hip":[(-11,100,-1.5), (0,0,0)], "knee":[(0,45,0), (4,0,0)], "ankle01":[(0,45,0),(0,0,0)], "ankle02":[(0,0,0),(0,0,0)], "ball":[(0,7,-20),(0,0,0)], "toe":[(0,0,-10),(0,0,0)] }
        self.rfootLocDVdict= { "frontLoc": [(-12,0,26), (0,0,0)], "backLoc": [(-11,0,-12), (0,0,0)], "sideLf": [(-18,0,9), (0,0,0)], "sideRt":[(-5,0,9),(0,0,0)] }
            
if __name__ == "__main__":
    a= proxyBipedJoint_Cl(1,0)
    a.proxyHead_Fn()
    a.proxyEyes_Fn("head_Jnt01","head_Jnt02")
    a.proxyJaw_Fn("head_Jnt01")
    a.proxyTongue_Fn("jaw_Jnt01")
    a.proxyTeeths_Fn("head_Jnt01","jaw_Jnt01")
    a.proxyTorso_Fn()
    a.proxyArm_Fn()
    a.proxyFingers_Fn("L_wrist_Jnt02","L_palm_Jnt01", 5, 4)
    a.proxyLeg_Fn()
    #print a.headDVdict["neck"]
