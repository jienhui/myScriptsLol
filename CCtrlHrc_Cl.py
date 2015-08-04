import maya.cmds as cmds

class CCtrlHrc_Cl( object ):
    def __init__( self ):
        pass
    
    def cCtrlHrc_Fn( self, name ):
        self.name= name
        self.ctrl= cmds.circle( n= '%s_ctrl' % self.name, nr= (0,1,0), ch=0, d=3,r=1 )
        cmds.setAttr( '%s_ctrl.sx' % self.name, l=1, k=0, cb=0 )
        cmds.setAttr( '%s_ctrl.sy' % self.name, l=1, k=0, cb=0 )
        cmds.setAttr( '%s_ctrl.sz' % self.name, l=1, k=0, cb=0 )
        cmds.setAttr( '%s_ctrl.v' % self.name, l=1, k=0, cb=0 )
        cmds.xform( '%s.cv[*]' % self.ctrl[0], ro= [90,0,0] )
        self.sdkGrp= cmds.group( n= '%s_ctrl_sdk' % self.name, em=0 )
        self.alignGrp= cmds.group( n= '%s_ctrl_align' % self.name, em=0 )
        self.spaceGrp= cmds.group( n= '%s_ctrl_space' % self.name, em=0 )
        return [ self.ctrl, self.sdkGrp, self.alignGrp, self.spaceGrp ]
