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

    bones_1=[]
    bones_2=[]
    bones_3=[]
    bones_4=[]
    bones_5=[]
    bones_6=[]
    bones_7=[]
    bones_8=[]
    bones_9=[]

    keyframes_=[]
    bones_=[]
    f.seek(0)
    Chunk = f.read()
    f.seek(0)
    boneid=-1
    boneid1=1
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
                booleanOnOffKeys1Posx = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys2Posy = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys3Posz = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys4Rotx = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys5Roty = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys6Rotz = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys7Sclx = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys8Scly = unpack("B", f.read(1))[0]==True
                booleanOnOffKeys9Sclz = unpack("B", f.read(1))[0]==True
                keybool.append([booleanOnOffKeys1Posx])
                keybool2.append([booleanOnOffKeys2Posy])
                keybool3.append([booleanOnOffKeys3Posz])
                keybool4.append([booleanOnOffKeys4Rotx])
                keybool5.append([booleanOnOffKeys5Roty])
                keybool6.append([booleanOnOffKeys6Rotz])
                keybool7.append([booleanOnOffKeys7Sclx])
                keybool8.append([booleanOnOffKeys8Scly])
                keybool9.append([booleanOnOffKeys9Sclz])
                boneid1+=1
                if booleanOnOffKeys1Posx > 0:
                    bones_1.append(k+k+booleanOnOffKeys1Posx-booleanOnOffKeys1Posx-1+boneid1-k-k-1)
                if booleanOnOffKeys2Posy > 0:
                    bones_2.append(k+k+booleanOnOffKeys2Posy-booleanOnOffKeys2Posy-1+boneid1-k-k-1)
                if booleanOnOffKeys3Posz > 0:
                    bones_3.append(k+k+booleanOnOffKeys3Posz-booleanOnOffKeys3Posz-1+boneid1-k-k-1)
                if booleanOnOffKeys4Rotx > 0:
                    bones_4.append(k+k+booleanOnOffKeys4Rotx-booleanOnOffKeys4Rotx-1+boneid1-k-k-1)
                if booleanOnOffKeys5Roty > 0:
                    bones_5.append(k+k+booleanOnOffKeys5Roty-booleanOnOffKeys5Roty-1+boneid1-k-k-1)
                if booleanOnOffKeys6Rotz > 0:
                    bones_6.append(k+k+booleanOnOffKeys6Rotz-booleanOnOffKeys6Rotz-1+boneid1-k-k-1)
                if booleanOnOffKeys7Sclx > 0:
                    bones_7.append(k+k+booleanOnOffKeys7Sclx-booleanOnOffKeys7Sclx-1+boneid1-k-k-1)
                if booleanOnOffKeys8Scly > 0:
                    bones_8.append(k+k+booleanOnOffKeys8Scly-booleanOnOffKeys8Scly-1+boneid1-k-k-1)
                if booleanOnOffKeys9Sclz > 0:
                    bones_9.append(k+k+booleanOnOffKeys9Sclz-booleanOnOffKeys9Sclz-1+boneid1-k-k-1)
                """boneid+=1
                if booleanOnOffKeys2Posy > 0:
                    bones_.append(k+k+booleanOnOffKeys2Posy-booleanOnOffKeys2Posy-1+boneid-k-k-1)
                boneid skips it to get the next boneid
                this will be after alpha release or finishing the id
                boneid=1
                0,2,3,6
                0,1,2,6
                """

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
                            posx = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))

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
                            posy = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

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
                            posz = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))

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
                            rotx = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))

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
                            roty = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))

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
                            rotz = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))

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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))

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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))

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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))

                elif Type1 == 8:
                    if bidx[1] == 7749:
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
                            posx = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))
                    elif bidx[3] == 7749:
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
                            posy = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

                    elif bidx[5] == 7749:
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
                            posz = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))

                    elif bidx[7] == 7749:
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
                            rotx = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))

                    elif bidx[9] == 7749:
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
                            roty = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))

                    elif bidx[11] == 7749:
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
                            rotz = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))

                    elif bidx[13] == 7749:
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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))

                    elif bidx[15] == 7749:
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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))

                    elif bidx[17] == 7749:
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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))
                        
                        

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
                            posx = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))

                    elif bidx[3] == 10081:
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
                            posy = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

                    elif bidx[5] == 10081:
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
                            posz = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))

                    elif bidx[7] == 10081:
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
                            rotx = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))

                    elif bidx[9] == 10081:
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
                            roty = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))

                    elif bidx[11] == 10081:
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
                            rotz = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))

                    elif bidx[13] == 10081:
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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))

                    elif bidx[15] == 10081:
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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))

                    elif bidx[17] == 10081:
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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))
                        
                        
                        
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
                            posx = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))
                            
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
                            posy = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

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
                            posz = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))

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
                            rotx = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))

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
                            roty = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))

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
                            rotz = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))

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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))

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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))

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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))

                elif Type1 == 4:
                    if bidx[1] == 8381 or bidx[1] == 7959 or bidx[1] == 12647 or bidx[1] == 7633 or bidx[1] == 7816 or bidx[1] == 8020 or bidx[1] == 7729 or bidx[1] == 7980 or bidx[1] == 8034 or bidx[1] == 5365 or bidx[1] == 7563:
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
                            posx = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))

                    elif bidx[3] == 8381 or bidx[3] == 7959 or bidx[3] == 12647 or bidx[3] == 7633 or bidx[3] == 7816 or bidx[3] == 8020 or bidx[3] == 7729 or bidx[3] == 7980 or bidx[3] == 8034 or bidx[3] == 5365 or bidx[3] == 7563:
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
                            posy = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

                    elif bidx[5] == 8381 or bidx[5] == 7959 or bidx[5] == 12647 or bidx[5] == 7633 or bidx[5] == 7816 or bidx[5] == 8020 or bidx[5] == 7729 or bidx[5] == 7980 or bidx[5] == 8034 or bidx[5] == 5365 or bidx[5] == 7563:
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
                            posz = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))

                    elif bidx[7] == 8381 or bidx[7] == 7959 or bidx[7] == 12647 or bidx[7] == 7633 or bidx[7] == 7816 or bidx[7] == 8020 or bidx[7] == 7729 or bidx[7] == 7980 or bidx[7] == 8034 or bidx[7] == 5365 or bidx[7] == 7563:
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
                            rotx = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))

                    elif bidx[9] == 8381 or bidx[9] == 7959 or bidx[9] == 12647 or bidx[9] == 7633 or bidx[9] == 7816 or bidx[9] == 8020 or bidx[9] == 7729 or bidx[9] == 7980 or bidx[9] == 8034 or bidx[9] == 5365 or bidx[9] == 7563:
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
                            roty = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))

                    elif bidx[11] == 8381 or bidx[11] == 7959 or bidx[11] == 12647 or bidx[11] == 7633 or bidx[11] == 7816 or bidx[11] == 8020 or bidx[11] == 7729 or bidx[11] == 7980 or bidx[11] == 8034 or bidx[11] == 5365 or bidx[11] == 7563:
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
                            rotz = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))

                    elif bidx[13] == 8391 or bidx[13] == 7959 or bidx[13] == 12647 or bidx[13] == 7633 or bidx[13] == 7816 or bidx[13] == 8020 or bidx[13] == 7729 or bidx[13] == 7980 or bidx[13] == 8034 or bidx[13] == 5365 or bidx[13] == 7563:
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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))

                    elif bidx[15] == 8391 or bidx[15] == 7959 or bidx[15] == 12647 or bidx[15] == 7633 or bidx[15] == 7816 or bidx[15] == 8020 or bidx[15] == 7729 or bidx[15] == 7980 or bidx[15] == 8034 or bidx[15] == 5365 or bidx[15] == 7563:
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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))

                    elif bidx[17] == 8391 or bidx[17] == 7959 or bidx[17] == 12647 or bidx[17] == 7633 or bidx[17] == 7816 or bidx[17] == 8020 or bidx[17] == 7729 or bidx[17] == 7980 or bidx[17] == 8034 or bidx[17] == 5365 or bidx[17] == 7563:
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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))
                            
                elif Type1 == 3:
                    if bidx[1] == 9192 or bidx[1] == 9469 or bidx[1] == 10324 or bidx[1] == 8003 or bidx[1] == 10239 or bidx[1] == 8924 or bidx[1] == 9890 or bidx[1] == 8286 or bidx[1] == 8315 or bidx[1] == 7999 or bidx[1] == 8733 or bidx[1] == 8722 or bidx[1] == 9992 or bidx[1] == 5365 or bidx[1] == 7968:
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
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))
                            
                    elif bidx[3] == 9192 or bidx[3] == 9469  or bidx[3] == 10324 or bidx[3] == 8003 or bidx[3] == 10239 or bidx[3] == 8924 or bidx[3] == 9890 or bidx[3] == 8286 or bidx[3] == 8315 or bidx[3] == 7999 or bidx[3] == 8733 or bidx[3] == 8722  or bidx[3] == 9992 or bidx[3] == 5365 or bidx[3] == 7968:
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
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))
                        
                            
                    elif bidx[5] == 9192 or bidx[5] == 9469 or bidx[5] == 10324 or bidx[5] == 8003 or bidx[5] == 10239 or bidx[5] == 8924 or bidx[5] == 9890 or bidx[5] == 8286 or bidx[5] == 8315 or bidx[5] == 7999 or bidx[5] == 8733 or bidx[5] == 8722 or bidx[5] == 9992 or bidx[5] == 5365 or bidx[5] == 7968:
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
                            posz = unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))
                            
                    elif bidx[7] == 9192 or bidx[7] == 9469 or bidx[7] == 10324 or bidx[7] == 8003 or bidx[7] == 10239 or bidx[7] == 8924 or bidx[7] == 9890 or bidx[7] == 8286 or bidx[7] == 8315 or bidx[7] == 7999 or bidx[7] == 8733 or bidx[7] == 8722 or bidx[7] == 9992 or bidx[7] == 5365 or bidx[7] == 7968:
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
                            rotx = -unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))
                            
                    elif bidx[9] == 9192 or bidx[9] == 9469 or bidx[9] == 10324 or bidx[9] == 8003 or bidx[9] == 10239 or bidx[9] == 8924 or bidx[9] == 9890 or bidx[9] == 8286 or bidx[9] == 8315 or bidx[9] == 7999 or bidx[9] == 8733 or bidx[9] == 8722 or bidx[9] == 9992 or bidx[9] == 5365 or bidx[9] == 7968:
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
                            roty = -unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))
                            
                    elif bidx[11] == 9192 or bidx[11] == 9469 or bidx[11] == 10324 or bidx[11] == 8003 or bidx[11] == 10239 or bidx[11] == 8924 or bidx[11] == 9890 or bidx[11] == 8286 or bidx[11] == 8315 or bidx[11] == 7999 or bidx[11] == 8733 or bidx[11] == 8722 or bidx[11] == 9992 or bidx[11] == 5365 or bidx[11] == 7968:
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
                            rotz = -unpack("<f", f.read(4))[0]
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))
                            
                    elif bidx[13] == 9192 or bidx[13] == 9469 or bidx[13] == 10324 or bidx[13] == 8003 or bidx[13] == 10239 or bidx[13] == 8924 or bidx[13] == 9890 or bidx[13] == 8286 or bidx[13] == 8315 or bidx[13] == 7999 or bidx[13] == 8733 or bidx[13] == 8722 or bidx[13] == 9992 or bidx[13] == 5365 or bidx[13] == 7968:
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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))
                            
                    elif bidx[15] == 9192 or bidx[15] == 9469 or bidx[15] == 10324 or bidx[15] == 8003 or bidx[15] == 10239 or bidx[15] == 8924 or bidx[15] == 9890 or bidx[15] == 8286 or bidx[15] == 8315 or bidx[15] == 7999 or bidx[15] == 8733 or bidx[15] == 8722 or bidx[15] == 9992 or bidx[15] == 5365 or bidx[15] == 7968:
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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))
                            
                    elif bidx[17] == 9192 or bidx[17] == 9469 or bidx[17] == 10324 or bidx[17] == 8003 or bidx[17] == 10239 or bidx[17] == 8924 or bidx[17] == 9890 or bidx[17] == 8286 or bidx[17] == 8315 or bidx[17] == 7999 or bidx[17] == 8733 or bidx[17] == 8722 or bidx[17] == 9992 or bidx[17] == 5365 or bidx[17] == 7968:
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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))

                elif Type1 == 2:
                    if bidx[1] == 7655 or bidx[1] == 10239 or bidx[1] == 9890 or bidx[1] == 7530 or bidx[1] == 7584 or bidx[1] == 9143 or bidx[1] == 9831 or bidx[1] == 12647 or bidx[1] == 9181 or bidx[1] == 9012 or bidx[1] == 10280 or bidx[1] == 8071 or bidx[1] == 5065 or bidx[1] == 11560 or bidx[1] == 8871 or bidx[1] == 7168 or bidx[1] == 9517:
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
                            posx = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.x = posx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))

                    elif bidx[3] == 7655 or bidx[3] == 10239 or bidx[3] == 9890 or bidx[3] == 7530 or bidx[3] == 7584 or bidx[3] == 9143 or bidx[3] == 9831 or bidx[3] == 12647 or bidx[3] == 9181 or bidx[3] == 9012 or bidx[3] == 10280 or bidx[3] == 8071 or bidx[3] == 5065 or bidx[3] == 11560 or bidx[3] == 8871 or bidx[3] == 7168 or bidx[3] == 9517:
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
                            posy = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.y = posy
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

                    elif bidx[5] == 7655 or bidx[5] == 10239 or bidx[5] == 9890 or bidx[5] == 7530 or bidx[5] == 7584 or bidx[5] == 9143 or bidx[5] == 9831 or bidx[5] == 12647 or bidx[5] == 9181 or bidx[5] == 9012 or bidx[5] == 10280 or bidx[5] == 8071 or bidx[5] == 5065 or bidx[5] == 11560 or bidx[5] == 8871 or bidx[5] == 7168 or bidx[5] == 9517:
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
                            posz = unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].location.z = posz
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))

                    elif bidx[7] == 7655 or bidx[7] == 10239 or bidx[7] == 9890 or bidx[7] == 7530 or bidx[7] == 7584 or bidx[7] == 9143 or bidx[7] == 9831 or bidx[7] == 12647 or bidx[7] == 9181 or bidx[7] == 9012 or bidx[7] == 10280 or bidx[7] == 8071 or bidx[7] == 5065 or bidx[7] == 11560 or bidx[7] == 8871 or bidx[7] == 7168 or bidx[7] == 9517:
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
                            rotx = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.x = rotx
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))

                    elif bidx[9] == 7655 or bidx[9] == 10239 or bidx[9] == 9890 or bidx[9] == 7530 or bidx[9] == 7584 or bidx[9] == 9143 or bidx[9] == 9831 or bidx[9] == 12647 or bidx[9] == 9181 or bidx[9] == 9012 or bidx[9] == 10280 or bidx[9] == 8071 or bidx[9] == 5065 or bidx[9] == 11560 or bidx[9] == 8871 or bidx[9] == 7168 or bidx[9] == 9517:
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
                            roty = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.y = roty
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))

                    elif bidx[11] == 7655 or bidx[11] == 10239 or bidx[11] == 9890 or bidx[11] == 7530 or bidx[11] == 7584 or bidx[11] == 9143 or bidx[11] == 9831 or bidx[11] == 12647 or bidx[11] == 9181 or bidx[11] == 9012 or bidx[11] == 10280 or bidx[11] == 8071 or bidx[11] == 5065 or bidx[11] == 11560 or bidx[11] == 8871 or bidx[11] == 7168 or bidx[11] == 9517:
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
                            rotz = -unpack("<f", f.read(4))[0]# / 10
                            unk = unpack("<f", f.read(4))[0]
                            if FloatCount == 1:
                                boneid+=1
                            ob.pose.bones[boneid].rotation_euler.z = rotz
                            ob.pose.bones[boneid].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))

                    elif bidx[13] == 7655 or bidx[13] == 10239 or bidx[13] == 9890 or bidx[13] == 7530 or bidx[13] == 7584 or bidx[13] == 9143 or bidx[13] == 9831 or bidx[13] == 12647 or bidx[13] == 9181 or bidx[13] == 9012 or bidx[13] == 10280 or bidx[13] == 8071 or bidx[13] == 5065 or bidx[13] == 11560 or bidx[13] == 8871 or bidx[13] == 7168 or bidx[13] == 9517:
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
                            ob.pose.bones[boneid].scale.x = sclx
                            ob.pose.bones[boneid].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))

                    elif bidx[15] == 7655 or bidx[15] == 10239 or bidx[15] == 9890 or bidx[15] == 7530 or bidx[15] == 7584 or bidx[15] == 9143 or bidx[15] == 9831 or bidx[15] == 12647 or bidx[15] == 9181 or bidx[15] == 9012 or bidx[15] == 10280 or bidx[15] == 8071 or bidx[15] == 5065 or bidx[15] == 11560 or bidx[15] == 8871 or bidx[15] == 7168 or bidx[15] == 9517:
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
                            ob.pose.bones[boneid].scale.y = scly
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))

                    elif bidx[17] == 7655 or bidx[17] == 10239 or bidx[17] == 9890 or bidx[17] == 7530 or bidx[17] == 7584 or bidx[17] == 9143 or bidx[17] == 9831 or bidx[17] == 12647 or bidx[17] == 9181 or bidx[17] == 9012 or bidx[17] == 10280 or bidx[17] == 8071 or bidx[17] == 5065 or bidx[17] == 11560 or bidx[17] == 8871 or bidx[17] == 7168 or bidx[17] == 9517:
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
                            ob.pose.bones[boneid].scale.z = sclz
                            ob.pose.bones[boneid].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))
                            
                elif Type1 == 1:
                    if bidx[1] == 8994 or bidx[1] == 9442 or bidx[1] == 8871 or bidx[1] == 9440 or bidx[1] == 9450 or bidx[1] == 8796 or bidx[1] == 9417 or bidx[1] == 9335 or bidx[1] == 14507 or bidx[1] == 6207 or bidx[1] == 8316 or bidx[1] == 9457 or bidx[1] == 10280 or bidx[1] == 9012 or bidx[1] == 11271 or bidx[1] == 7773 or bidx[1] == 10563 or bidx[1] == 7722 or bidx[1] == 9582 or bidx[1] == 7733:
                        if BoneCount == 78:
                            if bidx[0] == 3656:
                                f.seek(bidx[0]-32,0)
                                EntrySizeA = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeB = unpack("<H", f.read(2))[0]
                                f.seek(2,1)
                                EntrySizeC = unpack("<H", f.read(2))[0]
                                f.seek(2,1)
                                if EntrySizeA == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        posx = unpack("<f", f.read(4))[0]# / 10
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone0 in bones_1:
                                            if bone0 == 0:
                                                ob.pose.bones[0].location.x = posx
                                                ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(FloatCount))
                            
                    elif bidx[3] == 8994 or bidx[3] == 9442 or bidx[3] == 8871 or bidx[3] == 9440 or bidx[3] == 9450 or bidx[3] == 8796 or bidx[3] == 9417 or bidx[3] == 9335 or bidx[3] == 14507 or bidx[3] == 6207 or bidx[3] == 8316 or bidx[3] == 9457 or bidx[3] == 10280 or bidx[3] == 9012 or bidx[3] == 11271 or bidx[3] == 7773 or bidx[3] == 10563 or bidx[3] == 7722 or bidx[3] == 9582 or bidx[3] == 7733:

                        if BoneCount == 78:
                            if bidx[2] == 3656:
                                f.seek(bidx[2]-32,0)
                                EntrySizeD = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeE = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeF = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)

                                if EntrySizeD == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        posy = unpack("<f", f.read(4))[0]# / 10
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone1 in bones_2:
                                            if bone1 == 0:
                                                ob.pose.bones[0].location.y = posy
                                                ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(FloatCount))

                                    f.seek(8,1)
                                    EntrySizeG1 = unpack("<H", f.read(2))[0]-32
                                    f.seek(2,1)
                                    EntrySizeH1 = unpack("<H", f.read(2))[0]-32
                                    f.seek(2,1)
                                    EntrySizeI1 = unpack("<H", f.read(2))[0]-32
                                    f.seek(2,1)
                                    if EntrySizeG1 == 3736:
                                        while f.tell() < 3736:
                                            FloatCount = unpack("<f", f.read(4))[0]
                                            framerate = unpack("<f", f.read(4))[0]
                                            posz = unpack("<f", f.read(4))[0]# / 10
                                            unk = unpack("<f", f.read(4))[0]
                                            for bone2 in bones_3:
                                                if bone2 == 0:
                                                    ob.pose.bones[0].location.z = posz
                                                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))
                            
                    elif bidx[5] == 8994 or bidx[5] == 9442 or bidx[5] == 8871 or bidx[5] == 9440 or bidx[5] == 9450 or bidx[5] == 8796 or bidx[5] == 9417 or bidx[5] == 9335 or bidx[5] == 14507 or bidx[5] == 6207 or bidx[5] == 8316 or bidx[5] == 9457 or bidx[5] == 10280 or bidx[5] == 9012 or bidx[5] == 11271 or bidx[5] == 7773 or bidx[5] == 10563 or bidx[5] == 7722 or bidx[5] == 9582 or bidx[5] == 7733:
                        if BoneCount == 78:
                            if bidx[4] == 3656:
                                f.seek(bidx[4]-32,0)
                                EntrySizeG = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeH = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeI = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                if EntrySizeG == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        posz = unpack("<f", f.read(4))[0]# / 10
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone2 in bones_3:
                                            if bone2 == 0:
                                                ob.pose.bones[0].location.z = posz
                                                ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(FloatCount))
                                    f.seek(8,1)
                                    EntrySizeG2 = unpack("<H", f.read(2))[0]-32
                                    f.seek(2,1)
                                    EntrySizeH2 = unpack("<H", f.read(2))[0]-32
                                    f.seek(2,1)
                                    EntrySizeI2 = unpack("<H", f.read(2))[0]-32
                                    f.seek(2,1)
                                    if EntrySizeG2 == 3736:
                                        while f.tell() < 3736:
                                            FloatCount = unpack("<f", f.read(4))[0]
                                            framerate = unpack("<f", f.read(4))[0]
                                            rotx = unpack("<f", f.read(4))[0]# / 10
                                            unk = unpack("<f", f.read(4))[0]
                                            for bone3 in bones_4:
                                                if bone3 == 0:
                                                    ob.pose.bones[0].rotation_euler.x = rotx
                                                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))
                            
                            
                    elif bidx[7] == 8994 or bidx[7] == 9442 or bidx[7] == 8871 or bidx[7] == 9440 or bidx[7] == 9450 or bidx[7] == 8796 or bidx[7] == 9417 or bidx[7] == 9335 or bidx[7] == 14507 or bidx[7] == 6207 or bidx[7] == 8316 or bidx[7] == 9457 or bidx[7] == 10280 or bidx[7] == 9012 or bidx[7] == 11271 or bidx[7] == 7773 or bidx[7] == 10563 or bidx[7] == 7722 or bidx[7] == 9582 or bidx[7] == 7733:
                        if BoneCount == 78:
                            if bidx[6] == 3656:
                                f.seek(bidx[6]-32,0)
                                EntrySizeJ = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeK = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeL = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                if EntrySizeG == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        rotx = -unpack("<f", f.read(4))[0]
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone3 in bones_4:
                                            if bone3 == 0:
                                                ob.pose.bones[0].rotation_euler.x = rotx
                                                ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(FloatCount))
                            
                    elif bidx[9] == 8994 or bidx[9] == 9442 or bidx[9] == 8871 or bidx[9] == 9440 or bidx[9] == 9450 or bidx[9] == 8796 or bidx[9] == 9417 or bidx[9] == 9335 or bidx[9] == 14507 or bidx[9] == 6207 or bidx[9] == 8316 or bidx[9] == 9457 or bidx[9] == 10280 or bidx[9] == 9012 or bidx[9] == 11271 or bidx[9] == 7773 or bidx[9] == 10563 or bidx[9] == 7722 or bidx[9] == 9582 or bidx[9] == 7733:
                        if BoneCount == 78:
                            if bidx[8] == 3656:
                                f.seek(bidx[8]-32,0)
                                EntrySizeM = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeN = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeO = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                if EntrySizeM == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        roty = -unpack("<f", f.read(4))[0]
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone4 in bones_5:
                                            if bone4 == 0:
                                                ob.pose.bones[0].rotation_euler.y = roty
                                                ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(FloatCount))
                            
                    elif bidx[11] == 8994 or bidx[11] == 9442 or bidx[11] == 8871 or bidx[11] == 9440 or bidx[11] == 9450 or bidx[11] == 8796 or bidx[11] == 9417 or bidx[11] == 9335 or bidx[11] == 14507 or bidx[11] == 6207 or bidx[11] == 8316 or bidx[11] == 9457 or bidx[11] == 10280 or bidx[11] == 9012 or bidx[11] == 11271 or bidx[11] == 7773 or bidx[11] == 10563 or bidx[11] == 7722 or bidx[11] == 9582 or bidx[11] == 7733:
                        if BoneCount == 78:
                            if bidx[10] == 3656:
                                f.seek(bidx[10]-32,0)
                                EntrySizeP = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeQ = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeR = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                if EntrySizeP == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        rotz = -unpack("<f", f.read(4))[0]
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone5 in bones_6:
                                            if bone5 == 0:
                                                ob.pose.bones[0].rotation_euler.z = rotz
                                                ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(FloatCount))
                            
                    elif bidx[13] == 8994 or bidx[13] == 9442 or bidx[13] == 8871 or bidx[13] == 9440 or bidx[13] == 9450 or bidx[13] == 8796 or bidx[13] == 9417 or bidx[13] == 9335 or bidx[13] == 14507 or bidx[13] == 6207 or bidx[13] == 8316 or bidx[13] == 9457 or bidx[13] == 10280 or bidx[13] == 9012 or bidx[13] == 11271 or bidx[13] == 7773 or bidx[13] == 10563 or bidx[13] == 7722 or bidx[13] == 9582 or bidx[13] == 7733:

                        if BoneCount == 78:
                            if bidx[12] == 3656:
                                f.seek(bidx[12]-32,0)
                                EntrySizeS = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeT = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeU = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                if EntrySizeS == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        sclx = unpack("<f", f.read(4))[0]
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone6 in bones_7:
                                            if bone6 == 0:
                                                ob.pose.bones[0].scale.x = sclx
                                                ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(FloatCount))
                            
                    elif bidx[15] == 8994 or bidx[15] == 9442 or bidx[15] == 8871 or bidx[15] == 9440 or bidx[15] == 9450 or bidx[15] == 8796 or bidx[15] == 9417 or bidx[15] == 9335 or bidx[15] == 14507 or bidx[15] == 6207 or bidx[15] == 8316 or bidx[15] == 9457 or bidx[15] == 10280 or bidx[15] == 9012 or bidx[15] == 11271 or bidx[15] == 7773 or bidx[15] == 10563 or bidx[15] == 7722 or bidx[15] == 9582 or bidx[15] == 7733:

                        if BoneCount == 78:
                           if bidx[14] == 3656:
                               f.seek(bidx[16]-32,0)
                               EntrySizeV = unpack("<H", f.read(2))[0]-32
                               f.seek(2,1)
                               EntrySizeW = unpack("<H", f.read(2))[0]-32
                               f.seek(2,1)
                               EntrySizeX = unpack("<H", f.read(2))[0]-32
                               f.seek(2,1)
                               if EntrySizeV == 3684:
                                   while f.tell() < 3684:
                                       FloatCount = unpack("<f", f.read(4))[0]
                                       framerate = unpack("<f", f.read(4))[0]
                                       scly = unpack("<f", f.read(4))[0]
                                       unk = unpack("<f", f.read(4))[0]
                                       for bone7 in bones_8:
                                           if bone7 == 0:
                                               ob.pose.bones[0].scale.y = scly
                                               ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(FloatCount))
                            
                    elif bidx[17] == 8994 or bidx[17] == 9442 or bidx[17] == 8871 or bidx[17] == 9440 or bidx[17] == 9450 or bidx[17] == 8796 or bidx[17] == 9417 or bidx[17] == 9335 or bidx[17] == 14507 or bidx[17] == 6207 or bidx[17] == 8316 or bidx[17] == 9457 or bidx[17] == 10280 or bidx[17] == 9012 or bidx[17] == 11271 or bidx[17] == 7773 or bidx[17] == 10563 or bidx[17] == 7722 or bidx[17] == 9582 or bidx[17] == 7733:
                        if BoneCount == 78:
                            if bidx[16] == 3656:
                                f.seek(bidx[16]-32,0)
                                EntrySizeY = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeZ = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                EntrySizeZZ = unpack("<H", f.read(2))[0]-32
                                f.seek(2,1)
                                if EntrySizeY == 3684:
                                    while f.tell() < 3684:
                                        FloatCount = unpack("<f", f.read(4))[0]
                                        framerate = unpack("<f", f.read(4))[0]
                                        sclz = unpack("<f", f.read(4))[0]
                                        unk = unpack("<f", f.read(4))[0]
                                        for bone8 in bones_9:
                                            if bone8 == 0:
                                                ob.pose.bones[0].scale.z = sclz
                                                ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(FloatCount))




