import maya.mel as mel
import maya.cmds as cmds
import pymel.core as pm
import glob
import string

rootDir = cmds.workspace( q=True, rd=True )

def singleConvert():
    selectAllJoints()
    moveTimeData()

def batchConvert():
    fbxDir = rootDir + '/assets/inputs/'
    fbxs = glob.glob(fbxDir+'*.fbx')

    for fbx in fbxs:
        fbxName = cmds.file(fbxs[1], o = True, force=True)
        cmds.select('Tehau_Root')
        singleConvert()
        outName = fbxName.replace('inputs', 'outputs')
        cmds.FBXExport('-file', outName, '-s')
        cmds.delete('*_Root')



def moveTimeData():
    objs = cmds.ls(selection=True)
    for obj in objs:

        animAttributes = cmds.listAnimatable(obj);

        for attribute in animAttributes:

            numKeyframes = cmds.keyframe(attribute, query=True, keyframeCount=True)

            if (numKeyframes > 0):
                times = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), timeChange=True)
                cmds.keyframe(edit=True, relative=True, timeChange=-times[0])
                newTimes = cmds.keyframe(attribute, query=True, index=(0,numKeyframes), timeChange=True)


def selectAllJoints():
    root = cmds.ls(selection=True)[0]
    joints = cmds.listRelatives(root, ad=True, type='joint')
    if cmds.objectType(root) is 'joint':
        joints.append(root)
    cmds.select(joints)

batchConvert()
