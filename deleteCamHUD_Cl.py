# Delete CamHUD
import maya.cmds as cmds

class deleteCamHUD():
    def __init__( self ):
        
        camShapes= cmds.ls( ca=1, v=1 )
        self.camHUD= []
        for each in camShapes:
            typeValue= cmds.attributeQuery( 'type', node= str(each), ex=1 )
            if typeValue == True:
                self.camHUD.append( each )
        selCam= cmds.listRelatives( self.camHUD, p=1 )
        self.selCam= selCam
        self.deleteCamHUD_Fn()
    
    def deleteCamHUD_Fn( self ):
        for each in self.selCam:
            # Delete HUD on Selected Camera
            cmds.select( cl=1 )
            self.camShape= cmds.listRelatives( each, s=1 )
            cmds.deleteAttr( '%s.type' % self.camHUD[0] )
            cmds.deleteAttr( '%s.EXTRA' % each )
            cmds.deleteAttr( '%s.TVGateVis' % each )
            cmds.deleteAttr( '%s.TVsafeActionAdjust' % each )
            cmds.deleteAttr( '%s.fulcrumVis' % each )
            cmds.deleteAttr( '%s.fulcrumSize' % each )
            cmds.deleteAttr( '%s.nearClip' % each )
            cmds.deleteAttr( '%s.farClip' % each )
            cmds.deleteAttr( '%s.matchGuide' % each )
        cmds.delete( "CameraLabel_grp", "CAM_Ex_displayFrameCount" )
        cmds.select( cl=1 )
        
if __name__ == '__main__':
    abd= deleteCamHUD()
