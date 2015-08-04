import maya.cmds as cmds

class CNailCtrlHrc_Cl( object ):
    def __init__( self ):
        pass
    
    def cNailCtrlHrc_Fn( self, name ):
        self.name= name
        self.ctrl= cmds.curve( n= '%s_ctrl' % self.name, d=1, 
        p=[(0,0,0),(-2,0,0),(-2.292893,0,-0.707107),(-3,0,-1),(-3.707107,0,-0.707107),(-4,0,0),(-3.707107,0,0.707107),(-3,0,1),(-2.292893,0,0.707107),(-2,0,0),(-2.292893,0,0.707107),(-3.707107,0,-0.707107),(-3,0,-1),(-2.292893,0,-0.707107),(-3.707107,0,0.707107),(-3,0,1),(-2.292893,0,0.707107),(-2,0,0),(0,0,0),(2,0,0),(2.292893,0,-0.707107),(3,0,-1),(3.707107,0,-0.707107),(4,0,0),(3.707107,0,0.707107),(3,0,1),(2.292893,0,0.707107),(2,0,0),(2.292893,0,0.707107),(3.707107,0,-0.707107),(3,0,-1),(2.292893,0,-0.707107),(3.707107,0,0.707107)] )
        cmds.xform( self.ctrl, ro= [0,90,0] )
        cmds.makeIdentity( self.ctrl, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%s_ctrl.sx' % self.name, l=1, k=0, cb=0 )
        cmds.setAttr( '%s_ctrl.sy' % self.name, l=1, k=0, cb=0 )
        cmds.setAttr( '%s_ctrl.sz' % self.name, l=1, k=0, cb=0 )
        cmds.setAttr( '%s_ctrl.v' % self.name, l=1, k=0, cb=0 )
        self.sdkGrp= cmds.group( n= '%s_ctrl_sdk' % self.name, em=0 )
        self.alignGrp= cmds.group( n= '%s_ctrl_align' % self.name, em=0 )
        self.spaceGrp= cmds.group( n= '%s_ctrl_space' % self.name, em=0 )
        return [ self.ctrl, self.sdkGrp, self.alignGrp, self.spaceGrp ]

if __name__ == "__main__":
    abc= CNailCtrlHrc_Cl()
