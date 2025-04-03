from struct import unpack, pack, error
import bpy
import os
import mathutils
import math
        

def ani_importV2(f):
    ob = bpy.context.object
    bpy.context.scene.render.fps = 30
    bpy.context.scene.render.fps_base = 1
    bpy.context.scene.unit_settings.system_rotation = "RADIANS"

    for pbone in ob.pose.bones:
        pbone.rotation_mode = "XYZ"

    bones_=[]
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    boneid=-1
    boneid1=0
    keybool=[]
    keybool2=[]
    keybool3=[]
    keybool4=[]
    keybool5=[]
    keybool6=[]
    keybool7=[]
    keybool8=[]
    keybool9=[]
    keyb=[]
    keyboolIndex=-1
    keyM = []
    idxA = 0
    idxB = 0
    version = unpack("<I", f.read(4))[0]
    if version == 1:
        EntrySize = unpack("<I", f.read(4))[0] & 0xFFFF
        EntrySize1 = unpack("<I", f.read(4))[0] & 0xFFFF
        BoneCount1 = unpack("<I", f.read(4))[0]
        BoneCount2 = unpack("<I", f.read(4))[0]
        EntrySize2 = unpack("<I", f.read(4))[0] & 0xFFFF
        EntrySize3 = unpack("<I", f.read(4))[0] & 0xFFFF
        EntrySize4 = unpack("<I", f.read(4))[0] & 0xFFFF
        Type1 = unpack("<I", f.read(4))[0]
    elif version == 2:
        EntrySize = unpack("<I", f.read(4))[0] & 0xFFFF
        EntrySize1 = unpack("<I", f.read(4))[0] & 0xFFFF
        FloatCount = unpack("<f", f.read(4))[0]
        BoneCount = unpack("<H", f.read(2))[0]
        offsetCount = unpack("<H", f.read(2))[0]
        Type1 = unpack("<I", f.read(4))[0]
        EntrySize2 = unpack("<I", f.read(4))[0] & 0xFFFF
        EntrySize3 = unpack("<I", f.read(4))[0] & 0xFFFF
        EntrySize4 = unpack("<I", f.read(4))[0] & 0xFFFF
        
        bpy.context.scene.frame_end = int(FloatCount)
        bpy.context.scene.frame_current = 1
        bpy.context.scene.frame_start = 1

        if BoneCount == 0:
            pass

        elif BoneCount:
            for i in range(BoneCount):
                Size1 = unpack("<H", f.read(2))[0]
                id1 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid1 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix1 = unpack("<f", f.read(4))[0]
                Size2 = unpack("<H", f.read(2))[0]
                id2 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid2 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix2 = unpack("<f", f.read(4))[0]
                Size3 = unpack("<H", f.read(2))[0]
                id3 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid3 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix3 = unpack("<f", f.read(4))[0]
                Size4 = unpack("<H", f.read(2))[0]
                id4 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid4 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix4 = unpack("<f", f.read(4))[0]
                Size5 = unpack("<H", f.read(2))[0]
                id5 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid5 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix5 = unpack("<f", f.read(4))[0]
                Size6 = unpack("<H", f.read(2))[0]
                id6 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid6 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix6 = unpack("<f", f.read(4))[0]
                Size7 = unpack("<H", f.read(2))[0]
                id7 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid7 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix7 = unpack("<f", f.read(4))[0]
                Size8 = unpack("<H", f.read(2))[0]
                id8 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid8 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix8 = unpack("<f", f.read(4))[0]
                Size9 = unpack("<H", f.read(2))[0]
                id9 = unpack("<H", f.read(2))[0]
                f.seek(-4,1)
                sizeid9 = unpack("<I", f.read(4))[0]
                f.seek(-4,1)
                SclMatrix9 = unpack("<f", f.read(4))[0]
                keyM.append([Size1,id1,Size2,id2,Size3,id3,Size4,id4,Size5,id5,Size6,id6,Size7,id7,Size8,id8,Size9,id9])
            for k in range(BoneCount):
                booleanOnOffKeys1Posx = unpack("B", f.read(1))[0]
                booleanOnOffKeys2Posy = unpack("B", f.read(1))[0]
                booleanOnOffKeys3Posz = unpack("B", f.read(1))[0]
                booleanOnOffKeys4Rotx = unpack("B", f.read(1))[0]
                booleanOnOffKeys5Roty = unpack("B", f.read(1))[0]
                booleanOnOffKeys6Rotz = unpack("B", f.read(1))[0]
                booleanOnOffKeys7Sclx = unpack("B", f.read(1))[0]
                booleanOnOffKeys8Scly = unpack("B", f.read(1))[0]
                booleanOnOffKeys9Sclz = unpack("B", f.read(1))[0]
                keybool.append([booleanOnOffKeys1Posx])
                keybool2.append([booleanOnOffKeys2Posy])
                keybool3.append([booleanOnOffKeys3Posz])
                keybool4.append([booleanOnOffKeys4Rotx])
                keybool5.append([booleanOnOffKeys5Roty])
                keybool6.append([booleanOnOffKeys6Rotz])
                keybool7.append([booleanOnOffKeys7Sclx])
                keybool8.append([booleanOnOffKeys8Scly])
                keybool9.append([booleanOnOffKeys9Sclz])

            for i in range(BoneCount):
                boneiddd = unpack("B", f.read(1))[0]

            for i, bidx in enumerate(keyM):
                if Type1 == 15:
                    if bidx[1] == 7563:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))

                    elif bidx[3] == 7563:
                        f.seek(bidx[2]-32,0)
                        EntrySizeD = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeE = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeF = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeD:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posy = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[1] = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1,frame=int(FloatCount))

                    elif bidx[5] == 7563:
                        f.seek(bidx[4]-32,0)
                        EntrySizeG = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeH = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeI = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeG:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posz = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[2] = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2,frame=int(FloatCount))

                    elif bidx[7] == 7563:
                        f.seek(bidx[6]-32,0)
                        EntrySizeJ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeK = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeL = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeJ:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotx = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[0] = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0,frame=int(FloatCount))

                    elif bidx[9] == 7563:
                        f.seek(bidx[8]-32,0)
                        EntrySizeM = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeN = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeO = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeM:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            roty = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[1] = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1,frame=int(FloatCount))

                    elif bidx[11] == 7563:
                        f.seek(bidx[10]-32,0)
                        EntrySizeP = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeQ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeR = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeP:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotz = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[2] = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2,frame=int(FloatCount))

                    elif bidx[13] == 7563:
                        f.seek(bidx[12]-32,0)
                        EntrySizeS = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeT = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeU = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeS:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[0] = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0,frame=int(FloatCount))

                    elif bidx[15] == 7563:
                        f.seek(bidx[14]-32,0)
                        EntrySizeV = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeW = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeX = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeV:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            scly = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[1] = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1,frame=int(FloatCount))

                    elif bidx[17] == 7563:
                        f.seek(bidx[16]-32,0)
                        EntrySizeY = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeY:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[2] = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2,frame=int(FloatCount))

                elif Type1 == 7:
                    if bidx[1] == 10081:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))
                        
                        
                        
                        
                elif Type1 == 5:
                    if bidx[1] == 7980 or bidx[1] == 7308 or bidx[1] == 8796 or bidx[1] == 9127:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))
                    elif bidx[3] == 7980 or bidx[3] == 7308 or bidx[3] == 8796 or bidx[3] == 9127:
                        f.seek(bidx[2]-32,0)
                        EntrySizeD = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeE = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeF = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeD:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posy = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[1] = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1,frame=int(FloatCount))

                    elif bidx[5] == 7980 or bidx[5] == 7308 or bidx[5] == 8796 or bidx[5] == 9127:
                        f.seek(bidx[4]-32,0)
                        EntrySizeG = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeH = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeI = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeG:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posz = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[2] = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2,frame=int(FloatCount))

                    elif bidx[7] == 7980 or bidx[7] == 7308 or bidx[7] == 8796 or bidx[7] == 9127:
                        f.seek(bidx[6]-32,0)
                        EntrySizeJ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeK = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeL = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeJ:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotx = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[0] = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0,frame=int(FloatCount))

                    elif bidx[9] == 7980 or bidx[9] == 7308 or bidx[9] == 8796 or bidx[9] == 9127:
                        f.seek(bidx[8]-32,0)
                        EntrySizeM = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeN = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeO = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeM:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            roty = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[1] = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1,frame=int(FloatCount))

                    elif bidx[11] == 7980 or bidx[11] == 7308 or bidx[11] == 8796 or bidx[11] == 9127:
                        f.seek(bidx[10]-32,0)
                        EntrySizeP = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeQ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeR = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeP:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotz = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[2] = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2,frame=int(FloatCount))

                    elif bidx[13] == 7980 or bidx[13] == 7308 or bidx[13] == 8796 or bidx[13] == 9127:
                        f.seek(bidx[12]-32,0)
                        EntrySizeS = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeT = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeU = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeS:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[0] = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0,frame=int(FloatCount))

                    elif bidx[15] == 7980 or bidx[15] == 7308 or bidx[15] == 8796 or bidx[15] == 9127:
                        f.seek(bidx[14]-32,0)
                        EntrySizeV = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeW = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeX = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeV:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            scly = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[1] = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1,frame=int(FloatCount))

                    elif bidx[17] == 7980 or bidx[17] == 7308 or bidx[17] == 8796 or bidx[17] == 9127:
                        f.seek(bidx[16]-32,0)
                        EntrySizeY = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeY:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[2] = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2,frame=int(FloatCount))

                elif Type1 == 4:
                    if bidx[1] == 8381 or bidx[1] == 7959 or bidx[1] == 12647:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))

                    elif bidx[3] == 8381 or bidx[3] == 7959 or bidx[3] == 12647:
                        f.seek(bidx[2]-32,0)
                        EntrySizeD = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeE = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeF = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeD:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posy = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[1] = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1,frame=int(FloatCount))

                    elif bidx[5] == 8381 or bidx[5] == 7959 or bidx[5] == 12647:
                        f.seek(bidx[4]-32,0)
                        EntrySizeG = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeH = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeI = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeG:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posz = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[2] = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2,frame=int(FloatCount))

                    elif bidx[7] == 8381 or bidx[7] == 7959 or bidx[7] == 12647:
                        f.seek(bidx[6]-32,0)
                        EntrySizeJ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeK = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeL = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeJ:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotx = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[0] = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0,frame=int(FloatCount))

                    elif bidx[9] == 8381 or bidx[9] == 7959 or bidx[9] == 12647:
                        f.seek(bidx[8]-32,0)
                        EntrySizeM = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeN = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeO = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeM:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            roty = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[1] = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1,frame=int(FloatCount))

                    elif bidx[11] == 8381 or bidx[11] == 7959 or bidx[11] == 12647:
                        f.seek(bidx[10]-32,0)
                        EntrySizeP = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeQ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeR = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeP:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotz = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[2] = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2,frame=int(FloatCount))

                    elif bidx[13] == 8391 or bidx[13] == 7959 or bidx[13] == 12647:
                        f.seek(bidx[12]-32,0)
                        EntrySizeS = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeT = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeU = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeS:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[0] = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0,frame=int(FloatCount))

                    elif bidx[15] == 8391 or bidx[15] == 7959 or bidx[15] == 12647:
                        f.seek(bidx[14]-32,0)
                        EntrySizeV = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeW = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeX = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeV:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            scly = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[1] = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1,frame=int(FloatCount))

                    elif bidx[17] == 8391 or bidx[17] == 7959 or bidx[17] == 12647:
                        f.seek(bidx[16]-32,0)
                        EntrySizeY = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeY:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[2] = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2,frame=int(FloatCount))
                            
                elif Type1 == 3:
                    if bidx[1] == 9192 or bidx[1] == 9469 or bidx[1] == 10324 or bidx[1] == 8003 or bidx[1] == 10239 or bidx[1] == 8924 or bidx[1] == 9890 or bidx[1] == 8286 or bidx[1] == 8315:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if keybool[0] != [1]:
                                if FloatCount==1:
                                    boneid+=1
                            elif keybool[1] != [1]:
                                if FloatCount==1:
                                    boneid1+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))
                    elif bidx[3] == 9192 or bidx[3] == 9469  or bidx[3] == 10324 or bidx[3] == 8003 or bidx[3] == 10239 or bidx[3] == 8924 or bidx[3] == 9890 or bidx[3] == 8286 or bidx[3] == 8315:
                        f.seek(bidx[2]-32,0)
                        EntrySizeD = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeE = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeF = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeD:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posy = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if keybool2[0] == [1]:
                                if FloatCount==1:
                                    boneid+=1
                            ob.pose.bones[boneid].location[1] = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1,frame=int(FloatCount))
                    elif bidx[5] == 9192 or bidx[5] == 9469 or bidx[5] == 10324 or bidx[5] == 8003 or bidx[5] == 10239 or bidx[5] == 8924 or bidx[5] == 9890 or bidx[5] == 8286 or bidx[5] == 8315:
                        f.seek(bidx[4]-32,0)
                        EntrySizeG = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeH = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeI = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeG:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posz = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[2] = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2,frame=int(FloatCount))
                    elif bidx[7] == 9192 or bidx[7] == 9469 or bidx[7] == 10324 or bidx[7] == 8003 or bidx[7] == 10239 or bidx[7] == 8924 or bidx[7] == 9890 or bidx[7] == 8286 or bidx[7] == 8315:
                        f.seek(bidx[6]-32,0)
                        EntrySizeJ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeK = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeL = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeJ:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotx = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[0] = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0,frame=int(FloatCount))
                    elif bidx[9] == 9192 or bidx[9] == 9469 or bidx[9] == 10324 or bidx[9] == 8003 or bidx[9] == 10239 or bidx[9] == 8924 or bidx[9] == 9890 or bidx[9] == 8286 or bidx[9] == 8315:
                        f.seek(bidx[8]-32,0)
                        EntrySizeM = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeN = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeO = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeM:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            roty = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[1] = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1,frame=int(FloatCount))
                    elif bidx[11] == 9192 or bidx[11] == 9469 or bidx[11] == 10324 or bidx[11] == 8003 or bidx[11] == 10239 or bidx[11] == 8924 or bidx[11] == 9890 or bidx[11] == 8286 or bidx[11] == 8315:
                        f.seek(bidx[10]-32,0)
                        EntrySizeP = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeQ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeR = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeP:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotz = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[2] = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2,frame=int(FloatCount))
                    elif bidx[13] == 9192 or bidx[13] == 9469 or bidx[13] == 10324 or bidx[13] == 8003 or bidx[13] == 10239 or bidx[13] == 8924 or bidx[13] == 9890 or bidx[13] == 8286 or bidx[13] == 8315:
                        f.seek(bidx[12]-32,0)
                        EntrySizeS = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeT = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeU = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeS:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[0] = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0,frame=int(FloatCount))
                    elif bidx[15] == 9192 or bidx[15] == 9469 or bidx[15] == 10324 or bidx[15] == 8003 or bidx[15] == 10239 or bidx[15] == 8924 or bidx[15] == 9890 or bidx[15] == 8286 or bidx[15] == 8315:
                        f.seek(bidx[14]-32,0)
                        EntrySizeV = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeW = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeX = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeV:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            scly = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[1] = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1,frame=int(FloatCount))
                    elif bidx[17] == 9192 or bidx[17] == 9469 or bidx[17] == 10324 or bidx[17] == 8003 or bidx[17] == 10239 or bidx[17] == 8924 or bidx[17] == 9890 or bidx[17] == 8286 or bidx[17] == 8315:
                        f.seek(bidx[16]-32,0)
                        EntrySizeY = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeY:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[2] = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2,frame=int(FloatCount))

                elif Type1 == 2:
                    if bidx[1] == 7655 or bidx[1] == 10239 or bidx[1] == 9890 or bidx[1] == 7530 or bidx[1] == 7584 or bidx[1] == 9143 or bidx[1] == 9831 or bidx[1] == 12647:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))

                    elif bidx[3] == 7655 or bidx[3] == 10239 or bidx[3] == 9890 or bidx[3] == 7530 or bidx[3] == 7584 or bidx[3] == 9143 or bidx[3] == 9831 or bidx[3] == 12647:
                        f.seek(bidx[2]-32,0)
                        EntrySizeD = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeE = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeF = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeD:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posy = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[1] = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1,frame=int(FloatCount))

                    elif bidx[5] == 7655 or bidx[5] == 10239 or bidx[5] == 9890 or bidx[5] == 7530 or bidx[5] == 7584 or bidx[5] == 9143 or bidx[5] == 9831 or bidx[5] == 12647:
                        f.seek(bidx[4]-32,0)
                        EntrySizeG = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeH = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeI = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeG:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posz = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[2] = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2,frame=int(FloatCount))

                    elif bidx[7] == 7655 or bidx[7] == 10239 or bidx[7] == 9890 or bidx[7] == 7530 or bidx[7] == 7584 or bidx[7] == 9143 or bidx[7] == 9831 or bidx[7] == 12647:
                        f.seek(bidx[6]-32,0)
                        EntrySizeJ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeK = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeL = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeJ:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotx = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[0] = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0,frame=int(FloatCount))

                    elif bidx[9] == 7655 or bidx[9] == 10239 or bidx[9] == 9890 or bidx[9] == 7530 or bidx[9] == 7584 or bidx[9] == 9143 or bidx[9] == 9831 or bidx[9] == 12647:
                        f.seek(bidx[8]-32,0)
                        EntrySizeM = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeN = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeO = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeM:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            roty = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[1] = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1,frame=int(FloatCount))

                    elif bidx[11] == 7655 or bidx[11] == 10239 or bidx[11] == 9890 or bidx[11] == 7530 or bidx[11] == 7584 or bidx[11] == 9143 or bidx[11] == 9831 or bidx[11] == 12647:
                        f.seek(bidx[10]-32,0)
                        EntrySizeP = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeQ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeR = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeP:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotz = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[2] = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2,frame=int(FloatCount))

                    elif bidx[13] == 7655 or bidx[13] == 10239 or bidx[13] == 9890 or bidx[13] == 7530 or bidx[13] == 7584 or bidx[13] == 9143 or bidx[13] == 9831 or bidx[13] == 12647:
                        f.seek(bidx[12]-32,0)
                        EntrySizeS = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeT = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeU = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeS:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[0] = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0,frame=int(FloatCount))

                    elif bidx[15] == 7655 or bidx[15] == 10239 or bidx[15] == 9890 or bidx[15] == 7530 or bidx[15] == 7584 or bidx[15] == 9143 or bidx[15] == 9831 or bidx[15] == 12647:
                        f.seek(bidx[14]-32,0)
                        EntrySizeV = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeW = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeX = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeV:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            scly = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[1] = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1,frame=int(FloatCount))

                    elif bidx[17] == 7655 or bidx[17] == 10239 or bidx[17] == 9890 or bidx[17] == 7530 or bidx[17] == 7584 or bidx[17] == 9143 or bidx[17] == 9831 or bidx[17] == 12647:
                        f.seek(bidx[16]-32,0)
                        EntrySizeY = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeY:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[2] = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2,frame=int(FloatCount))
                elif Type1 == 1:
                    if bidx[1] == 8994 or bidx[1] == 9442 or bidx[1] == 8871 or bidx[1] == 9440 or bidx[1] == 9450 or bidx[1] == 8796 or bidx[1] == 9417 or bidx[1] == 9335 or bidx[1] == 14507 or bidx[1] == 6207 or bidx[1] == 8316 or bidx[1] == 9457 or bidx[1] == 10280:
                        f.seek(bidx[0]-32,0)
                        EntrySizeA = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeB = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeC = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeA:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posx = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[0] = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0,frame=int(FloatCount))
                    elif bidx[3] == 8994 or bidx[3] == 9442 or bidx[3] == 8871 or bidx[3] == 9440 or bidx[3] == 9450 or bidx[3] == 8796 or bidx[3] == 9417 or bidx[3] == 9335 or bidx[3] == 14507 or bidx[3] == 6207 or bidx[3] == 8316 or bidx[3] == 9457 or bidx[3] == 10280:
                        f.seek(bidx[2]-32,0)
                        EntrySizeD = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeE = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeF = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeD:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posy = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[1] = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1,frame=int(FloatCount))
                    elif bidx[5] == 8994 or bidx[5] == 9442 or bidx[5] == 8871 or bidx[5] == 9440 or bidx[5] == 9450 or bidx[5] == 8796 or bidx[5] == 9417 or bidx[5] == 9335 or bidx[5] == 14507 or bidx[5] == 6207 or bidx[5] == 8316 or bidx[5] == 9457 or bidx[5] == 10280:
                        f.seek(bidx[4]-32,0)
                        EntrySizeG = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeH = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeI = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeG:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            posz = unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location[2] = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2,frame=int(FloatCount))
                    elif bidx[7] == 8994 or bidx[7] == 9442 or bidx[7] == 8871 or bidx[7] == 9440 or bidx[7] == 9450 or bidx[7] == 8796 or bidx[7] == 9417 or bidx[7] == 9335 or bidx[7] == 14507 or bidx[7] == 6207 or bidx[7] == 8316 or bidx[7] == 9457 or bidx[7] == 10280:
                        f.seek(bidx[6]-32,0)
                        EntrySizeJ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeK = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeL = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeJ:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotx = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[0] = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0,frame=int(FloatCount))
                    elif bidx[9] == 8994 or bidx[9] == 9442 or bidx[9] == 8871 or bidx[9] == 9440 or bidx[9] == 9450 or bidx[9] == 8796 or bidx[9] == 9417 or bidx[9] == 9335 or bidx[9] == 14507 or bidx[9] == 6207 or bidx[9] == 8316 or bidx[9] == 9457 or bidx[9] == 10280:
                        f.seek(bidx[8]-32,0)
                        EntrySizeM = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeN = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeO = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeM:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            roty = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[1] = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1,frame=int(FloatCount))
                    elif bidx[11] == 8994 or bidx[11] == 9442 or bidx[11] == 8871 or bidx[11] == 9440 or bidx[11] == 9450 or bidx[11] == 8796 or bidx[11] == 9417 or bidx[11] == 9335 or bidx[11] == 14507 or bidx[11] == 6207 or bidx[11] == 8316 or bidx[11] == 9457 or bidx[11] == 10280:
                        f.seek(bidx[10]-32,0)
                        EntrySizeP = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeQ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeR = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeP:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            rotz = -unpack("<f", f.read(4))[0] / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler[2] = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2,frame=int(FloatCount))
                    elif bidx[13] == 8994 or bidx[13] == 9442 or bidx[13] == 8871 or bidx[13] == 9440 or bidx[13] == 9450 or bidx[13] == 8796 or bidx[13] == 9417 or bidx[13] == 9335 or bidx[13] == 14507 or bidx[13] == 6207 or bidx[13] == 8316 or bidx[13] == 9457 or bidx[13] == 10280:
                        f.seek(bidx[12]-32,0)
                        EntrySizeS = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeT = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeU = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeS:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclx = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[0] = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0,frame=int(FloatCount))
                    elif bidx[15] == 8994 or bidx[15] == 9442 or bidx[15] == 8871 or bidx[15] == 9440 or bidx[15] == 9450 or bidx[15] == 8796 or bidx[15] == 9417 or bidx[15] == 9335 or bidx[15] == 14507 or bidx[15] == 6207 or bidx[15] == 8316 or bidx[15] == 9457 or bidx[15] == 10280:
                        f.seek(bidx[14]-32,0)
                        EntrySizeV = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeW = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeX = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeV:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            scly = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[1] = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1,frame=int(FloatCount))
                    elif bidx[17] == 8994 or bidx[17] == 9442 or bidx[17] == 8871 or bidx[17] == 9440 or bidx[17] == 9450 or bidx[17] == 8796 or bidx[17] == 9417 or bidx[17] == 9335 or bidx[17] == 14507 or bidx[17] == 6207 or bidx[17] == 8316 or bidx[17] == 9457 or bidx[17] == 10280:
                        f.seek(bidx[16]-32,0)
                        EntrySizeY = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                        f.seek(2,1)
                        while f.tell() < EntrySizeY:
                            FloatCount = unpack("<f", f.read(4))[0]
                            framerate = unpack("<f", f.read(4))[0]
                            sclz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].scale[2] = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2,frame=int(FloatCount))




def ani_exportV2_all_move_non_parser(f):
    pass
                
                

            
            
            


                
    
def ani_importer_read(filepath):
    with open(filepath,"rb") as f:
        ani_importV2(f)

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        ani_exportV2_all_move_non_parser(f)
