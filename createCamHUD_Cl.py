# shotCamHUD Class
import maya.cmds as cmds
import os as os

class createCamHUD():
    def __init__( self ):
        selCam= cmds.ls(sl=1)
        self.selCam= selCam
        self.createCamHUD_Fn()
    
    # shotCamHUD Function
    def createCamHUD_Fn(self):
        
        cmds.setAttr('%s.v' % self.selCam[0], lock= False )
        cmds.setAttr('%s.v' % self.selCam[0], 1 )
        self.camShape= cmds.listRelatives( self.selCam, s=1 )
        
        # Create HUD Annotation
        cmds.select( cl=1 )
        self.sceneInfoLoc= cmds.spaceLocator( n= '%s.sceneInfoLocator' % self.selCam[0] )
        cmds.setAttr( '%sShape.lodVisibility' % self.sceneInfoLoc[0], 0 )
        labelList= [ ('%s_sceneName' % self.selCam[0]), ('%s_userInfo' % self.selCam[0]), ('%s_cameraName' % self.selCam[0]), ('%s_sceneInfo' % self.selCam[0]) ]
        anntList= []
        anntGrpList= []
        for i, each in enumerate(range(1,5)):
            ant= cmds.annotate( self.sceneInfoLoc )
            annt= cmds.rename( 'annotation1', labelList[i] )
            cmds.setAttr( '%s.tx' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ty' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.tz' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rx' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % annt, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % annt, l=1, k=0, cb=0 ) 
            cmds.setAttr( '%s.displayArrow' % annt, 0 )
            anntGrp= cmds.group( n= 'label_%s' % labelList[i], em=0 )
            anntGrpList.append( anntGrp )
            cmds.parent( anntGrp, self.sceneInfoLoc )
            anntList.append( annt )
        # Create Expression for each Annotation
        if cmds.objExists( 'CAM_Ex_displayFrameCount' ):
            cmds.select( cl=1 )
            cmds.select( '%sShape' % anntList[3] )
            newSceneInfoAnnt= cmds.ls( sl=1 )
            cmds.select( cl=1 )
            cmds.select( '*_sceneInfoShape', add=1 )
            sceneInfoAnntList= cmds.ls( sl=1 )
            sceneInfoAnntList.remove( newSceneInfoAnnt[0] )
            cmds.connectAttr( '%s.text' % sceneInfoAnntList[0], '%s.text' % newSceneInfoAnnt[0] )
            cmds.select( cl=1 )
        else:
            cmds.expression( s= "//-------set timecode seconds padding--------- \nglobal proc string secondsPadding(int $num)\n{\nstring $tmp;\nint $pad;\n\n$tmp = $num;\n$pad = size($tmp);\n\nif($pad == 1)\n{\nreturn (\"0\" + $tmp);\n}\nelse\n{\nreturn $tmp;\n}\n}\n\n//-------set timecode frames padding\nglobal proc string framesPadding(int $num)\n{\nstring $tmp;\nint $pad;\n\n$tmp = $num;\n$pad = size($tmp);\n\nif($pad == 1)\n{\nreturn (\"0\" + $tmp);\n}\nelse\n{\nreturn $tmp;\n}\n}\n\n$ct = `currentTime -q`;\n$fps = `currentTimeUnitToFPS`;\n$s = ($ct % (60 * $fps)) / $fps;\n$f = ($ct % $fps);\nif ($f == 0)\n{ \n$f = 25;\n$s = $s - 1;\n}\n$ss = secondsPadding($s);\n$ff = framesPadding($f);\n\nstring $sequence = .I[0];\nstring $seqpad = substring(\"-0000\",1,4-size($sequence));\nstring $sq = $seqpad + $sequence;\n\nstring $scene = .I[1];\nstring $scpad = substring(\"-0000\",1,4-size($scene));\nstring $sc = $scpad + $scene;\n\nint $sceneindex = .I[2];\nstring $sceneletter = \"\";\nif ($sceneindex > 0)\n{\n$sceneletter = substring(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\", $sceneindex, $sceneindex);\n}\nstring $sclabel = $sc + $sceneletter;\n\nstring $cTxt = \"sq\" + $sq + \" sc\" + $sclabel + \" | fr-\";\n\n// get the global frame number as a string\n//string $annotation1Text = `file -q -sn -shn` + \" | \" + frame + (\" / \" + `playbackOptions -q -maxTime`) + \" | \" + ($ss + \":\" + $ff);\nstring $annotation1Text = frame + (\" / \" + `playbackOptions -q -maxTime`) + \" | \" + ($ss + \":\" + $ff);\n\n// set it to annotationShape1.text attribute \nstring $prefix[] = `ls -s \"*sceneInfoShape\"`;\nstring $frameLabel = $prefix[0] +  \".text\" ;\nsetAttr -type \"string\"  $frameLabel $annotation1Text;", o= '%sShape' % str(anntList[0]), n= 'CAM_Ex_displayFrameCount', ae=1, uc= 'none' )
        # Modify Annotions Location
        cmds.xform( anntGrpList[0], t= [1.724,0.01,0] )
        cmds.xform( anntGrpList[1], t= [4.014,0.01,0] )
        cmds.xform( anntGrpList[2], t= [1.724,-1.268,0] )
        cmds.xform( anntGrpList[3], t= [3.974,-1.268,0] )
        cmds.xform( self.sceneInfoLoc, t= [-0.250,0.205,-0.005], s= [0.146,0.336,0.336] )
        # Lock Attributes
        for each in anntGrpList:
            cmds.setAttr( '%s.tx' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ty' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.tz' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rx' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.overrideEnabled' % each,1 )
        # Set Labels Color
        cmds.setAttr( '%s.overrideColor' % anntGrpList[0],18 )
        cmds.setAttr( '%s.overrideColor' % anntGrpList[1],18 )
        cmds.setAttr( '%s.overrideColor' % anntGrpList[2],18 )
        cmds.setAttr( '%s.overrideColor' % anntGrpList[3],17 )
        # Set Label Name
        fileName= cmds.file( q=1, sn=1, shn=1 )
        userName= os.getenv( "user" )
        cmds.setAttr( '%sShape.text' % anntList[0], fileName, type= "string" )
        cmds.setAttr( '%sShape.text' % anntList[1], userName, type= "string" )
        cmds.setAttr( '%sShape.text' % anntList[2], self.selCam[0], type= "string" )
        
        # Create Film Gates and Fulcrum
        self.prism= cmds.polyPyramid( n= '%s_fulcrum' % self.selCam[0], ch=0 )
        cmds.xform( self.prism, ro= [90,0,45], sp=[0,0.353553,0], rp=[0,0.353553,0] )
        tmpCnst= cmds.pointConstraint( self.selCam, self.prism, mo=0 )
        cmds.delete( tmpCnst )
        cmds.makeIdentity( self.prism, a=1, t=1, r=1, s=1 )
        cmds.xform( self.prism, t= [0,0,0.662], s= [0.86,0.49,1] )
        cmds.makeIdentity( self.prism, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%sShape.overrideEnabled' % self.prism[0], 1 )
        cmds.setAttr( '%sShape.overrideDisplayType' % self.prism[0], 1 )
        self.TVsafe= cmds.polyPlane( n= '%s_TVsafe_4x3' % self.selCam[0], sx=1, sy=1, ch=0 )
        cmds.xform( self.TVsafe, ro=[90,0,0], s=[0.554,0.410,0.410] )
        cmds.makeIdentity( self.TVsafe, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%sShape.overrideEnabled' % self.TVsafe[0], 1 )
        cmds.setAttr( '%sShape.overrideLevelOfDetail' % self.TVsafe[0], 1 )
        cmds.setAttr( '%sShape.overrideDisplayType' % self.TVsafe[0], 1 )
        self.filmGateA= cmds.polyPlane( n= '%s_Filmgate_4x3' % self.selCam[0], sx=1, sy=1, ch=0 )
        cmds.xform( self.filmGateA, ro=[90,0,0], s= [0.613,0.4,0.454] )
        cmds.makeIdentity( self.filmGateA, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%sShape.overrideEnabled' % self.filmGateA[0], 1 )
        cmds.setAttr( '%sShape.overrideLevelOfDetail' % self.filmGateA[0], 1 )
        cmds.setAttr( '%sShape.overrideDisplayType' % self.filmGateA[0], 1 )
        self.tvGateGrp= cmds.group( n= '%s_TV_4x3_adjust' % self.selCam[0], em=0 )
        cmds.parent( self.TVsafe, self.tvGateGrp )
        self.filmGateB= cmds.polyPlane( n= '%s_Filmgate_16x9' % self.selCam[0], sx=1, sy=1, ch=0 )
        cmds.xform( self.filmGateB, ro=[90,0,0], s= [0.806,0.453,0.453] )
        cmds.makeIdentity( self.filmGateB, a=1, t=1, r=1, s=1 )
        cmds.setAttr( '%sShape.overrideEnabled' % self.filmGateB[0], 1 )
        cmds.setAttr( '%sShape.overrideLevelOfDetail' % self.filmGateB[0], 1 )
        cmds.setAttr( '%sShape.overrideDisplayType' % self.filmGateB[0], 1 )
        self.clipGrp= cmds.group( n= '%s_lock_to_clipping' % self.selCam[0], em=0 )
        cmds.parent( self.sceneInfoLoc, self.tvGateGrp, self.filmGateB )
        cmds.xform( self.clipGrp, t= [0,0,-0.345], s= [6.1,4.56,4.56] )
        self.guideGrp= cmds.group( n= '%s_GUIDES' % self.selCam[0], em=1 )
        cmds.parent( self.clipGrp, self.guideGrp )
        cmds.xform( self.guideGrp, t= [0,0,-0.662], s= [0.875,0.875,1] )
        gates= [ '%s_TVsafe_4x3' % self.selCam[0], '%s_Filmgate_4x3' % self.selCam[0] ]
        for each in gates:
            cmds.setAttr( '%s.tx' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ty' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.tz' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rx' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.ry' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.rz' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sx' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sy' % each, l=1, k=0, cb=0 )
            cmds.setAttr( '%s.sz' % each, l=1, k=0, cb=0 )
        
        # Setup Camera
        cmds.modelEditor( 'modelPanel4', e=1, dim=1 )
        cmds.setAttr( '%s.nearClipPlane' % self.camShape[0], lock= False )
        cmds.setAttr( '%s.nearClipPlane' % self.camShape[0], 1 )
        cmds.setAttr( '%s.farClipPlane' % self.camShape[0], lock= False )
        cmds.setAttr( '%s.farClipPlane' % self.camShape[0], 100000 )
        cmds.setAttr( '%s.filmFit' % self.camShape[0], lock= False )
        cmds.setAttr( '%s.filmFit' % self.camShape[0], 3 )
        self.guideSdk= cmds.group( n= '%s_GUIDE_sdk' % self.selCam[0], em=1 )
        self.guideAlign= cmds.group( n= '%s_GUIDE_align' % self.selCam[0], em=0 )
        self.guideSpace= cmds.group( n= '%s_GUIDE_space' % self.selCam[0], em=0 )
        cmds.parent( self.guideGrp, self.guideSdk )
        tmpScale= cmds.scaleConstraint( self.selCam, self.guideSpace, mo=0 )
        tmpCnst= cmds.parentConstraint( self.selCam, self.guideSpace, mo=0 )
        cmds.delete( tmpCnst, tmpScale )
        tmpScale= cmds.scaleConstraint( self.selCam, self.prism, mo=0 )
        tmpCnst= cmds.parentConstraint( self.selCam, self.prism, mo=0 )
        cmds.delete( tmpCnst, tmpScale )
        cmds.parent( self.prism, self.guideGrp )
        cmds.parentConstraint( self.selCam, self.guideSpace, mo=0 )
        cmds.scaleConstraint( self.selCam, self.guideSpace, mo=0 )
        # Hide All Default Maya HUD
        defaultHUD= cmds.headsUpDisplay( lv=0 )
        # setUp Camera Attributes
        cmds.addAttr( self.selCam[0], ln='EXTRA', at='enum', en='-' )
        cmds.setAttr( '%s.EXTRA' % self.selCam[0], e=1, l=False, k=False, cb=True )
        cmds.addAttr( self.camShape[0], ln='type', dt='string' )
        cmds.setAttr( '%s.type' % self.camShape[0], e=1, k=True )
        cmds.setAttr( '%s.type' % self.camShape[0],  'shotCam', type= "string" )
        # TV Adjust Attributes
        cmds.addAttr( self.selCam[0], ln='TVGateVis', at='enum', en='Off:On:')
        cmds.setAttr( '%s.TVGateVis' % self.selCam[0], e=1, k=True )
        cmds.connectAttr( '%s.TVGateVis' % self.selCam[0], '%s.v' % self.tvGateGrp )
        cmds.addAttr( self.selCam[0], ln='TVsafeActionAdjust', at='float', hnv=1, hxv=1, max= 1, min= -1 )
        cmds.setAttr( '%s.TVsafeActionAdjust' % self.selCam[0], e=1, k=True )
        self.tvAdjustMD= cmds.createNode( 'multiplyDivide', n= 'CAM_tvAdjust_multiplier' )
        cmds.connectAttr( '%s.TVsafeActionAdjust' % self.selCam[0], '%s.input1X' % self.tvAdjustMD )
        cmds.setAttr( '%s.input2X' % self.tvAdjustMD, 0.025 )
        cmds.connectAttr( '%s.outputX' % self.tvAdjustMD, '%s.translateX' % self.tvGateGrp )
        # fulcrum Attributes
        cmds.addAttr( self.selCam[0], ln='fulcrumVis', at='enum', en='Off:On:' )
        cmds.setAttr( '%s.fulcrumVis' % self.selCam[0], e=1, k=True )
        cmds.connectAttr( '%s.fulcrumVis' % self.selCam[0], '%s.v' % self.prism[0] )
        cmds.addAttr( self.selCam[0], ln='fulcrumSize', at='float', hnv=1, min= 1 )
        cmds.setAttr( '%s.fulcrumSize' % self.selCam[0], 3 )
        cmds.setAttr( '%s.fulcrumSize' % self.selCam[0], e=1, k=True)
        self.prismScalerMD= cmds.createNode( 'multiplyDivide', n= 'CAM_fulcrumScaler' )
        cmds.connectAttr( '%s.fulcrumSize' % self.selCam[0], '%s.input1X' % self.prismScalerMD )
        cmds.connectAttr( '%s.fulcrumSize' % self.selCam[0], '%s.input1Y' % self.prismScalerMD )
        cmds.connectAttr( '%s.fulcrumSize' % self.selCam[0], '%s.input1Z' % self.prismScalerMD )
        cmds.setAttr( '%s.input2X' % self.prismScalerMD, 10 )
        cmds.setAttr( '%s.input2Y' % self.prismScalerMD, 10 )
        cmds.setAttr( '%s.input2Z' % self.prismScalerMD, 10 )
        cmds.connectAttr( '%s.outputX' % self.prismScalerMD, '%s.sx' % self.prism[0] )
        cmds.connectAttr( '%s.outputY' % self.prismScalerMD, '%s.sy' % self.prism[0] )
        cmds.connectAttr( '%s.outputZ' % self.prismScalerMD, '%s.sz' % self.prism[0] )
        # FOV Setup
        self.focalMD= cmds.createNode( 'multiplyDivide', n= 'CAM_guides_to_FOV' )
        cmds.setAttr( '%s.operation' % self.focalMD, 2 )
        cmds.setAttr( '%s.input1X' % self.focalMD, 35 )
        cmds.connectAttr( '%s.focalLength' % self.camShape[0], '%s.input2X' % self.focalMD )
        cmds.connectAttr( '%s.outputX' % self.focalMD, '%s.sx' % self.guideGrp )
        cmds.connectAttr( '%s.outputX' % self.focalMD, '%s.sy' % self.guideGrp )
        # clipping Setup
        cmds.addAttr( self.selCam[0], ln='nearClip', at='float', hnv=1, min= 0 )
        cmds.setAttr( '%s.nearClip' % self.selCam[0], e=1, k=True )
        cmds.setAttr( '%s.nearClip' % self.selCam[0], 1 )
        cmds.addAttr( self.selCam[0], ln='farClip', at='float' )
        cmds.setAttr( '%s.farClip' % self.selCam[0], e=1, k=True)
        cmds.setAttr( '%s.farClip' % self.selCam[0], 1000000 )
        cmds.connectAttr( '%s.nearClip' % self.selCam[0], '%s.nearClipPlane' % self.camShape[0] )
        cmds.connectAttr( '%s.farClip' % self.selCam[0], '%s.farClipPlane' % self.camShape[0] )
        self.nearClipMD= cmds.createNode( 'multiplyDivide', n= 'CAM_clippingControl01' )
        cmds.setAttr( '%s.input2X' % self.nearClipMD, -1 )
        cmds.setAttr( '%s.input2Y' % self.nearClipMD, 1.51 )
        cmds.setAttr( '%s.input1Z' % self.nearClipMD, 1 )
        cmds.connectAttr( '%s.nearClip' % self.selCam[0], '%s.input1X' % self.nearClipMD )
        cmds.connectAttr( '%s.nearClip' % self.selCam[0], '%s.input1Y' % self.nearClipMD )
        cmds.connectAttr( '%s.outputX' % self.nearClipMD, '%s.tz' % self.clipGrp )
        self.nearClipPMA= cmds.createNode( 'plusMinusAverage', n= 'CAM_clippingControl02' )
        cmds.connectAttr( '%s.outputY' % self.nearClipMD, '%s.input1D[1]' % self.nearClipPMA )
        cmds.connectAttr( '%s.outputZ' % self.nearClipMD, '%s.input1D[0]' % self.nearClipPMA )
        cmds.connectAttr( '%s.output1D' % self.nearClipPMA, '%s.sx' % self.clipGrp )
        cmds.connectAttr( '%s.output1D' % self.nearClipPMA, '%s.sy' % self.clipGrp )
        cmds.connectAttr( '%s.output1D' % self.nearClipPMA, '%s.sz' % self.clipGrp )
        # AperTure Setup
        self.honMD01= cmds.createNode( 'multiplyDivide', n= 'horizontalApperture_MD01' )
        cmds.setAttr( '%s.operation' % self.honMD01, 2 )
        cmds.setAttr( '%s.input2X' % self.honMD01, 2 )
        self.honMD02= cmds.createNode( 'multiplyDivide', n= 'horizontalApperture_MD02' )
        cmds.setAttr( '%s.operation' % self.honMD02, 2 )
        cmds.setAttr( '%s.input2X' % self.honMD02, 0.843 )
        cmds.connectAttr( '%s.horizontalFilmAperture' % self.camShape[0], '%s.input1X' % self.honMD01 )
        cmds.connectAttr( '%s.outputX' % self.honMD01, '%s.input1X' % self.honMD02 )
        cmds.connectAttr( '%s.outputX' % self.honMD02, '%s.sx' % self.guideAlign )
        self.vertMD01=  cmds.createNode( 'multiplyDivide', n= 'verticalApperture_MD01' )
        cmds.setAttr( '%s.operation' % self.vertMD01, 2 )
        cmds.setAttr( '%s.input2X' % self.vertMD01, 0.945 )
        self.vertMD02= cmds.createNode( 'multiplyDivide', n= 'verticalApperture_MD02' )
        cmds.setAttr( '%s.operation' % self.vertMD02, 2 )
        cmds.setAttr( '%s.operation' % self.vertMD02, 1 )
        cmds.connectAttr( '%s.verticalFilmAperture' % self.camShape[0], '%s.input1X' % self.vertMD01 )
        cmds.connectAttr( '%s.outputX' % self.vertMD01, '%s.input1X' % self.vertMD02 )
        cmds.connectAttr( '%s.outputX' % self.vertMD02, '%s.sy' % self.guideAlign )
        # Counter Resolution Setup
        darMD= cmds.createNode(  'multiplyDivide', n= 'deviceAspectRatio_MD01' )
        cmds.setAttr( '%s.operation' % darMD, 2 )
        cmds.setAttr( '%s.input1X' % darMD, 1.5 )
        cmds.connectAttr( 'defaultResolution.deviceAspectRatio', '%s.input2X' % darMD )
        darCon= cmds.createNode( 'condition', n= 'deviceAspectRatio_CON01' )
        cmds.setAttr( '%s.operation' % darCon, 4 )
        cmds.setAttr( '%s.secondTerm' % darCon, 1.7 )
        cmds.setAttr( '%s.colorIfTrueG' % darCon, 1 )
        cmds.setAttr( '%s.colorIfFalseG' % darCon, 1.19 )
        cmds.setAttr( '%s.colorIfTrueR' % darCon, 1 )
        cmds.connectAttr( '%s.input2X' % darMD, '%s.firstTerm' % darCon )
        cmds.connectAttr( '%s.outputX' % darMD, '%s.colorIfTrueR' % darCon )
        cmds.connectAttr( '%s.outColorG' % darCon, '%s.sx' % self.filmGateB[0] )
        cmds.connectAttr( '%s.outColorR' % darCon, '%s.sy' % self.filmGateB[0] )
        #  Camera Scale Setup 
        cmds.addAttr( self.selCam[0], ln='matchGuide', at='float', hnv=1, min=-10, hxv=1, max= 10 )
        cmds.setAttr( '%s.matchGuide' % self.selCam[0], e=1, k=True )
        camScaleMD= cmds.createNode( 'multiplyDivide', n= 'cameraScaleCounter_MD01' )
        cmds.connectAttr( '%s.matchGuide' % self.selCam[0], '%s.input1X' % camScaleMD )
        cmds.setAttr( '%s.input2X' % camScaleMD, 1 )
        cmds.connectAttr( '%s.outputX' % camScaleMD, '%s.tz' % self.guideSdk )
        # Lock Attributes
        lockList= [ self.sceneInfoLoc[0], self.prism[0], self.tvGateGrp, self.clipGrp, self.guideGrp, self.guideAlign ]
        for each in lockList:
            cmds.setAttr( '%s.tx' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.ty' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.tz' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.rx' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.ry' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.rz' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.sx' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.sy' % each, l=1, k=1, cb=1 )
            cmds.setAttr( '%s.sz' % each, l=1, k=1, cb=1 )
        # Camera Label Group
        cmds.select( cl=1 )
        if cmds.objExists( 'CameraLabel_grp' ):
            cmds.select( 'CameraLabel_grp' )
            self.mainCamGrp= cmds.ls( sl=1 )
            cmds.parent( self.guideSpace, self.mainCamGrp )
        else:
            self.mainCamGrp= cmds.group( n= 'CameraLabel_grp', em=1 )
            cmds.parent( self.guideSpace, self.mainCamGrp )
        cmds.select( cl=1 )
        cmds.select( self.selCam )
        
        # Help Window
        cHelpWin= 'CamHUD Help Window'
    
        if cmds.window( cHelpWin, q=1, ex=True ):
            cmds.deleteUI( cHelpWin )
        
        if cmds.windowPref( cHelpWin, ex=True ):
            cmds.windowPref( cHelpWin, remove=True )
            
        cHelpWin= cmds.window( title= 'CamHUD v.1.0 Help', s=0, w= 400, h= 150 )
        cmds.frameLayout( 'User Guide', borderStyle= 'etchedOut', collapsable= 1, collapse=0  )
        form= cmds.formLayout()
        content= ('CamHUD is Setup when this window pop-up. '
                  + '\n\n'
                  + 'If CamHUD not showing up/matching with grey gate on playblast panel.Try the following steps.'
                  + '\n\n'
                  + '1. Change view port from Film Gate to Resolution Gate.'
                  + '\n\n'
                  + '2. Select playblast camera.'
                  + '\n\n'
                  + '3. Tweak the value of the Match Guide attribute until the CamHUD show up and match with the Resolution Gate.'
                  + '\n\n'
                  + '4. Call for help from rigger if the CamHUD still not showing up.'
                  + '\n\n'
                  + 'The Match Guide attributes is corresponding with value of Camera Scale( under cameraShape node. Open Attribute Editor to locate it. Under Focal Length. Default value is 1. )'
                  + '\n\n'
                  + 'Camera Scale= 0.5, Match Guide= -6'
                  + '\n\n'
                  + 'Camera Scale= 1, Match Guide= 0'
                  + '\n\n'
                  + 'Camera Scale= 2, Match Guide= 3'
                  + '\n\n'
                  + 'Camera Scale= 3, Match Guide= 4'
                  + '\n\n'
                  + 'Close This window if CamHUD is Set up properly. Thanks.')
                  
        cmds.scrollField( wordWrap= True, editable= False, text= content, w= 400, h= 460 )
        cmds.showWindow( cHelpWin )
        
if __name__ ==  '__main__' :
    abc= createCamHUD()
