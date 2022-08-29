import maya.cmds as cmds

def moveTimeData():
    objs = cmds.ls(selection=True)
    for obj in objs:

        animAttributes = cmds.listAnimatable(obj);

        for attribute in animAttributes:

            numKeyframes = cmds.keyframe(attribute, query=True, keyframeCount=True)

            if (numKeyframes > 0):
                times = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), timeChange=True)
                cmds.keyframe(edit=True, relative=True, timeChange=-times[0])

                
def selectAllJoints():
    root = cmds.ls(selection=True)[0]
    joints = cmds.listRelatives(root, ad=True, type='joint')
    if cmds.objectType(root) is 'joint':
        joints.append(root)
    cmds.select(joints)

selectAllJoints()
moveTimeData()
