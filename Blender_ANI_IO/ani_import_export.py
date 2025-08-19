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

    global version

    booleanns = []

    version = unpack("<I", f.read(4))[0]
    if version == 2:
        EntrySize = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
        EntrySize1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
        FloatCount = unpack("<f", f.read(4))[0]
        BoneCount = unpack("<H", f.read(2))[0]
        offsetCount = unpack("<H", f.read(2))[0]
        Type1 = unpack("<I", f.read(4))[0]
        EntrySize2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
        EntrySize3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
        EntrySize4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
        
        bpy.context.scene.frame_end = int(FloatCount)
        bpy.context.scene.frame_current = 1
        bpy.context.scene.frame_start = 1

        if BoneCount == 0:
            pass
        elif BoneCount == 1:
            posxOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            
            booleanPX1 = unpack("B", f.read(1))[0]==True
            booleanPY1 = unpack("B", f.read(1))[0]==True
            booleanPZ1 = unpack("B", f.read(1))[0]==True
            booleanRX1 = unpack("B", f.read(1))[0]==True
            booleanRY1 = unpack("B", f.read(1))[0]==True
            booleanRZ1 = unpack("B", f.read(1))[0]==True
            booleanSX1 = unpack("B", f.read(1))[0]==True
            booleanSY1 = unpack("B", f.read(1))[0]==True
            booleanSZ1 = unpack("B", f.read(1))[0]==True
            if booleanPX1 > 0:
                f.seek(posxOn,0)
                f.seek(-32,1)
                Size1 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size2 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size3 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))
            if booleanPY1 > 0:
                f.seek(posyOn,0)
                f.seek(-32,1)
                Size4 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size5 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size6 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size4:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))
            if booleanPZ1 > 0:
                f.seek(poszOn,0)
                f.seek(-32,1)
                Size7 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size8 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size9 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size7:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))
            if booleanRX1 > 0:
                f.seek(rotxOn,0)
                f.seek(-32,1)
                Size10 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size11 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size12 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size10:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))
            if booleanRY1 > 0:
                f.seek(rotyOn,0)
                f.seek(-32,1)
                Size13 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size14 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size15 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size13:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))
            if booleanRZ1 > 0:
                f.seek(rotzOn,0)
                f.seek(-32,1)
                Size16 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size17 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size18 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size16:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))
            if booleanSX1 > 0:
                f.seek(sclxOn,0)
                f.seek(-32,1)
                Size19 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size20 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size21 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size19:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))
            if booleanSY1 > 0:
                f.seek(sclyOn,0)
                f.seek(-32,1)
                Size22 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size23 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size24 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size22:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))
            if booleanSZ1 > 0:
                f.seek(sclzOn,0)
                f.seek(-32,1)
                Size25 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size26 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size27 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size25:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 2:
            posxOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn1 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn2 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1a = unpack("B", f.read(1))[0]==True
            booleanPY1a = unpack("B", f.read(1))[0]==True
            booleanPZ1a = unpack("B", f.read(1))[0]==True
            booleanRX1a = unpack("B", f.read(1))[0]==True
            booleanRY1a = unpack("B", f.read(1))[0]==True
            booleanRZ1a = unpack("B", f.read(1))[0]==True
            booleanSX1a = unpack("B", f.read(1))[0]==True
            booleanSY1a = unpack("B", f.read(1))[0]==True
            booleanSZ1a = unpack("B", f.read(1))[0]==True

            booleanPX1b = unpack("B", f.read(1))[0]==True
            booleanPY1b = unpack("B", f.read(1))[0]==True
            booleanPZ1b = unpack("B", f.read(1))[0]==True
            booleanRX1b = unpack("B", f.read(1))[0]==True
            booleanRY1b = unpack("B", f.read(1))[0]==True
            booleanRZ1b = unpack("B", f.read(1))[0]==True
            booleanSX1b = unpack("B", f.read(1))[0]==True
            booleanSY1b = unpack("B", f.read(1))[0]==True
            booleanSZ1b = unpack("B", f.read(1))[0]==True

            if booleanPX1a > 0:
                f.seek(posxOn1,0)
                f.seek(-32,1)
                Size1 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size2 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size3 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1a > 0:
                f.seek(posyOn1,0)
                f.seek(-32,1)
                Size4 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size5 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size6 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size4:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1a > 0:
                f.seek(poszOn1,0)
                f.seek(-32,1)
                Size7 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size8 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size9 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size7:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1a > 0:
                f.seek(rotxOn1,0)
                f.seek(-32,1)
                Size10 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size11 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size12 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size10:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1a > 0:
                f.seek(rotyOn1,0)
                f.seek(-32,1)
                Size13 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size14 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size15 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size13:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1a > 0:
                f.seek(rotzOn1,0)
                f.seek(-32,1)
                Size16 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size17 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size18 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size16:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1a > 0:
                f.seek(sclxOn1,0)
                f.seek(-32,1)
                Size19 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size20 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size21 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size19:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1a > 0:
                f.seek(sclyOn1,0)
                f.seek(-32,1)
                Size22 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size23 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size24 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size22:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1a > 0:
                f.seek(sclzOn1,0)
                f.seek(-32,1)
                Size25 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size26 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size27 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size16:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1b > 0:
                f.seek(posxOn2,0)
                f.seek(-32,1)
                Size28 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size29 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size30 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size28:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx1 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx1
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1b > 0:
                f.seek(posyOn2,0)
                f.seek(-32,1)
                Size31 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size32 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size33 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size31:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy1 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy1
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1b > 0:
                f.seek(poszOn2,0)
                f.seek(-32,1)
                Size34 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size35 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size36 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size34:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz1 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz1
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1b > 0:
                f.seek(rotxOn2,0)
                f.seek(-32,1)
                Size37 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size38 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size39 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size37:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx1 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx1
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1b > 0:
                f.seek(rotyOn2,0)
                f.seek(-32,1)
                Size40 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size41 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size42 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size40:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz1 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz1
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1b > 0:
                f.seek(rotzOn2,0)
                f.seek(-32,1)
                Size43 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size44 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size45 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size43:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty1 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty1
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1b > 0:
                f.seek(sclxOn2,0)
                f.seek(-32,1)
                Size46 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size47 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size48 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size46:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx1 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx1
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1b > 0:
                f.seek(sclyOn2,0)
                f.seek(-32,1)
                Size49 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size50 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size51 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size49:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly1 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly1
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1b > 0:
                f.seek(sclzOn2,0)
                f.seek(-32,1)
                Size52 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size53 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size54 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size52:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz1 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz1
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 3:
            posxOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn3 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn4 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn5 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1c = unpack("B", f.read(1))[0]==True
            booleanPY1c = unpack("B", f.read(1))[0]==True
            booleanPZ1c = unpack("B", f.read(1))[0]==True
            booleanRX1c = unpack("B", f.read(1))[0]==True
            booleanRY1c = unpack("B", f.read(1))[0]==True
            booleanRZ1c = unpack("B", f.read(1))[0]==True
            booleanSX1c = unpack("B", f.read(1))[0]==True
            booleanSY1c = unpack("B", f.read(1))[0]==True
            booleanSZ1c = unpack("B", f.read(1))[0]==True

            booleanPX1d = unpack("B", f.read(1))[0]==True
            booleanPY1d = unpack("B", f.read(1))[0]==True
            booleanPZ1d = unpack("B", f.read(1))[0]==True
            booleanRX1d = unpack("B", f.read(1))[0]==True
            booleanRY1d = unpack("B", f.read(1))[0]==True
            booleanRZ1d = unpack("B", f.read(1))[0]==True
            booleanSX1d = unpack("B", f.read(1))[0]==True
            booleanSY1d = unpack("B", f.read(1))[0]==True
            booleanSZ1d = unpack("B", f.read(1))[0]==True

            booleanPX1e = unpack("B", f.read(1))[0]==True
            booleanPY1e = unpack("B", f.read(1))[0]==True
            booleanPZ1e = unpack("B", f.read(1))[0]==True
            booleanRX1e = unpack("B", f.read(1))[0]==True
            booleanRY1e = unpack("B", f.read(1))[0]==True
            booleanRZ1e = unpack("B", f.read(1))[0]==True
            booleanSX1e = unpack("B", f.read(1))[0]==True
            booleanSY1e = unpack("B", f.read(1))[0]==True
            booleanSZ1e = unpack("B", f.read(1))[0]==True

            if booleanPX1c > 0:
                f.seek(posxOn3,0)
                f.seek(-32,1)
                Size55 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size56 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size57 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size55:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx2 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx2
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1c > 0:
                f.seek(posyOn3,0)
                f.seek(-32,1)
                Size58 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size59 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size60 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size58:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy2 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy2
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1c > 0:
                f.seek(poszOn3,0)
                f.seek(-32,1)
                Size61 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size62 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size63 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size61:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz2 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz2
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1c > 0:
                f.seek(rotxOn3,0)
                f.seek(-32,1)
                Size64 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size65 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size66 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size64:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx2 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx2
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1c > 0:
                f.seek(rotyOn3,0)
                f.seek(-32,1)
                Size67 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size68 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size69 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size67:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz2 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz2
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1c > 0:
                f.seek(rotzOn3,0)
                f.seek(-32,1)
                Size70 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size71 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size72 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size70:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty2 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty2
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1c > 0:
                f.seek(sclxOn3,0)
                f.seek(-32,1)
                Size73 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size74 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size75 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size73:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx2 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx2
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1c > 0:
                f.seek(sclyOn3,0)
                f.seek(-32,1)
                Size76 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size77 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size78 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size76:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly2 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly2
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1c > 0:
                f.seek(sclzOn3,0)
                f.seek(-32,1)
                Size79 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size80 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size81 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size79:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz2 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz2
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1d > 0:
                f.seek(posxOn4,0)
                f.seek(-32,1)
                Size82 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size83 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size84 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size82:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx3 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx3
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1d > 0:
                f.seek(posyOn4,0)
                f.seek(-32,1)
                Size85 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size86 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size87 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size85:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy3 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy3
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1d > 0:
                f.seek(poszOn4,0)
                f.seek(-32,1)
                Size88 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size89 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size90 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size88:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz3 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz3
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1d > 0:
                f.seek(rotxOn4,0)
                f.seek(-32,1)
                Size91 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size92 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size93 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size91:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx3 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx3
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1d > 0:
                f.seek(rotyOn4,0)
                f.seek(-32,1)
                Size94 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size95 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size96 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size94:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz3 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz3
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1d > 0:
                f.seek(rotzOn4,0)
                f.seek(-32,1)
                Size97 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size98 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size99 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size97:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty3 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty3
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1d > 0:
                f.seek(sclxOn4,0)
                f.seek(-32,1)
                Size100 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size101 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size102 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size100:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx3 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx3
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1d > 0:
                f.seek(sclyOn4,0)
                f.seek(-32,1)
                Size103 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size104 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size105 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size103:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly3 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly3
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1d > 0:
                f.seek(sclzOn4,0)
                f.seek(-32,1)
                Size106 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size107 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size108 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size106:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz3 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz3
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1e > 0:
                f.seek(posxOn5,0)
                f.seek(-32,1)
                Size109 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size110 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size111 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size109:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx4 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx4
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1e > 0:
                f.seek(posyOn5,0)
                f.seek(-32,1)
                Size112 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size113 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size114 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size112:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy4 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy4
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1e > 0:
                f.seek(poszOn5,0)
                f.seek(-32,1)
                Size115 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size116 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size117 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size115:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz4 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz4
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1e > 0:
                f.seek(rotxOn5,0)
                f.seek(-32,1)
                Size118 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size119 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size120 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size118:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx4 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx4
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1e > 0:
                f.seek(rotyOn5,0)
                f.seek(-32,1)
                Size121 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size122 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size123 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size121:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz4 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz4
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1e > 0:
                f.seek(rotzOn5,0)
                f.seek(-32,1)
                Size124 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size125 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size126 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size124:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty4 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty4
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1e > 0:
                f.seek(sclxOn5,0)
                f.seek(-32,1)
                Size127 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size128 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size129 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size127:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx4 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx4
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1e > 0:
                f.seek(sclyOn5,0)
                f.seek(-32,1)
                Size130 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size131 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size132 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size130:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly4 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly4
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1e > 0:
                f.seek(sclzOn5,0)
                f.seek(-32,1)
                Size133 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size134 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size135 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size133:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz4 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz4
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))
        elif BoneCount == 4:
            posxOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn6 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn7 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn8 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn9 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1f = unpack("B", f.read(1))[0]==True
            booleanPY1f = unpack("B", f.read(1))[0]==True
            booleanPZ1f = unpack("B", f.read(1))[0]==True
            booleanRX1f = unpack("B", f.read(1))[0]==True
            booleanRY1f = unpack("B", f.read(1))[0]==True
            booleanRZ1f = unpack("B", f.read(1))[0]==True
            booleanSX1f = unpack("B", f.read(1))[0]==True
            booleanSY1f = unpack("B", f.read(1))[0]==True
            booleanSZ1f = unpack("B", f.read(1))[0]==True

            booleanPX1g = unpack("B", f.read(1))[0]==True
            booleanPY1g = unpack("B", f.read(1))[0]==True
            booleanPZ1g = unpack("B", f.read(1))[0]==True
            booleanRX1g = unpack("B", f.read(1))[0]==True
            booleanRY1g = unpack("B", f.read(1))[0]==True
            booleanRZ1g = unpack("B", f.read(1))[0]==True
            booleanSX1g = unpack("B", f.read(1))[0]==True
            booleanSY1g = unpack("B", f.read(1))[0]==True
            booleanSZ1g = unpack("B", f.read(1))[0]==True

            booleanPX1h = unpack("B", f.read(1))[0]==True
            booleanPY1h = unpack("B", f.read(1))[0]==True
            booleanPZ1h = unpack("B", f.read(1))[0]==True
            booleanRX1h = unpack("B", f.read(1))[0]==True
            booleanRY1h = unpack("B", f.read(1))[0]==True
            booleanRZ1h = unpack("B", f.read(1))[0]==True
            booleanSX1h = unpack("B", f.read(1))[0]==True
            booleanSY1h = unpack("B", f.read(1))[0]==True
            booleanSZ1h = unpack("B", f.read(1))[0]==True

            booleanPX1i = unpack("B", f.read(1))[0]==True
            booleanPY1i = unpack("B", f.read(1))[0]==True
            booleanPZ1i = unpack("B", f.read(1))[0]==True
            booleanRX1i = unpack("B", f.read(1))[0]==True
            booleanRY1i = unpack("B", f.read(1))[0]==True
            booleanRZ1i = unpack("B", f.read(1))[0]==True
            booleanSX1i = unpack("B", f.read(1))[0]==True
            booleanSY1i = unpack("B", f.read(1))[0]==True
            booleanSZ1i = unpack("B", f.read(1))[0]==True

            if booleanPX1f > 0:
                f.seek(posxOn6,0)
                f.seek(-32,1)
                Size136 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size137 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size138 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size136:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx5 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx5
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1f > 0:
                f.seek(posyOn6,0)
                f.seek(-32,1)
                Size139 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size140 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size141 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size139:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy5 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy5
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1f > 0:
                f.seek(poszOn6,0)
                f.seek(-32,1)
                Size142 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size143 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size144 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size139:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz5 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz5
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1f > 0:
                f.seek(rotxOn6,0)
                f.seek(-32,1)
                Size145 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size146 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size147 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size145:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx5 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx5
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1f > 0:
                f.seek(rotyOn6,0)
                f.seek(-32,1)
                Size148 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size149 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size150 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size148:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz5 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz5
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1f > 0:
                f.seek(rotzOn6,0)
                f.seek(-32,1)
                Size151 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size152 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size153 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size151:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty5 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty5
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1f > 0:
                f.seek(sclxOn6,0)
                f.seek(-32,1)
                Size154 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size155 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size156 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size154:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx5 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx5
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1f > 0:
                f.seek(sclyOn6,0)
                f.seek(-32,1)
                Size157 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size158 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size159 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size157:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly5 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly5
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1f > 0:
                f.seek(sclzOn6,0)
                f.seek(-32,1)
                Size160 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size161 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size162 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size160:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz5 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz5
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1g > 0:
                f.seek(posxOn7,0)
                f.seek(-32,1)
                Size163 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size164 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size165 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size163:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx6 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx6
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1g > 0:
                f.seek(posyOn7,0)
                f.seek(-32,1)
                Size166 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size167 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size168 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size166:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy6 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy6
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1g > 0:
                f.seek(poszOn7,0)
                f.seek(-32,1)
                Size169 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size170 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size171 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size169:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz6 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz6
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1g > 0:
                f.seek(rotxOn7,0)
                f.seek(-32,1)
                Size172 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size173 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size174 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size172:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx6 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx6
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1g > 0:
                f.seek(rotyOn7,0)
                f.seek(-32,1)
                Size175 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size176 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size177 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size175:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz6 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz6
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1g > 0:
                f.seek(rotzOn7,0)
                f.seek(-32,1)
                Size178 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size179 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size180 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size178:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty6 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty6
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1g > 0:
                f.seek(sclxOn7,0)
                f.seek(-32,1)
                Size181 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size182 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size183 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size181:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx6 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx6
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1g > 0:
                f.seek(sclyOn7,0)
                f.seek(-32,1)
                Size184 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size185 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size186 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size184:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly6 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly6
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1g > 0:
                f.seek(sclzOn7,0)
                f.seek(-32,1)
                Size187 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size188 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size189 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size187:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz6 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz6
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1h > 0:
                f.seek(posxOn8,0)
                f.seek(-32,1)
                Size190 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size191 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size192 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size190:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx7 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx7
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1h > 0:
                f.seek(posyOn8,0)
                f.seek(-32,1)
                Size193 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size194 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size195 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size193:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy7 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy7
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1h > 0:
                f.seek(poszOn8,0)
                f.seek(-32,1)
                Size196 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size197 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size198 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size196:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz7 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz7
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1h > 0:
                f.seek(rotxOn8,0)
                f.seek(-32,1)
                Size199 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size200 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size201 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size199:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx7 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx7
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1h > 0:
                f.seek(rotyOn8,0)
                f.seek(-32,1)
                Size202 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size203 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size204 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size202:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz7 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz7
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1h > 0:
                f.seek(rotzOn8,0)
                f.seek(-32,1)
                Size205 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size206 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size207 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size205:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty7 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty7
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1h > 0:
                f.seek(sclxOn8,0)
                f.seek(-32,1)
                Size208 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size209 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size210 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size208:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx7 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx7
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1h > 0:
                f.seek(sclyOn8,0)
                f.seek(-32,1)
                Size211 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size212 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size213 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size211:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly7 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly7
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1h > 0:
                f.seek(sclzOn8,0)
                f.seek(-32,1)
                Size214 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size215 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size216 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size214:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz7 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz7
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1i > 0:
                f.seek(posxOn9,0)
                f.seek(-32,1)
                Size217 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size218 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size219 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size217:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx8 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx8
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1i > 0:
                f.seek(posyOn9,0)
                f.seek(-32,1)
                Size220 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size221 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size222 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size220:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy8 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy8
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1i > 0:
                f.seek(poszOn9,0)
                f.seek(-32,1)
                Size223 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size224 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size225 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size223:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz8 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz8
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1i > 0:
                f.seek(rotxOn9,0)
                f.seek(-32,1)
                Size226 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size227 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size228 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size226:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx8 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx8
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1i > 0:
                f.seek(rotyOn9,0)
                f.seek(-32,1)
                Size229 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size230 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size231 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size229:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz8 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz8
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1i > 0:
                f.seek(rotzOn9,0)
                f.seek(-32,1)
                Size232 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size233 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size234 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size232:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty8 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty8
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1i > 0:
                f.seek(sclxOn9,0)
                f.seek(-32,1)
                Size235 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size236 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size237 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size235:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx8 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx8
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1i > 0:
                f.seek(sclyOn9,0)
                f.seek(-32,1)
                Size238 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size239 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size240 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size238:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly8 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly8
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1i > 0:
                f.seek(sclzOn9,0)
                f.seek(-32,1)
                Size241 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size242 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size243 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size241:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz8 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz8
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 5:
            posxOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn10 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn11 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn12 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn13 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn14 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1j = unpack("B", f.read(1))[0]==True
            booleanPY1j = unpack("B", f.read(1))[0]==True
            booleanPZ1j = unpack("B", f.read(1))[0]==True
            booleanRX1j = unpack("B", f.read(1))[0]==True
            booleanRY1j = unpack("B", f.read(1))[0]==True
            booleanRZ1j = unpack("B", f.read(1))[0]==True
            booleanSX1j = unpack("B", f.read(1))[0]==True
            booleanSY1j = unpack("B", f.read(1))[0]==True
            booleanSZ1j = unpack("B", f.read(1))[0]==True

            booleanPX1k = unpack("B", f.read(1))[0]==True
            booleanPY1k = unpack("B", f.read(1))[0]==True
            booleanPZ1k = unpack("B", f.read(1))[0]==True
            booleanRX1k = unpack("B", f.read(1))[0]==True
            booleanRY1k = unpack("B", f.read(1))[0]==True
            booleanRZ1k = unpack("B", f.read(1))[0]==True
            booleanSX1k = unpack("B", f.read(1))[0]==True
            booleanSY1k = unpack("B", f.read(1))[0]==True
            booleanSZ1k = unpack("B", f.read(1))[0]==True

            booleanPX1l = unpack("B", f.read(1))[0]==True
            booleanPY1l = unpack("B", f.read(1))[0]==True
            booleanPZ1l = unpack("B", f.read(1))[0]==True
            booleanRX1l = unpack("B", f.read(1))[0]==True
            booleanRY1l = unpack("B", f.read(1))[0]==True
            booleanRZ1l = unpack("B", f.read(1))[0]==True
            booleanSX1l = unpack("B", f.read(1))[0]==True
            booleanSY1l = unpack("B", f.read(1))[0]==True
            booleanSZ1l = unpack("B", f.read(1))[0]==True

            booleanPX1m = unpack("B", f.read(1))[0]==True
            booleanPY1m = unpack("B", f.read(1))[0]==True
            booleanPZ1m = unpack("B", f.read(1))[0]==True
            booleanRX1m = unpack("B", f.read(1))[0]==True
            booleanRY1m = unpack("B", f.read(1))[0]==True
            booleanRZ1m = unpack("B", f.read(1))[0]==True
            booleanSX1m = unpack("B", f.read(1))[0]==True
            booleanSY1m = unpack("B", f.read(1))[0]==True
            booleanSZ1m = unpack("B", f.read(1))[0]==True

            booleanPX1n = unpack("B", f.read(1))[0]==True
            booleanPY1n = unpack("B", f.read(1))[0]==True
            booleanPZ1n = unpack("B", f.read(1))[0]==True
            booleanRX1n = unpack("B", f.read(1))[0]==True
            booleanRY1n = unpack("B", f.read(1))[0]==True
            booleanRZ1n = unpack("B", f.read(1))[0]==True
            booleanSX1n = unpack("B", f.read(1))[0]==True
            booleanSY1n = unpack("B", f.read(1))[0]==True
            booleanSZ1n = unpack("B", f.read(1))[0]==True

            if booleanPX1j > 0:
                f.seek(posxOn10,0)
                f.seek(-32,1)
                Size244 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size245 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size246 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size244:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx9 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx9
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1j > 0:
                f.seek(posyOn10,0)
                f.seek(-32,1)
                Size247 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size248 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size249 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size247:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy9 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy9
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1j > 0:
                f.seek(poszOn10,0)
                f.seek(-32,1)
                Size250 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size251 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size252 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size250:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz9 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz9
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1j > 0:
                f.seek(rotxOn10,0)
                f.seek(-32,1)
                Size253 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size254 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size255 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size253:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1j > 0:
                f.seek(rotyOn10,0)
                f.seek(-32,1)
                Size256 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size257 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size258 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size256:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1j > 0:
                f.seek(rotzOn10,0)
                f.seek(-32,1)
                Size259 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size260 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size261 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size259:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1j > 0:
                f.seek(sclxOn10,0)
                f.seek(-32,1)
                Size262 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size263 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size264 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size262:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1j > 0:
                f.seek(sclyOn10,0)
                f.seek(-32,1)
                Size265 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size266 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size267 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size265:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1j > 0:
                f.seek(sclzOn10,0)
                f.seek(-32,1)
                Size268 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size269 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size270 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size268:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1k > 0:
                f.seek(posxOn11,0)
                f.seek(-32,1)
                Size271 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size272 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size273 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size271:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx10 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx10
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1k > 0:
                f.seek(posyOn11,0)
                f.seek(-32,1)
                Size274 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size275 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size276 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size274:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy10 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy10
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1k > 0:
                f.seek(poszOn11,0)
                f.seek(-32,1)
                Size277 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size278 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size279 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size277:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz10 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz10
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1k > 0:
                f.seek(rotxOn11,0)
                f.seek(-32,1)
                Size280 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size281 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size282 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size280:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx10 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx10
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1k > 0:
                f.seek(rotyOn11,0)
                f.seek(-32,1)
                Size283 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size284 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size285 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size283:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz10 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz10
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1k > 0:
                f.seek(rotzOn11,0)
                f.seek(-32,1)
                Size286 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size287 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size288 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size286:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty10 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty10
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1k > 0:
                f.seek(sclxOn11,0)
                f.seek(-32,1)
                Size289 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size290 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size291 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size289:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx10 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx10
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1k > 0:
                f.seek(sclyOn11,0)
                f.seek(-32,1)
                Size292 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size293 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size294 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size292:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly10 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly10
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1k > 0:
                f.seek(sclzOn11,0)
                f.seek(-32,1)
                Size295 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size296 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size297 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size295:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz10 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz10
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1l > 0:
                f.seek(posxOn12,0)
                f.seek(-32,1)
                Size298 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size299 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size300 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size298:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx11 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx11
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1l > 0:
                f.seek(posyOn12,0)
                f.seek(-32,1)
                Size301 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size302 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size303 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size301:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy11 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy11
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1l > 0:
                f.seek(poszOn12,0)
                f.seek(-32,1)
                Size304 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size305 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size306 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size304:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz11 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz11
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1l > 0:
                f.seek(rotxOn12,0)
                f.seek(-32,1)
                Size307 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size308 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size309 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size307:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx11 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx11
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1l > 0:
                f.seek(rotyOn12,0)
                f.seek(-32,1)
                Size310 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size311 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size312 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size310:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz11 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz11
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1l > 0:
                f.seek(rotzOn12,0)
                f.seek(-32,1)
                Size313 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size314 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size315 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size313:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty11 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty11
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1l > 0:
                f.seek(sclxOn12,0)
                f.seek(-32,1)
                Size316 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size317 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size318 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size313:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx11 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx11
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1l > 0:
                f.seek(sclyOn12,0)
                f.seek(-32,1)
                Size319 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size320 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size321 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size319:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly11 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly11
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1l > 0:
                f.seek(sclzOn12,0)
                f.seek(-32,1)
                Size322 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size323 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size324 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size322:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz11 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz11
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1m > 0:
                f.seek(posxOn13,0)
                f.seek(-32,1)
                Size325 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size326 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size327 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size325:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx12 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx12
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1m > 0:
                f.seek(posyOn13,0)
                f.seek(-32,1)
                Size328 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size329 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size330 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size328:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy12 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy12
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1m > 0:
                f.seek(poszOn13,0)
                f.seek(-32,1)
                Size331 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size332 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size333 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size331:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz12 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz12
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1m > 0:
                f.seek(rotxOn13,0)
                f.seek(-32,1)
                Size334 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size335 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size336 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size334:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx12 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx12
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1m > 0:
                f.seek(rotyOn13,0)
                f.seek(-32,1)
                Size337 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size338 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size339 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size337:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz12 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz12
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1m > 0:
                f.seek(rotzOn13,0)
                f.seek(-32,1)
                Size340 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size341 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size342 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size340:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty12 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty12
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1m > 0:
                f.seek(sclxOn13,0)
                f.seek(-32,1)
                Size343 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size344 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size345 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size343:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx12 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx12
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1m > 0:
                f.seek(sclyOn13,0)
                f.seek(-32,1)
                Size346 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size347 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size348 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size346:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly12 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly12
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1m > 0:
                f.seek(sclzOn13,0)
                f.seek(-32,1)
                Size349 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size350 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size351 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size349:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz12 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz12
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanPX1n > 0:
                f.seek(posxOn14,0)
                f.seek(-32,1)
                Size352 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size353 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size354 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size352:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx13 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx13
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1n > 0:
                f.seek(posyOn14,0)
                f.seek(-32,1)
                Size355 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size356 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size357 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size355:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy13 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy13
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1n > 0:
                f.seek(poszOn14,0)
                f.seek(-32,1)
                Size358 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size359 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size360 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size358:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz13 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz13
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1n > 0:
                f.seek(rotxOn14,0)
                f.seek(-32,1)
                Size361 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size362 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size363 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size361:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx13 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx13
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1n > 0:
                f.seek(rotyOn14,0)
                f.seek(-32,1)
                Size364 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size365 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size366 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size364:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz13 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz13
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1n > 0:
                f.seek(rotzOn14,0)
                f.seek(-32,1)
                Size367 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size368 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size369 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size367:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty13 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty13
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1n > 0:
                f.seek(sclxOn14,0)
                f.seek(-32,1)
                Size370 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size371 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size372 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size370:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx13 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx13
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1n > 0:
                f.seek(sclyOn14,0)
                f.seek(-32,1)
                Size373 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size374 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size375 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size373:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly13 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly13
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1n > 0:
                f.seek(sclyOn14,0)
                f.seek(-32,1)
                Size376 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size377 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size378 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size376:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz13 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz13
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 6:
            posxOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn15 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn16 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn17 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn18 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn19 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn20 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1o = unpack("B", f.read(1))[0]==True
            booleanPY1o = unpack("B", f.read(1))[0]==True
            booleanPZ1o = unpack("B", f.read(1))[0]==True
            booleanRX1o = unpack("B", f.read(1))[0]==True
            booleanRY1o = unpack("B", f.read(1))[0]==True
            booleanRZ1o = unpack("B", f.read(1))[0]==True
            booleanSX1o = unpack("B", f.read(1))[0]==True
            booleanSY1o = unpack("B", f.read(1))[0]==True
            booleanSZ1o = unpack("B", f.read(1))[0]==True

            booleanPX1p = unpack("B", f.read(1))[0]==True
            booleanPY1p = unpack("B", f.read(1))[0]==True
            booleanPZ1p = unpack("B", f.read(1))[0]==True
            booleanRX1p = unpack("B", f.read(1))[0]==True
            booleanRY1p = unpack("B", f.read(1))[0]==True
            booleanRZ1p = unpack("B", f.read(1))[0]==True
            booleanSX1p = unpack("B", f.read(1))[0]==True
            booleanSY1p = unpack("B", f.read(1))[0]==True
            booleanSZ1p = unpack("B", f.read(1))[0]==True

            booleanPX1q = unpack("B", f.read(1))[0]==True
            booleanPY1q = unpack("B", f.read(1))[0]==True
            booleanPZ1q = unpack("B", f.read(1))[0]==True
            booleanRX1q = unpack("B", f.read(1))[0]==True
            booleanRY1q = unpack("B", f.read(1))[0]==True
            booleanRZ1q = unpack("B", f.read(1))[0]==True
            booleanSX1q = unpack("B", f.read(1))[0]==True
            booleanSY1q = unpack("B", f.read(1))[0]==True
            booleanSZ1q = unpack("B", f.read(1))[0]==True

            booleanPX1r = unpack("B", f.read(1))[0]==True
            booleanPY1r = unpack("B", f.read(1))[0]==True
            booleanPZ1r = unpack("B", f.read(1))[0]==True
            booleanRX1r = unpack("B", f.read(1))[0]==True
            booleanRY1r = unpack("B", f.read(1))[0]==True
            booleanRZ1r = unpack("B", f.read(1))[0]==True
            booleanSX1r = unpack("B", f.read(1))[0]==True
            booleanSY1r = unpack("B", f.read(1))[0]==True
            booleanSZ1r = unpack("B", f.read(1))[0]==True

            booleanPX1s = unpack("B", f.read(1))[0]==True
            booleanPY1s = unpack("B", f.read(1))[0]==True
            booleanPZ1s = unpack("B", f.read(1))[0]==True
            booleanRX1s = unpack("B", f.read(1))[0]==True
            booleanRY1s = unpack("B", f.read(1))[0]==True
            booleanRZ1s = unpack("B", f.read(1))[0]==True
            booleanSX1s = unpack("B", f.read(1))[0]==True
            booleanSY1s = unpack("B", f.read(1))[0]==True
            booleanSZ1s = unpack("B", f.read(1))[0]==True

            booleanPX1t = unpack("B", f.read(1))[0]==True
            booleanPY1t = unpack("B", f.read(1))[0]==True
            booleanPZ1t = unpack("B", f.read(1))[0]==True
            booleanRX1t = unpack("B", f.read(1))[0]==True
            booleanRY1t = unpack("B", f.read(1))[0]==True
            booleanRZ1t = unpack("B", f.read(1))[0]==True
            booleanSX1t = unpack("B", f.read(1))[0]==True
            booleanSY1t = unpack("B", f.read(1))[0]==True
            booleanSZ1t = unpack("B", f.read(1))[0]==True

            if booleanPX1o > 0:
                f.seek(posxOn15,0)
                f.seek(-32,1)
                Size379 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size380 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size381 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size379:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx14 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx14
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1o > 0:
                f.seek(posyOn15,0)
                f.seek(-32,1)
                Size382 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size383 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size384 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size382:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy14 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy14
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1o > 0:
                f.seek(poszOn15,0)
                f.seek(-32,1)
                Size385 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size386 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size387 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size385:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz14 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz14
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1o > 0:
                f.seek(rotxOn15,0)
                f.seek(-32,1)
                Size388 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size389 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size390 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size388:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx14 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx14
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1o > 0:
                f.seek(rotyOn15,0)
                f.seek(-32,1)
                Size391 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size392 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size393 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size391:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz14 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz14
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1o > 0:
                f.seek(rotzOn15,0)
                f.seek(-32,1)
                Size394 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size395 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size396 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size394:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty14 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty14
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1o > 0:
                f.seek(sclxOn15,0)
                f.seek(-32,1)
                Size397 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size398 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size399 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size397:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx14 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx14
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1o > 0:
                f.seek(sclyOn15,0)
                f.seek(-32,1)
                Size400 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size401 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size402 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size400:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly14 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly14
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1o > 0:
                f.seek(sclzOn15,0)
                f.seek(-32,1)
                Size403 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size404 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size405 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size403:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz14 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz14
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1p > 0:
                f.seek(posxOn16,0)
                f.seek(-32,1)
                Size406 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size407 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size408 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size406:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx15 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx15
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1p > 0:
                f.seek(posyOn16,0)
                f.seek(-32,1)
                Size409 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size410 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size411 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size409:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy15 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy15
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1p > 0:
                f.seek(poszOn16,0)
                f.seek(-32,1)
                Size412 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size413 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size414 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size412:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz15 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz15
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1p > 0:
                f.seek(rotxOn16,0)
                f.seek(-32,1)
                Size415 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size416 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size417 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size415:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx15 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx15
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1p > 0:
                f.seek(rotyOn16,0)
                f.seek(-32,1)
                Size418 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size419 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size420 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size418:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz15 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz15
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1p > 0:
                f.seek(rotzOn16,0)
                f.seek(-32,1)
                Size421 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size422 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size423 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size421:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty15 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty15
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1p > 0:
                f.seek(sclxOn16,0)
                f.seek(-32,1)
                Size424 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size425 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size426 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size424:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx15 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx15
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1p > 0:
                f.seek(sclyOn16,0)
                f.seek(-32,1)
                Size427 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size428 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size429 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size427:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly15 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly15
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1p > 0:
                f.seek(sclzOn16,0)
                f.seek(-32,1)
                Size430 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size431 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size432 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size430:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz15 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz15
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1q > 0:
                f.seek(posxOn17,0)
                f.seek(-32,1)
                Size433 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size434 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size435 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size433:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx16 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx16
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1q > 0:
                f.seek(posyOn17,0)
                f.seek(-32,1)
                Size436 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size437 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size438 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size436:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy16 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy16
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1q > 0:
                f.seek(poszOn17,0)
                f.seek(-32,1)
                Size439 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size440 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size441 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size439:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz16 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz16
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1q > 0:
                f.seek(rotxOn17,0)
                f.seek(-32,1)
                Size442 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size443 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size444 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size442:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx16 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx16
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1q > 0:
                f.seek(rotyOn17,0)
                f.seek(-32,1)
                Size445 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size446 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size447 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size445:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz16 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz16
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1q > 0:
                f.seek(rotzOn17,0)
                f.seek(-32,1)
                Size448 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size449 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size450 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size448:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty16 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty16
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1q > 0:
                f.seek(sclxOn17,0)
                f.seek(-32,1)
                Size451 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size452 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size453 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size451:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx16 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx16
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1q > 0:
                f.seek(sclyOn17,0)
                f.seek(-32,1)
                Size454 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size455 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size456 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size454:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly16 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly16
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1q > 0:
                f.seek(sclzOn17,0)
                f.seek(-32,1)
                Size457 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size458 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size459 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size457:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz16 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz16
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1r > 0:
                f.seek(posxOn18,0)
                f.seek(-32,1)
                Size460 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size461 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size462 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size460:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx17 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx17
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1r > 0:
                f.seek(posyOn18,0)
                f.seek(-32,1)
                Size463 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size464 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size465 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size463:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy17 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy17
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1r > 0:
                f.seek(poszOn18,0)
                f.seek(-32,1)
                Size466 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size467 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size468 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size466:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz17 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz17
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1r > 0:
                f.seek(rotxOn18,0)
                f.seek(-32,1)
                Size469 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size470 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size471 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size469:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx17 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx17
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1r > 0:
                f.seek(rotyOn18,0)
                f.seek(-32,1)
                Size472 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size473 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size474 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size472:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz17 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz17
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1r > 0:
                f.seek(rotzOn18,0)
                f.seek(-32,1)
                Size475 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size476 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size477 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size475:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty17 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty17
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1r > 0:
                f.seek(sclxOn18,0)
                f.seek(-32,1)
                Size478 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size479 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size480 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size478:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx17 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx17
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1r > 0:
                f.seek(sclyOn18,0)
                f.seek(-32,1)
                Size481 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size482 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size483 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size481:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly17 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly17
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1r > 0:
                f.seek(sclzOn18,0)
                f.seek(-32,1)
                Size484 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size485 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size486 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size484:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz17 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz17
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1s > 0:
                f.seek(posxOn19,0)
                f.seek(-32,1)
                Size487 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size488 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size489 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size487:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx18 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx18
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1s > 0:
                f.seek(posyOn19,0)
                f.seek(-32,1)
                Size490 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size491 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size492 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size490:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy18 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy18
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1s > 0:
                f.seek(poszOn19,0)
                f.seek(-32,1)
                Size493 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size494 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size495 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size493:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz18 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz18
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1s > 0:
                f.seek(rotxOn19,0)
                f.seek(-32,1)
                Size496 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size497 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size498 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size496:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx18 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx18
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1s > 0:
                f.seek(rotyOn19,0)
                f.seek(-32,1)
                Size499 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size500 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size501 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size499:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz18 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz18
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1s > 0:
                f.seek(rotzOn19,0)
                f.seek(-32,1)
                Size502 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size503 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size504 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size502:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty18 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty18
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1s > 0:
                f.seek(sclxOn19,0)
                f.seek(-32,1)
                Size505 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size506 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size507 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size505:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx18 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx18
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1s > 0:
                f.seek(sclyOn19,0)
                f.seek(-32,1)
                Size508 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size509 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size510 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size508:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly18 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly18
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1s > 0:
                f.seek(sclzOn19,0)
                f.seek(-32,1)
                Size511 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size512 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size513 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size511:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz18 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz18
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1t > 0:
                f.seek(posxOn20,0)
                f.seek(-32,1)
                Size514 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size515 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size516 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size514:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx19 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.x = posx19
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1t > 0:
                f.seek(posyOn20,0)
                f.seek(-32,1)
                Size517 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size518 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size519 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size517:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy19 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.y = posy19
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1t > 0:
                f.seek(poszOn20,0)
                f.seek(-32,1)
                Size520 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size521 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size522 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size520:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz19 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.z = posz19
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1t > 0:
                f.seek(rotxOn20,0)
                f.seek(-32,1)
                Size523 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size524 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size525 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size523:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx19 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.x = rotx19
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1t > 0:
                f.seek(rotyOn20,0)
                f.seek(-32,1)
                Size526 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size527 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size528 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size526:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz19 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.z = rotz19
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1t > 0:
                f.seek(rotzOn20,0)
                f.seek(-32,1)
                Size529 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size530 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size531 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size529:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty19 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.y = roty19
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1t > 0:
                f.seek(sclxOn20,0)
                f.seek(-32,1)
                Size532 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size533 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size534 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size532:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx19 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.x = sclx19
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1t > 0:
                f.seek(sclyOn20,0)
                f.seek(-32,1)
                Size535 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size536 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size537 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size535:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly19 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.y = scly19
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1t > 0:
                f.seek(sclzOn20,0)
                f.seek(-32,1)
                Size538 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size539 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size540 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size538:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz19 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.z = sclz19
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 7:
            posxOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn21 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn22 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn23 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn24 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn25 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn26 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn27 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1u = unpack("B", f.read(1))[0]==True
            booleanPY1u = unpack("B", f.read(1))[0]==True
            booleanPZ1u = unpack("B", f.read(1))[0]==True
            booleanRX1u = unpack("B", f.read(1))[0]==True
            booleanRY1u = unpack("B", f.read(1))[0]==True
            booleanRZ1u = unpack("B", f.read(1))[0]==True
            booleanSX1u = unpack("B", f.read(1))[0]==True
            booleanSY1u = unpack("B", f.read(1))[0]==True
            booleanSZ1u = unpack("B", f.read(1))[0]==True

            booleanPX1v = unpack("B", f.read(1))[0]==True
            booleanPY1v = unpack("B", f.read(1))[0]==True
            booleanPZ1v = unpack("B", f.read(1))[0]==True
            booleanRX1v = unpack("B", f.read(1))[0]==True
            booleanRY1v = unpack("B", f.read(1))[0]==True
            booleanRZ1v = unpack("B", f.read(1))[0]==True
            booleanSX1v = unpack("B", f.read(1))[0]==True
            booleanSY1v = unpack("B", f.read(1))[0]==True
            booleanSZ1v = unpack("B", f.read(1))[0]==True

            booleanPX1w = unpack("B", f.read(1))[0]==True
            booleanPY1w = unpack("B", f.read(1))[0]==True
            booleanPZ1w = unpack("B", f.read(1))[0]==True
            booleanRX1w = unpack("B", f.read(1))[0]==True
            booleanRY1w = unpack("B", f.read(1))[0]==True
            booleanRZ1w = unpack("B", f.read(1))[0]==True
            booleanSX1w = unpack("B", f.read(1))[0]==True
            booleanSY1w = unpack("B", f.read(1))[0]==True
            booleanSZ1w = unpack("B", f.read(1))[0]==True

            booleanPX1x = unpack("B", f.read(1))[0]==True
            booleanPY1x = unpack("B", f.read(1))[0]==True
            booleanPZ1x = unpack("B", f.read(1))[0]==True
            booleanRX1x = unpack("B", f.read(1))[0]==True
            booleanRY1x = unpack("B", f.read(1))[0]==True
            booleanRZ1x = unpack("B", f.read(1))[0]==True
            booleanSX1x = unpack("B", f.read(1))[0]==True
            booleanSY1x = unpack("B", f.read(1))[0]==True
            booleanSZ1x = unpack("B", f.read(1))[0]==True

            booleanPX1y = unpack("B", f.read(1))[0]==True
            booleanPY1y = unpack("B", f.read(1))[0]==True
            booleanPZ1y = unpack("B", f.read(1))[0]==True
            booleanRX1y = unpack("B", f.read(1))[0]==True
            booleanRY1y = unpack("B", f.read(1))[0]==True
            booleanRZ1y = unpack("B", f.read(1))[0]==True
            booleanSX1y = unpack("B", f.read(1))[0]==True
            booleanSY1y = unpack("B", f.read(1))[0]==True
            booleanSZ1y = unpack("B", f.read(1))[0]==True

            booleanPX1z = unpack("B", f.read(1))[0]==True
            booleanPY1z = unpack("B", f.read(1))[0]==True
            booleanPZ1z = unpack("B", f.read(1))[0]==True
            booleanRX1z = unpack("B", f.read(1))[0]==True
            booleanRY1z = unpack("B", f.read(1))[0]==True
            booleanRZ1z = unpack("B", f.read(1))[0]==True
            booleanSX1z = unpack("B", f.read(1))[0]==True
            booleanSY1z = unpack("B", f.read(1))[0]==True
            booleanSZ1z = unpack("B", f.read(1))[0]==True

            booleanPX1zz = unpack("B", f.read(1))[0]==True
            booleanPY1zz = unpack("B", f.read(1))[0]==True
            booleanPZ1zz = unpack("B", f.read(1))[0]==True
            booleanRX1zz = unpack("B", f.read(1))[0]==True
            booleanRY1zz = unpack("B", f.read(1))[0]==True
            booleanRZ1zz = unpack("B", f.read(1))[0]==True
            booleanSX1zz = unpack("B", f.read(1))[0]==True
            booleanSY1zz = unpack("B", f.read(1))[0]==True
            booleanSZ1zz = unpack("B", f.read(1))[0]==True

            if booleanPX1u > 0:
                f.seek(posxOn21,0)
                f.seek(-32,1)
                Size541 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size542 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size543 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size541:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx20 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx20
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1u > 0:
                f.seek(posyOn21,0)
                f.seek(-32,1)
                Size544 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size545 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size546 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size544:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy20 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy20
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1u > 0:
                f.seek(poszOn21,0)
                f.seek(-32,1)
                Size547 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size548 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size549 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size547:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz20 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz20
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1u > 0:
                f.seek(rotxOn21,0)
                f.seek(-32,1)
                Size550 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size551 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size552 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size550:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx20 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx20
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1u > 0:
                f.seek(rotyOn21,0)
                f.seek(-32,1)
                Size553 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size554 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size555 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size553:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz20 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz20
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1u > 0:
                f.seek(rotzOn21,0)
                f.seek(-32,1)
                Size556 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size557 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size558 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size556:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty20 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty20
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1u > 0:
                f.seek(sclxOn21,0)
                f.seek(-32,1)
                Size559 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size560 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size561 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size559:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx20 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx20
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1u > 0:
                f.seek(sclyOn21,0)
                f.seek(-32,1)
                Size562 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size563 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size564 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size562:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly20 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly20
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1u > 0:
                f.seek(sclzOn21,0)
                f.seek(-32,1)
                Size565 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size566 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size567 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size565:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz20 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz20
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1v > 0:
                f.seek(posxOn22,0)
                f.seek(-32,1)
                Size568 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size569 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size570 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size568:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx21 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx21
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1v > 0:
                f.seek(posyOn22,0)
                f.seek(-32,1)
                Size571 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size572 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size573 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size571:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy21 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy21
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1v > 0:
                f.seek(poszOn22,0)
                f.seek(-32,1)
                Size574 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size575 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size576 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size574:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz21 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz21
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1v > 0:
                f.seek(rotxOn22,0)
                f.seek(-32,1)
                Size577 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size578 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size579 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size577:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx21 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx21
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1v > 0:
                f.seek(rotyOn22,0)
                f.seek(-32,1)
                Size580 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size581 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size582 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size580:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz21 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz21
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1v > 0:
                f.seek(rotzOn22,0)
                f.seek(-32,1)
                Size583 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size584 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size585 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size583:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty21 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty21
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1v > 0:
                f.seek(sclxOn22,0)
                f.seek(-32,1)
                Size586 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size587 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size588 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size586:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx21 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx21
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1v > 0:
                f.seek(sclyOn22,0)
                f.seek(-32,1)
                Size589 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size590 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size591 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size589:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly21 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly21
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1v > 0:
                f.seek(sclzOn22,0)
                f.seek(-32,1)
                Size592 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size593 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size594 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size592:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz21 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz21
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1w > 0:
                f.seek(posxOn23,0)
                f.seek(-32,1)
                Size595 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size596 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size597 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size595:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx22 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx22
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1w > 0:
                f.seek(posyOn23,0)
                f.seek(-32,1)
                Size598 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size599 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size600 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size598:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy22 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy22
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1w > 0:
                f.seek(poszOn23,0)
                f.seek(-32,1)
                Size601 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size602 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size603 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size601:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz22 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz22
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1w > 0:
                f.seek(rotxOn23,0)
                f.seek(-32,1)
                Size604 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size605 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size606 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size604:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx22 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx22
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1w > 0:
                f.seek(rotyOn23,0)
                f.seek(-32,1)
                Size607 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size608 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size609 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size607:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz22 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz22
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1w > 0:
                f.seek(rotzOn23,0)
                f.seek(-32,1)
                Size610 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size611 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size612 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size610:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty22 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty22
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1w > 0:
                f.seek(sclxOn23,0)
                f.seek(-32,1)
                Size613 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size614 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size615 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size613:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx22 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx22
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1w > 0:
                f.seek(sclyOn23,0)
                f.seek(-32,1)
                Size616 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size617 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size618 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size616:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly22 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly22
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1w > 0:
                f.seek(sclzOn23,0)
                f.seek(-32,1)
                Size619 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size620 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size621 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size619:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz22 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz22
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1x > 0:
                f.seek(posxOn24,0)
                f.seek(-32,1)
                Size622 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size623 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size624 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size622:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx23 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx23
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1x > 0:
                f.seek(posyOn24,0)
                f.seek(-32,1)
                Size625 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size626 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size627 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size625:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy23 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy23
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1x > 0:
                f.seek(poszOn24,0)
                f.seek(-32,1)
                Size628 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size629 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size630 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size628:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz23 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz23
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1x > 0:
                f.seek(rotxOn24,0)
                f.seek(-32,1)
                Size631 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size632 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size633 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size631:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx23 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx23
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1x > 0:
                f.seek(rotyOn24,0)
                f.seek(-32,1)
                Size634 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size635 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size636 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size634:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz23 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz23
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1x > 0:
                f.seek(rotzOn24,0)
                f.seek(-32,1)
                Size637 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size638 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size639 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size637:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty23 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty23
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1x > 0:
                f.seek(sclxOn24,0)
                f.seek(-32,1)
                Size640 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size641 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size642 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size640:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx23 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx23
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1x > 0:
                f.seek(sclyOn24,0)
                f.seek(-32,1)
                Size643 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size644 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size645 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size643:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly23 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly23
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1x > 0:
                f.seek(sclzOn24,0)
                f.seek(-32,1)
                Size646 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size647 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size648 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size646:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz23 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz23
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1y > 0:
                f.seek(posxOn25,0)
                f.seek(-32,1)
                Size649 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size650 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size651 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size649:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx24 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx24
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1y > 0:
                f.seek(posyOn25,0)
                f.seek(-32,1)
                Size652 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size653 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size654 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size652:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy24 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy24
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1y > 0:
                f.seek(poszOn25,0)
                f.seek(-32,1)
                Size655 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size656 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size657 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size655:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz24 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz24
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1y > 0:
                f.seek(rotxOn25,0)
                f.seek(-32,1)
                Size658 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size659 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size660 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size658:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx24 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx24
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1y > 0:
                f.seek(rotyOn25,0)
                f.seek(-32,1)
                Size661 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size662 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size663 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size661:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz24 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz24
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1y > 0:
                f.seek(rotzOn25,0)
                f.seek(-32,1)
                Size664 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size665 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size666 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size664:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty24 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty24
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1y > 0:
                f.seek(sclxOn25,0)
                f.seek(-32,1)
                Size667 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size668 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size669 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size667:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx24 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx24
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1y > 0:
                f.seek(sclyOn25,0)
                f.seek(-32,1)
                Size670 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size671 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size672 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size670:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly24 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly24
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1y > 0:
                f.seek(sclzOn25,0)
                f.seek(-32,1)
                Size673 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size674 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size675 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size673:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz24 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz24
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1z > 0:
                f.seek(posxOn26,0)
                f.seek(-32,1)
                Size676 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size677 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size678 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size676:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx25 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.x = posx25
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1z > 0:
                f.seek(posyOn26,0)
                f.seek(-32,1)
                Size679 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size680 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size681 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size679:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy25 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.y = posy25
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1z > 0:
                f.seek(poszOn26,0)
                f.seek(-32,1)
                Size682 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size683 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size684 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size682:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz25 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.z = posz25
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1z > 0:
                f.seek(rotxOn26,0)
                f.seek(-32,1)
                Size685 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size686 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size687 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size685:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx25 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.x = rotx25
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1z > 0:
                f.seek(rotyOn26,0)
                f.seek(-32,1)
                Size688 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size689 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size690 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size688:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz25 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.z = rotz25
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1z > 0:
                f.seek(rotzOn26,0)
                f.seek(-32,1)
                Size691 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size692 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size693 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size691:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty25 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.y = roty25
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1z > 0:
                f.seek(sclxOn26,0)
                f.seek(-32,1)
                Size694 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size695 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size696 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size694:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx25 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.x = sclx25
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1z > 0:
                f.seek(sclyOn26,0)
                f.seek(-32,1)
                Size697 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size698 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size699 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size697:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly25 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.y = scly25
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1z > 0:
                f.seek(sclzOn26,0)
                f.seek(-32,1)
                Size700 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size701 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size702 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size700:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz25 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.z = sclz25
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zz > 0:
                f.seek(posxOn27,0)
                f.seek(-32,1)
                Size703 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size704 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size705 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size703:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx26 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.x = posx26
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zz > 0:
                f.seek(posyOn27,0)
                f.seek(-32,1)
                Size706 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size707 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size708 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size706:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy26 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.y = posy26
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zz > 0:
                f.seek(poszOn27,0)
                f.seek(-32,1)
                Size709 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size710 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size711 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size709:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz26 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.z = posz26
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zz > 0:
                f.seek(rotxOn27,0)
                f.seek(-32,1)
                Size712 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size713 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size714 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size712:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx26 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.x = rotx26
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zz > 0:
                f.seek(rotyOn27,0)
                f.seek(-32,1)
                Size715 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size716 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size717 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size715:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz26 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.z = rotz26
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zz > 0:
                f.seek(rotzOn27,0)
                f.seek(-32,1)
                Size718 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size719 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size720 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size718:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty26 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.y = roty26
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zz > 0:
                f.seek(sclxOn27,0)
                f.seek(-32,1)
                Size721 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size722 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size723 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size721:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx26 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.x = sclx26
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zz > 0:
                f.seek(sclyOn27,0)
                f.seek(-32,1)
                Size724 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size725 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size726 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size724:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly26 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.y = scly26
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zz > 0:
                f.seek(sclzOn27,0)
                f.seek(-32,1)
                Size727 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size728 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size729 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size727:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz26 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.z = sclz26
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 8:
            posxOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn28 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn29 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn30 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn31 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn32 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn33 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn34 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn35 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1zzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzz = unpack("B", f.read(1))[0]==True

            if booleanPX1zzz > 0:
                f.seek(posxOn28,0)
                f.seek(-32,1)
                Size730 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size731 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size732 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size730:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx27 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx27
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzz > 0:
                f.seek(posyOn28,0)
                f.seek(-32,1)
                Size733 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size734 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size735 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size733:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy27 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy27
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzz > 0:
                f.seek(poszOn28,0)
                f.seek(-32,1)
                Size736 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size737 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size738 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size736:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz27 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz27
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzz > 0:
                f.seek(rotxOn28,0)
                f.seek(-32,1)
                Size739 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size740 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size741 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size739:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx27 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx27
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzz > 0:
                f.seek(rotyOn28,0)
                f.seek(-32,1)
                Size742 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size743 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size744 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size742:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz27 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz27
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzz > 0:
                f.seek(rotzOn28,0)
                f.seek(-32,1)
                Size745 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size746 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size747 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size745:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty27 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty27
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzz > 0:
                f.seek(sclxOn28,0)
                f.seek(-32,1)
                Size748 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size749 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size750 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size748:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx27 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx27
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))
            if booleanSY1zzz > 0:
                f.seek(sclyOn28,0)
                f.seek(-32,1)
                Size751 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size752 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size753 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size751:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly27 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly27
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzz > 0:
                f.seek(sclzOn28,0)
                f.seek(-32,1)
                Size754 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size755 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size756 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size754:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz27 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz27
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzz > 0:
                f.seek(posxOn29,0)
                f.seek(-32,1)
                Size757 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size758 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size759 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size757:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx28 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx28
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzz > 0:
                f.seek(posyOn29,0)
                f.seek(-32,1)
                Size760 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size761 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size762 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size760:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy28 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy28
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzz > 0:
                f.seek(poszOn29,0)
                f.seek(-32,1)
                Size763 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size764 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size765 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size763:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz28 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz28
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzz > 0:
                f.seek(rotxOn29,0)
                f.seek(-32,1)
                Size766 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size767 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size768 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size766:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx28 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx28
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzz > 0:
                f.seek(rotyOn29,0)
                f.seek(-32,1)
                Size769 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size770 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size771 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size769:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz28 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz28
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzz > 0:
                f.seek(rotzOn29,0)
                f.seek(-32,1)
                Size772 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size773 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size774 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size772:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty28 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty28
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzz > 0:
                f.seek(sclxOn29,0)
                f.seek(-32,1)
                Size775 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size776 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size777 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size775:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx28 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx28
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzz > 0:
                f.seek(sclyOn29,0)
                f.seek(-32,1)
                Size778 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size779 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size780 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size778:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly28 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly28
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzz > 0:
                f.seek(sclzOn29,0)
                f.seek(-32,1)
                Size781 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size782 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size783 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size781:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz28 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz28
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzz > 0:
                f.seek(posxOn30,0)
                f.seek(-32,1)
                Size784 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size785 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size786 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size784:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx29 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx29
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzz > 0:
                f.seek(posyOn30,0)
                f.seek(-32,1)
                Size787 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size788 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size789 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size787:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy29 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy29
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))
                    
                        

def ani_importer_read(filepath, Beta_ani=False, Norm_ani=False):
    with open(filepath,"rb") as f:
        ani_importV2(f)

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        pass
                    
        
    