def ani_exportV2_all_move_non_parser_locrotscl(f):
    ob = bpy.context.object
    index1=0
    ExtrIndex=2
    divideIndex=-1
    index_=1
    frameratess=1
    frameEndIndex=0
    frameEndIndex2=0
    frameratess=1
    f.write(pack("<I", 2))
    f.write(pack("<I", 32))
    f.write(pack("<I", 44))
    f.write(pack("<f", bpy.context.scene.frame_end))
    f.write(pack("<H", len(ob.pose.bones)))
    f.write(pack("<H", 9))
    f.write(pack("<I", 1))
    f.write(pack("<I", 68))
    f.write(pack("<I", 36+36*len(ob.pose.bones)+32))
    f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+32))
    for pbone in ob.pose.bones:
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+12+16*bpy.context.scene.frame_end+8+frameEndIndex))
        frameEndIndex+=12+16*bpy.context.scene.frame_end+8+32*9
        if pbone.scale.x:
            f.write(pack("<f", 1))
        if pbone.scale.y:
            f.write(pack("<f", 1))
        if pbone.scale.z:
            f.write(pack("<f", 1))
    for pbone in ob.pose.bones:
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 1))
    for pbone in ob.pose.bones:
        f.write(pack("B", 35))

    for pbone in ob.pose.bones:
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.location.x))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.location.z))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.location.y))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", -pbone.rotation_euler.y))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", -pbone.rotation_euler.z))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", -pbone.rotation_euler.y))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.scale.x))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.scale.y))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))

        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+16*bpy.context.scene.frame_end+32*2))
        f.write(pack("<I", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+12+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.scale.z))
            f.write(pack("<f", 0))

        f.write(pack("<I", 131073))
        f.write(pack("<I", 0))
                                 
        
def ani_importer_read(filepath, Beta_ani=False, Norm_ani=False):
    with open(filepath,"rb") as f:
        if Norm_ani:
            ani_importV2(f)
        if Beta_ani:
            pass

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        ani_exportV2_all_move_non_parser(f)
