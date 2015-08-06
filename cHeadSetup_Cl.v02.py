import maya.cmds as cmds
import cCtrlHrc_Cl as CC

# Head Setup Class
class HeadSetup_Cl( object ):
    def __init__( self ):
        global c
        c= CC.CCtrlHrc_Cl()
        
    
    # Head Setup Function    
    def headSetup_Fn( self, neck, head, lEye, rEye, name ):
        self.neck= neck
        self.head= head
        self.lEye= lEye
        self.rEye= rEye
        self.name= name
        
        cmds.select( self.head, hi=1 )
        headJntSel= cmds.ls( sl=1 )
        headEndPos= cmds.getAttr( '%s.tx' % headJntSel[1] )
        self.neckCtrl= c.cCtrlHrc_Fn( 'neck01' )
        cmds.xform( self.neckCtrl[0], ro=[0,-90,0] )
        cmds.makeIdentity( self.neckCtrl[0], a=1, t=1, r=1 ) 
        tmpCnst= cmds.parentConstraint( self.neck, self.neckCtrl[-1], mo=0 )
        cmds.delete( tmpCnst )
        cmds.pointConstraint( self.neckCtrl[0], self.neck, mo=0 )
        
        # Setup Head Controller
        self.headCtrl= cmds.curve( n= 'head01_ctrl', d=1, p= ([0,0.35,-1.001567],[-0.336638,0.677886,-0.751175],[-0.0959835,0.677886,-0.751175],[-0.0959835,0.850458,-0.500783],[-0.0959835,0.954001,-0.0987656],[-0.500783,0.850458,-0.0987656],[-0.751175,0.677886,-0.0987656],[-0.751175,0.677886,-0.336638],[-1.001567,0.35,0],[-0.751175,0.677886,0.336638],[-0.751175,0.677886,0.0987656],[-0.500783,0.850458,0.0987656],[-0.0959835,0.954001,0.0987656],[-0.0959835,0.850458,0.500783],[-0.0959835,0.677886,0.751175],[-0.336638,0.677886,0.751175],[0,0.35,1.001567],[0.336638,0.677886,0.751175],[0.0959835,0.677886,0.751175],[0.0959835,0.850458,0.500783],[0.0959835,0.954001,0.0987656],[0.500783,0.850458,0.0987656],[0.751175,0.677886,0.0987656],[0.751175,0.677886,0.336638],[1.001567,0.35,0],[0.751175,0.677886,-0.336638],[0.751175,0.677886,-0.0987656],[0.500783,0.850458,-0.0987656],[0.0959835,0.954001,-0.0987656],[0.0959835,0.850458,-0.500783],[0.0959835,0.677886,-0.751175],[0.336638,0.677886,-0.751175],[0,0.35,-1.001567]) )
        cmds.xform( self.headCtrl, ro=[0,0,-90] )
        cmds.makeIdentity( self.headCtrl, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%s.sx' % self.headCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.headCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.headCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.headCtrl, l=1, k=0, cb=0 ) 
        cmds.addAttr( self.headCtrl, ln='follow', at='enum', en='World:Neck:', k=True )
        cmds.setAttr( '%s.follow' % self.headCtrl, l=False, k=True, cb=True )
        cmds.setAttr( '%s.follow' % self.headCtrl, keyable= True)
        cmds.setAttr( '%s.follow' % self.headCtrl, 1 )
        cmds.group( n= '%s_sdk' % self.headCtrl, em=0 )
        cmds.group( n= '%s_align' % self.headCtrl, em=0 )
        self.headSpace= cmds.group( n= '%s_space' % self.headCtrl, em=0 )
        cmds.move( headEndPos,0,0, '%s.cv[*]' % self.headCtrl, r=1, os=1, wd=1 )
        tmpCnst= cmds.parentConstraint( self.head, self.headSpace, mo=0 )
        cmds.delete( tmpCnst )
        cmds.orientConstraint( self.headCtrl, self.head, mo=1 )
        cmds.aimConstraint( self.headCtrl, self.neck, mo=1 )
        neckCnst= cmds.parentConstraint( self.neckCtrl[0], self.headSpace, mo=1 )
        cmds.connectAttr( '%s.follow' % self.headCtrl, str(neckCnst[0]) + '.%sW0' % self.neckCtrl[0][0] )
        
        
        # Eye Setup
        cmds.select( self.lEye, hi=1 )
        lEyeList=cmds.ls( sl=1 )
        eyeEndPos= cmds.getAttr( '%s.tx' % lEyeList[1] )
        eyeCtrlPos= (eyeEndPos) * 8
        cmds.select( self.lEye,self.rEye )
        eyes= cmds.ls( sl=1 )
        eyeCtrlList= []
        eyeSpaceList= []
        for each in eyes:
            eyeName= str(each).split( '_jnt' )
            eyeCtrl= c.cCtrlHrc_Fn( eyeName[0] )
            eyeCtrlList.append( eyeCtrl[0] )
            eyeSpaceList.append( eyeCtrl[-1] )
            tmpCnst= cmds.parentConstraint( each, eyeCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.parent( eyeCtrl[-1], each )
            cmds.move( eyeCtrlPos,0,0, eyeCtrl[-1], r=1, os=1, wd=1 )
            cmds.parent( eyeCtrl[-1], w=1 )
            cmds.xform( '%s.cv[*]' % eyeCtrl[0][0], ro= [0,90,0] )
            cmds.aimConstraint( eyeCtrl[0], each, mo=1 )
        
        # Create Main Eye Controller
        self.mainEye= c.cCtrlHrc_Fn( 'main_eye' )
        cmds.addAttr( self.mainEye[0], ln='follow', at='enum', en='World:Head:' )
        cmds.setAttr( '%s.follow' % self.mainEye[0][0], e=1, l=False, k=True, cb=True )
        cmds.setAttr( '%s.follow' % self.mainEye[0][0], 1 )
        tmpCnst= cmds.parentConstraint( eyeCtrlList[0], eyeCtrlList[1], self.mainEye[-1], mo=0 )
        cmds.delete( tmpCnst )
        cmds.xform( '%s.cv[*]' % self.mainEye[0][0], ro= [0,90,0], s=[4,2,4]  )
        headCnst= cmds.parentConstraint( self.head, self.mainEye[-1], mo=1 )
        cmds.connectAttr( '%s.follow' % self.mainEye[0][0], str(headCnst[0]) + '.%sW0' % self.head )
        cmds.parent( eyeSpaceList[0], eyeSpaceList[1], self.mainEye[0] )
        
        return [ self.neckCtrl[-1], self.headSpace, self.mainEye[0] ]
        
    # Mouth Setup Function    
    def mouthSetup_Fn( self, jaw, tongue, upTeeth, dnTeeth, name ):
        self.jaw= jaw
        self.tongue= tongue
        self.upTeeth= upTeeth
        self.dnTeeth= dnTeeth
        self.name= name
        self.innerMouth= cmds.group( n= 'innerMouth_ctrlGrp', em=1 )
        
        # Jaw Setup
        cmds.select( self.jaw, hi=1 )
        jawJntSel= cmds.ls( sl=1 )
        jawEndPos= cmds.getAttr( '%s.tx' % jawJntSel[1] )
        self.jawCtrl= cmds.curve( n= 'jaw01_ctrl', d=1, p= ([0,0.35,-1.001567],[-0.336638,0.677886,-0.751175],[-0.0959835,0.677886,-0.751175],[-0.0959835,0.850458,-0.500783],[-0.0959835,0.954001,-0.0987656],[-0.500783,0.850458,-0.0987656],[-0.751175,0.677886,-0.0987656],[-0.751175,0.677886,-0.336638],[-1.001567,0.35,0],[-0.751175,0.677886,0.336638],[-0.751175,0.677886,0.0987656],[-0.500783,0.850458,0.0987656],[-0.0959835,0.954001,0.0987656],[-0.0959835,0.850458,0.500783],[-0.0959835,0.677886,0.751175],[-0.336638,0.677886,0.751175],[0,0.35,1.001567],[0.336638,0.677886,0.751175],[0.0959835,0.677886,0.751175],[0.0959835,0.850458,0.500783],[0.0959835,0.954001,0.0987656],[0.500783,0.850458,0.0987656],[0.751175,0.677886,0.0987656],[0.751175,0.677886,0.336638],[1.001567,0.35,0],[0.751175,0.677886,-0.336638],[0.751175,0.677886,-0.0987656],[0.500783,0.850458,-0.0987656],[0.0959835,0.954001,-0.0987656],[0.0959835,0.850458,-0.500783],[0.0959835,0.677886,-0.751175],[0.336638,0.677886,-0.751175],[0,0.35,-1.001567]) )
        cmds.xform( self.jawCtrl, ro= [0,0,-90] )
        cmds.makeIdentity( self.jawCtrl, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%s.sx' % self.jawCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sy' % self.jawCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.sz' % self.jawCtrl, l=1, k=0, cb=0 )
        cmds.setAttr( '%s.v' % self.jawCtrl, l=1, k=0, cb=0 )
        cmds.group( n= '%s_sdk' % self.jawCtrl, em=0 )
        cmds.group( n= '%s_align' % self.jawCtrl, em=0 )
        self.jawSpace= cmds.group( n= '%s_space' % self.jawCtrl, em=0 )
        cmds.move( jawEndPos,0,0, '%s.cv[*]' % self.jawCtrl, r=1, os=1, wd=1 )
        tmpCnst= cmds.parentConstraint( self.jaw, self.jawSpace, mo=0 )
        cmds.delete( tmpCnst )
        cmds.parentConstraint( self.jawCtrl, self.jaw, mo=1 )
        cmds.parentConstraint( self.head, self.jawSpace, mo=1 )
        
        # Tongue Setup
        cmds.select( self.tongue, hi=1 )
        tongueJntSel= cmds.ls( sl=1 )
        tongueCtrlList= []
        tongueSpaceList= []  
        for each in tongueJntSel:
            if each.endswith( '_end' ):
                tongueJntSel.remove( tongueJntSel[-1] )            
        for each in tongueJntSel:    
            tongueName= str(each).split( '_jnt' )
            tongueCtrl= c.cCtrlHrc_Fn( tongueName[0] )
            tongueCtrlList.append( tongueCtrl[0] )
            tongueSpaceList.append( tongueCtrl[-1] )
            cmds.xform( tongueCtrl[0], ro=[0,90,0] )
            cmds.makeIdentity( tongueCtrl[0], a=1, t=1, r=1 )
            tmpCnst= cmds.parentConstraint( each, tongueCtrl[-1], mo=0 )
            cmds.delete( tmpCnst )
            cmds.parentConstraint( tongueCtrl[0], each, mo=1 )
        cmds.parent( tongueSpaceList[-1], tongueCtrlList[-2] )
        cmds.parent( tongueSpaceList[-2], tongueCtrlList[0] )
        cmds.parentConstraint( self.jawCtrl, tongueSpaceList[0], mo=1 )
        cmds.parent( tongueSpaceList[0], self.innerMouth )
        
        # Teeth Setup
        cmds.select( self.upTeeth, self.dnTeeth )
        teeth= cmds.ls( sl=1 )
        teethSpaceList= []
        for each in teeth:
            teethCtrl= cmds.curve( n= str(each).replace('_jnt', '_ctrl' ), d=1, p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)] )
            cmds.setAttr( '%s.sx' % teethCtrl, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % teethCtrl, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % teethCtrl, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.v' % teethCtrl, l=1, k=0, cb=0 )
            cmds.group( n= '%s_sdk' % teethCtrl, em=0 )
            cmds.group( n= '%s_align' % teethCtrl, em=0 )
            teethSpace= cmds.group( n= '%s_space' % teethCtrl, em=0 )
            teethSpaceList.append( teethSpace )
            tmpCnst= cmds.parentConstraint( each, teethSpace, mo=0 )
            cmds.delete( tmpCnst )
            cmds.parentConstraint( teethCtrl, each, mo=1 )
            cmds.parent( teethSpace, self.innerMouth )
        cmds.parentConstraint( self.jawCtrl, teethSpaceList[1], mo=1 )
        cmds.parentConstraint( self.head, teethSpaceList[0], mo=1 )
        
        return [ self.jawSpace, self.innerMouth ]

if __name__ == '__main__' :
    CC= HeadSetup_Cl()
    h= CC.headSetup_Fn( 'neck01_jnt', 'head01_jnt', 'l_eye01_jnt', 'r_eye01_jnt', 'head' )
    m= CC.mouthSetup_Fn( 'jaw01_jnt', 'tongue01_jnt', 'upper_teeth01_jnt', 'lower_teeth01_jnt', 'mouth' )
    print m
    print h
