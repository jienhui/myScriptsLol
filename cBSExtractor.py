# Duplicate Blendshapes Tools
import maya.cmds as cmds
import maya.mel as mel

########################################################################
sourceMesh= "body_bln"        # <----- input source geometry here
targetMesh= "body_geo_new"    # <----- input new geometry here
########################################################################

# Collecting Data
try:
    skinNode= cmds.ls( cmds.listHistory( sourceMesh ), typ= "skinCluster" )[0]
    cmds.setAttr( "%s.envelope" % skinNode, 0 )
except IndexError:
    pass
try:
    bsNode= cmds.ls( cmds.listHistory( sourceMesh ), typ= "blendShape" )[0]
    bsList= cmds.listAttr( "%s.w" % bsNode, m=1 )
except IndexError:
    cmds.warning( "No blendshape node in %s!" % sourceMesh )

# Get Inbetween Data
bsDict= {}
bsValue= []
for each in range(len(bsList)):
    iTi = '.inputTargetItem'
    iTg = '%s.inputTarget[0]' % bsNode
    iTgGr = '.inputTargetGroup[%s]' % each
    iTi = '.inputTargetItem'
    item= cmds.getAttr( iTg + iTgGr + iTi, mi=1 )
    value= []
    for v in item:
        if str(v) == "6000":
            nv= 1.0
            value.append(nv)
        else:
            strList= list(str(v))
            strList[0] = "0."
            sNv= "".join(strList)
            nv= float(sNv)
            value.append( nv )
    bsDict[bsList[each]]= value
    bsValue.append(value)

# Break Blendshapes List Connections
connectionList= []

for each in bsList:
    connect= cmds.listConnections( "%s.%s" % (bsNode, each), s=1, p=1 )
    if connect is None:
        connectionList.append( connect )
    else:
        connectionList.append( connect[0] )
    #mel.eval( 'source generateChannelMenu' )
    #mel.eval( 'CBdeleteConnection "%s.%s";' % ( bsNode, each ) )
for i,each in enumerate(bsList):
    try:
        cmds.disconnectAttr( connectionList[i], "%s.%s" % (bsNode, each) )
        cmds.setAttr( "%s.%s" % (bsNode, each), 0 )
    except RuntimeError:
        cmds.setAttr("%s.%s" % (bsNode, each), l=0)
        if connectionList[i] is None:
            pass
        else:
            cmds.disconnectAttr( connectionList[i], "%s.%s" % (bsNode, each) )
        cmds.setAttr( "%s.%s" % (bsNode, each), 0 )  

# Create Temp Wrapper
try:
    lockAttr= cmds.listAttr( targetMesh, l=1 )
    for each in lockAttr:
        cmds.setAttr( "%s.%s" % (targetMesh, each), l=0 )
except TypeError:
    pass
   
wrapper= cmds.duplicate( targetMesh, n= "wrapper" )
cmds.parent( wrapper, w=1 )
cmds.select( cl=1 )
cmds.select( wrapper, sourceMesh, add=1 )
cmds.CreateWrap()

# Duplicate Blendshape From New Mesh
newBS= cmds.group( n= "NEW_BS_GRP", em=1 )

for i, each in enumerate( bsList ):
    if len(bsValue[i]) > 1:
        for n in bsValue[i]:
            cmds.setAttr( "%s.%s" % (bsNode, each), n )
            dup= cmds.duplicate( wrapper, n= "%s_%s" % ( each, n ) )
            cmds.parent( dup, newBS )
            cmds.setAttr( "%s.%s" % (bsNode, each), 0 )
            cmds.select( cl=1 )
    else:
        cmds.setAttr( "%s.%s" % (bsNode, each), float(bsValue[i][0]) )
        dup= cmds.duplicate( wrapper, n= "%s_%s" % ( each, float(bsValue[i][0]) ) )
        cmds.parent( dup, newBS )
        cmds.setAttr( "%s.%s" % (bsNode, each), 0 )
        cmds.select( cl=1 )

cmds.delete( wrapper )
cmds.sets( newBS, e=1, forceElement= 'initialShadingGroup' )
cmds.select( newBS )

print "All Blendshapes Extract Successfully! Please Grab them in %s!" % newBS ,
