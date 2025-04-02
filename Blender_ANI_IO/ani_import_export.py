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
    keybool=[]
    keyb=[]
    keyboolIndex=-1
    keyM = []
    idxA = 0
    idxB = 0
    version = unpack("<I", f.read(4))[0]
    if version == 2:
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
                m1 = unpack("<H", f.read(2))[0]
                u1 = unpack("<H", f.read(2))[0]
                m2 = unpack("<H", f.read(2))[0]
                u2 = unpack("<H", f.read(2))[0]
                m3 = unpack("<H", f.read(2))[0]
                u3 = unpack("<H", f.read(2))[0]
                m4 = unpack("<H", f.read(2))[0]
                u4 = unpack("<H", f.read(2))[0]
                m5 = unpack("<H", f.read(2))[0]
                u5 = unpack("<H", f.read(2))[0]
                m6 = unpack("<H", f.read(2))[0]
                u6 = unpack("<H", f.read(2))[0]
                m7 = unpack("<H", f.read(2))[0]
                u7 = unpack("<H", f.read(2))[0]
                m8 = unpack("<H", f.read(2))[0]
                u8 = unpack("<H", f.read(2))[0]
                m9 = unpack("<H", f.read(2))[0]
                u9 = unpack("<H", f.read(2))[0]
                keyM.append([m1,u1,m2,u2,m3,u3,m4,u4,m5,u5,m6,u6,m7,u7,m8,u8,m9,u9])
                idxA+=36
            for i in range(BoneCount):
                booleansOnOffKeys1Posx = unpack("B", f.read(1))[0]
                booleansOnOffKeys2Posy = unpack("B", f.read(1))[0]
                booleansOnOffKeys3Posz = unpack("B", f.read(1))[0]
                booleansOnOffKeys4Rotx = unpack("B", f.read(1))[0]
                booleansOnOffKeys5Roty = unpack("B", f.read(1))[0]
                booleansOnOffKeys6Rotz = unpack("B", f.read(1))[0]
                booleansOnOffKeys7Sclx = unpack("B", f.read(1))[0]
                booleansOnOffKeys8Scly = unpack("B", f.read(1))[0]
                booleansOnOffKeys9Sclz = unpack("B", f.read(1))[0]
                idxB+=9
            for i in range(BoneCount):
                boneiddd = unpack("B", f.read(1))[0]

            for i, bidx in enumerate(keyM):
                if Type1 == 5:
                    if bidx[1] == 7980 or bidx[1] == 7308:
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
                    elif bidx[3] == 7980 or bidx[3] == 7308:
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

                    elif bidx[5] == 7980 or bidx[5] == 7308:
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

                    elif bidx[7] == 7980 or bidx[7] == 7308:
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

                    elif bidx[9] == 7980 or bidx[9] == 7308:
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

                    elif bidx[11] == 7980 or bidx[11] == 7308:
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

                    elif bidx[13] == 7980 or bidx[13] == 7308:
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

                    elif bidx[15] == 7980 or bidx[15] == 7308:
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

                    elif bidx[17] == 7980 or bidx[17] == 7308:
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
                    if bidx[1] == 9192 or bidx[1] == 9469 or bidx[1] == 10324 or bidx[1] == 8003 or bidx[1] == 10239:
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
                    elif bidx[3] == 9192 or bidx[3] == 9469  or bidx[3] == 10324 or bidx[3] == 8003 or bidx[3] == 10239:
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
                    elif bidx[5] == 9192 or bidx[5] == 9469 or bidx[5] == 10324 or bidx[5] == 8003 or bidx[5] == 10239:
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
                    elif bidx[7] == 9192 or bidx[7] == 9469 or bidx[7] == 10324 or bidx[7] == 8003 or bidx[7] == 10239:
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
                    elif bidx[9] == 9192 or bidx[9] == 9469 or bidx[9] == 10324 or bidx[9] == 8003 or bidx[9] == 10239:
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
                    elif bidx[11] == 9192 or bidx[11] == 9469 or bidx[11] == 10324 or bidx[11] == 8003 or bidx[11] == 10239:
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
                    elif bidx[13] == 9192 or bidx[13] == 9469 or bidx[13] == 10324 or bidx[13] == 8003 or bidx[13] == 10239:
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
                    elif bidx[15] == 9192 or bidx[15] == 9469 or bidx[15] == 10324 or bidx[15] == 8003 or bidx[15] == 10239:
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
                    elif bidx[17] == 9192 or bidx[17] == 9469 or bidx[17] == 10324 or bidx[17] == 8003 or bidx[17] == 10239:
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
                    if bidx[1] == 7655 or bidx[1] == 10239:
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

                    elif bidx[3] == 7655 or bidx[3] == 10239:
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

                    elif bidx[5] == 7655 or bidx[5] == 10239:
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

                    elif bidx[7] == 7655 or bidx[7] == 10239:
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

                    elif bidx[9] == 7655 or bidx[9] == 10239:
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

                    elif bidx[11] == 7655 or bidx[11] == 10239:
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

                    elif bidx[13] == 7655 or bidx[13] == 10239:
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

                    elif bidx[15] == 7655 or bidx[15] == 10239:
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

                    elif bidx[17] == 7655 or bidx[17] == 10239:
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
                    if bidx[1] == 8994 or bidx[1] == 9442 or bidx[1] == 8871:
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
                    elif bidx[3] == 8994 or bidx[3] == 9442 or bidx[3] == 8871:
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
                    elif bidx[5] == 8994 or bidx[5] == 9442 or bidx[5] == 8871:
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
                    elif bidx[7] == 8994 or bidx[7] == 9442 or bidx[7] == 8871:
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
                    elif bidx[9] == 8994 or bidx[9] == 9442 or bidx[9] == 8871:
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
                    elif bidx[11] == 8994 or bidx[11] == 9442 or bidx[11] == 8871:
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
                    elif bidx[13] == 8994 or bidx[13] == 9442 or bidx[13] == 8871:
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
                    elif bidx[15] == 8994 or bidx[15] == 9442 or bidx[15] == 8871:
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
                    elif bidx[17] == 8994 or bidx[17] == 9442 or bidx[17] == 8871:
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
