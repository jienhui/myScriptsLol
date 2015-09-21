import maya.cmds as cmds

# Get Deformers Lists
deformersInput= cmds.ls( type= ("nonLinear", "ffd", "wrap", "wire", "cluster", "sculpt", "softMod", "jiggle", "skinCluster") )
deformers= []
deformSets= []
for each in deformersInput:
    xform= cmds.deformer( each, q=1, dt=1)[0]
    deformers.append( xform )
    set= cmds.listConnections( each, type= 'objectSet' )[0]
    deformSets.append( set )

# Get new name to Deformer Input
renameItem= []
renameSet= []
newInput= []
for each in deformersInput :
    digit= each[-1].isdigit()
    if digit == True:
        renameItem.append(each)
    else:
        pass
        
for each in deformSets :
    underscore= each.find('_')
    if underscore == -1 :
        renameSet.append(each)
    else:
        pass
        
for each in renameItem:
    name= each.split()[0]
    newName= ''.join(i for i in name if not i.isdigit())
    newInput.append(newName)

sourceList=[]    
for each in renameSet:
    source= cmds.listConnections( each, s=1  )
    xform= cmds.ls( source, typ='transform' )[0]
    sourceList.append( xform )

# Rename Deformers Input
if len(renameItem) > 0 :
    for i, each in enumerate( renameItem ):
        newDeformersInput= cmds.rename( each, '%s_%s' % (sourceList[i], newInput[i] ) )
else:
    cmds.warning( 'All Inputs Have Correct Name!!' )
# Rename Deformers Set
if len(renameSet) > 0 :
    for i, each in enumerate(renameSet):
        cmds.rename( each, '%s_%sSet' % ( sourceList[i], newInput[i] ) )
else:
    cmds.warning( 'All Sets Have Correct Name!!' )
