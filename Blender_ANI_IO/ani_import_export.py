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

            if booleanPZ1zzzzz > 0:
                f.seek(poszOn30,0)
                f.seek(-32,1)
                Size790 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size791 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size792 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size790:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz29 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz29
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzz > 0:
                f.seek(rotxOn30,0)
                f.seek(-32,1)
                Size793 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size794 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size795 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size793:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx29 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx29
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzz > 0:
                f.seek(rotyOn30,0)
                f.seek(-32,1)
                Size796 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size797 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size798 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size796:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz29 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz29
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzz > 0:
                f.seek(rotzOn30,0)
                f.seek(-32,1)
                Size799 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size800 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size801 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size799:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty29 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty29
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzz > 0:
                f.seek(sclxOn30,0)
                f.seek(-32,1)
                Size802 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size803 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size804 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size802:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx29 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx29
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzz > 0:
                f.seek(sclyOn30,0)
                f.seek(-32,1)
                Size805 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size806 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size807 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size805:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly29 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly29
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzz > 0:
                f.seek(sclzOn30,0)
                f.seek(-32,1)
                Size808 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size809 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size810 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size808:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz29 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz29
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzz > 0:
                f.seek(posxOn31,0)
                f.seek(-32,1)
                Size811 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size812 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size813 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size811:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx30 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx30
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzz > 0:
                f.seek(posyOn31,0)
                f.seek(-32,1)
                Size814 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size815 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size816 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size814:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy30 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy30
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzz > 0:
                f.seek(poszOn31,0)
                f.seek(-32,1)
                Size817 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size818 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size819 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size817:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz30 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz30
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzz > 0:
                f.seek(rotxOn31,0)
                f.seek(-32,1)
                Size820 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size821 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size822 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size820:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx30 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx30
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzz > 0:
                f.seek(rotyOn31,0)
                f.seek(-32,1)
                Size823 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size824 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size825 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size823:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz30 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz30
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzz > 0:
                f.seek(rotzOn31,0)
                f.seek(-32,1)
                Size826 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size827 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size828 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size826:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty30 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty30
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzz > 0:
                f.seek(sclxOn31,0)
                f.seek(-32,1)
                Size829 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size830 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size831 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size829:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx30 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx30
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzz > 0:
                f.seek(sclyOn31,0)
                f.seek(-32,1)
                Size832 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size833 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size834 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size832:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly30 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly30
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzz > 0:
                f.seek(sclzOn31,0)
                f.seek(-32,1)
                Size835 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size836 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size837 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size835:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz30 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz30
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzz > 0:
                f.seek(posxOn32,0)
                f.seek(-32,1)
                Size838 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size839 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size840 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size838:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx31 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx31
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzz > 0:
                f.seek(posyOn32,0)
                f.seek(-32,1)
                Size841 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size842 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size843 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size841:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy31 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy31
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzz > 0:
                f.seek(poszOn32,0)
                f.seek(-32,1)
                Size844 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size845 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size846 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size844:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz31 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz31
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzz > 0:
                f.seek(rotxOn32,0)
                f.seek(-32,1)
                Size847 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size848 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size849 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size847:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx31 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx31
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzz > 0:
                f.seek(rotyOn32,0)
                f.seek(-32,1)
                Size850 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size851 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size852 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size850:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz31 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz31
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzz > 0:
                f.seek(rotzOn32,0)
                f.seek(-32,1)
                Size853 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size854 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size855 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size853:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty31 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty31
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzz > 0:
                f.seek(sclxOn32,0)
                f.seek(-32,1)
                Size856 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size857 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size858 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size856:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx31 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx31
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzz > 0:
                f.seek(sclyOn32,0)
                f.seek(-32,1)
                Size859 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size860 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size861 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size859:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly31 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly31
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzz > 0:
                f.seek(sclzOn32,0)
                f.seek(-32,1)
                Size862 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size863 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size864 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size862:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz31 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz31
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzz > 0:
                f.seek(posxOn33,0)
                f.seek(-32,1)
                Size865 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size866 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size867 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size865:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx32 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.x = posx32
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzz > 0:
                f.seek(posyOn33,0)
                f.seek(-32,1)
                Size868 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size869 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size870 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size868:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy32 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.y = posy32
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzz > 0:
                f.seek(poszOn33,0)
                f.seek(-32,1)
                Size871 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size872 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size873 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size871:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz32 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.z = posz32
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzz > 0:
                f.seek(rotxOn33,0)
                f.seek(-32,1)
                Size874 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size875 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size876 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size874:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx32 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.x = rotx32
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzz > 0:
                f.seek(rotyOn33,0)
                f.seek(-32,1)
                Size877 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size878 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size879 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size877:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz32 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.z = rotz32
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzz > 0:
                f.seek(rotzOn33,0)
                f.seek(-32,1)
                Size880 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size881 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size882 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size880:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty32 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.y = roty32
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzz > 0:
                f.seek(sclxOn33,0)
                f.seek(-32,1)
                Size883 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size884 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size885 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size883:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx32 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.x = sclx32
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzz > 0:
                f.seek(sclyOn33,0)
                f.seek(-32,1)
                Size886 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size887 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size888 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size886:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly32 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.y = scly32
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzz > 0:
                f.seek(sclzOn33,0)
                f.seek(-32,1)
                Size889 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size890 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size891 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size889:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz32 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.z = sclz32
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzz > 0:
                f.seek(posxOn34,0)
                f.seek(-32,1)
                Size892 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size893 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size894 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size892:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx33 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.x = posx33
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzz > 0:
                f.seek(posyOn34,0)
                f.seek(-32,1)
                Size895 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size896 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size897 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size895:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy33 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.y = posy33
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzz > 0:
                f.seek(poszOn34,0)
                f.seek(-32,1)
                Size898 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size899 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size900 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size898:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz33 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.z = posz33
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzz > 0:
                f.seek(rotxOn34,0)
                f.seek(-32,1)
                Size901 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size902 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size903 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size901:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx33 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.x = rotx33
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzz > 0:
                f.seek(rotyOn34,0)
                f.seek(-32,1)
                Size904 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size905 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size906 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size904:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz33 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.z = rotz33
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzz > 0:
                f.seek(rotzOn34,0)
                f.seek(-32,1)
                Size907 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size908 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size909 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size907:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty33 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.y = roty33
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzz > 0:
                f.seek(sclxOn34,0)
                f.seek(-32,1)
                Size910 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size911 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size912 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size910:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx33 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.x = sclx33
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzz > 0:
                f.seek(sclyOn34,0)
                f.seek(-32,1)
                Size913 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size914 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size915 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size913:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly33 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.y = scly33
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzz > 0:
                f.seek(sclzOn34,0)
                f.seek(-32,1)
                Size916 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size917 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size918 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size916:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz33 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.z = sclz33
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzz > 0:
                f.seek(posxOn35,0)
                f.seek(-32,1)
                Size919 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size920 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size921 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size919:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx34 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.x = posx34
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzz > 0:
                f.seek(posyOn35,0)
                f.seek(-32,1)
                Size922 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size923 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size924 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size922:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy34 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.y = posy34
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzz > 0:
                f.seek(poszOn35,0)
                f.seek(-32,1)
                Size925 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size926 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size927 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size925:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz34 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.z = posz34
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzz > 0:
                f.seek(rotxOn35,0)
                f.seek(-32,1)
                Size928 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size929 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size930 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size928:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx34 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.x = rotx34
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzz > 0:
                f.seek(rotyOn35,0)
                f.seek(-32,1)
                Size931 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size932 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size933 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size931:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz34 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.z = rotz34
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzz > 0:
                f.seek(rotzOn35,0)
                f.seek(-32,1)
                Size934 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size935 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size936 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size934:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty34 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.y = roty34
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzz > 0:
                f.seek(sclxOn35,0)
                f.seek(-32,1)
                Size937 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size938 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size939 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size937:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx34 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.x = sclx34
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzz > 0:
                f.seek(sclyOn35,0)
                f.seek(-32,1)
                Size940 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size941 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size942 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size940:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly34 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.y = scly34
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzz > 0:
                f.seek(sclzOn35,0)
                f.seek(-32,1)
                Size943 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size944 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size945 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size943:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz34 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.z = sclz34
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 9:
            posxOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn36 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn37 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn38 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn39 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn40 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn41 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn42 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn43 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn44 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            if booleanPX1zzzzzzzzzzz > 0:
                f.seek(posxOn36,0)
                f.seek(-32,1)
                Size946 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size947 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size948 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size946:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx35 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx35
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzz > 0:
                f.seek(posyOn36,0)
                f.seek(-32,1)
                Size949 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size950 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size951 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size949:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy35 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy35
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzz > 0:
                f.seek(poszOn36,0)
                f.seek(-32,1)
                Size952 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size953 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size954 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size952:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz35 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz35
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzz > 0:
                f.seek(rotxOn36,0)
                f.seek(-32,1)
                Size955 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size956 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size957 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size955:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx35 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx35
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzz > 0:
                f.seek(rotyOn36,0)
                f.seek(-32,1)
                Size958 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size959 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size960 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size958:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz35 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz35
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzz > 0:
                f.seek(rotzOn36,0)
                f.seek(-32,1)
                Size961 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size962 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size963 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size961:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty35 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty35
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzz > 0:
                f.seek(sclxOn36,0)
                f.seek(-32,1)
                Size964 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size965 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size966 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size964:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx35 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx35
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzz > 0:
                f.seek(sclyOn36,0)
                f.seek(-32,1)
                Size967 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size968 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size969 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size967:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly35 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly35
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzz > 0:
                f.seek(sclzOn36,0)
                f.seek(-32,1)
                Size970 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size971 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size972 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size970:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz35 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz35
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzz > 0:
                f.seek(posxOn37,0)
                f.seek(-32,1)
                Size973 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size974 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size975 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size973:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx36 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx36
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzz > 0:
                f.seek(posyOn37,0)
                f.seek(-32,1)
                Size976 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size977 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size978 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size976:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy36 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy36
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzz > 0:
                f.seek(poszOn37,0)
                f.seek(-32,1)
                Size979 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size980 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size981 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size979:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz36 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz36
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))
            if booleanRX1zzzzzzzzzzzz > 0:
                f.seek(rotxOn37,0)
                f.seek(-32,1)
                Size982 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size983 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size984 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size982:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx36 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx36
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzz > 0:
                f.seek(rotyOn37,0)
                f.seek(-32,1)
                Size985 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size986 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size987 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size985:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz36 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz36
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzz > 0:
                f.seek(rotzOn37,0)
                f.seek(-32,1)
                Size988 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size989 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size990 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size988:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty36 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty36
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzz > 0:
                f.seek(sclxOn37,0)
                f.seek(-32,1)
                Size991 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size992 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size993 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size991:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx36 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx36
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzz > 0:
                f.seek(sclyOn37,0)
                f.seek(-32,1)
                Size994 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size995 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size996 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size994:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly36 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly36
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzz > 0:
                f.seek(sclzOn37,0)
                f.seek(-32,1)
                Size997 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size998 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size999 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size997:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz36 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz36
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzz > 0:
                f.seek(posxOn38,0)
                f.seek(-32,1)
                Size1000 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1001 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1002 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1000:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx37 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx37
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzz > 0:
                f.seek(posyOn38,0)
                f.seek(-32,1)
                Size1003 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1004 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1005 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1003:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy37 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy37
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzz > 0:
                f.seek(poszOn38,0)
                f.seek(-32,1)
                Size1006 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1007 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1008 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1006:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz37 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz37
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzz > 0:
                f.seek(rotxOn38,0)
                f.seek(-32,1)
                Size1009 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1010 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1011 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1009:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx37 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx37
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzz > 0:
                f.seek(rotyOn38,0)
                f.seek(-32,1)
                Size1012 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1013 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1014 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1012:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz37 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz37
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzz > 0:
                f.seek(rotzOn38,0)
                f.seek(-32,1)
                Size1015 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1016 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1017 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1015:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty37 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty37
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzz > 0:
                f.seek(sclxOn38,0)
                f.seek(-32,1)
                Size1018 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1019 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1020 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1018:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx37 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx37
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzz > 0:
                f.seek(sclyOn38,0)
                f.seek(-32,1)
                Size1021 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1022 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1023 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1021:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly37 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly37
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzz > 0:
                f.seek(sclzOn38,0)
                f.seek(-32,1)
                Size1024 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1025 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1026 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1024:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz37 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz37
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzz > 0:
                f.seek(posxOn39,0)
                f.seek(-32,1)
                Size1027 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1028 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1029 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1027:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx38 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx38
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzz > 0:
                f.seek(posyOn39,0)
                f.seek(-32,1)
                Size1030 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1031 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1032 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1030:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy38 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy38
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzz > 0:
                f.seek(poszOn39,0)
                f.seek(-32,1)
                Size1033 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1034 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1035 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1033:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz38 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz38
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzz > 0:
                f.seek(rotxOn39,0)
                f.seek(-32,1)
                Size1036 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1037 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1038 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1036:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx38 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx38
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzz > 0:
                f.seek(rotyOn39,0)
                f.seek(-32,1)
                Size1039 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1040 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1041 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1039:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz38 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz38
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzz > 0:
                f.seek(rotzOn39,0)
                f.seek(-32,1)
                Size1042 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1043 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1044 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1042:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty38 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty38
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzz > 0:
                f.seek(sclxOn39,0)
                f.seek(-32,1)
                Size1045 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1046 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1047 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1045:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx38 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx38
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzz > 0:
                f.seek(sclyOn39,0)
                f.seek(-32,1)
                Size1048 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1049 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1050 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1048:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly38 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly38
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzz > 0:
                f.seek(sclzOn39,0)
                f.seek(-32,1)
                Size1051 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1052 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1053 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1051:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz38 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz38
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzz > 0:
                f.seek(posxOn40,0)
                f.seek(-32,1)
                Size1054 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1055 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1056 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1054:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx39 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx39
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzz > 0:
                f.seek(posyOn40,0)
                f.seek(-32,1)
                Size1057 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1058 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1059 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1057:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy39 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy39
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzz > 0:
                f.seek(poszOn40,0)
                f.seek(-32,1)
                Size1060 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1061 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1062 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1060:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz39 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz39
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn40,0)
                f.seek(-32,1)
                Size1063 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1064 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1065 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1063:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx39 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx39
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn40,0)
                f.seek(-32,1)
                Size1066 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1067 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1068 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1066:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz39 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz39
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn40,0)
                f.seek(-32,1)
                Size1069 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1070 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1071 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1069:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty39 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty39
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn40,0)
                f.seek(-32,1)
                Size1072 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1073 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1074 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1072:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx39 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx39
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn40,0)
                f.seek(-32,1)
                Size1075 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1076 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1077 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1075:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly39 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly39
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn40,0)
                f.seek(-32,1)
                Size1078 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1079 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1080 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1078:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz39 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz39
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn41,0)
                f.seek(-32,1)
                Size1081 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1082 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1083 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1081:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx40 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.x = posx40
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn41,0)
                f.seek(-32,1)
                Size1084 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1085 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1086 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1084:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy40 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.y = posy40
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn41,0)
                f.seek(-32,1)
                Size1087 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1088 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1089 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1087:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz40 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.z = posz40
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn41,0)
                f.seek(-32,1)
                Size1090 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1091 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1092 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1090:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx40 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.x = rotx40
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn41,0)
                f.seek(-32,1)
                Size1093 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1094 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1095 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1093:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz40 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.z = rotz40
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn41,0)
                f.seek(-32,1)
                Size1096 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1097 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1098 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1096:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty40 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.y = roty40
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn41,0)
                f.seek(-32,1)
                Size1099 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1100 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1101 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1099:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx40 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.x = sclx40
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn41,0)
                f.seek(-32,1)
                Size1102 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1103 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1104 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1102:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly40 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.y = scly40
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn41,0)
                f.seek(-32,1)
                Size1105 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1106 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1107 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1105:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz40 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.z = sclz40
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn42,0)
                f.seek(-32,1)
                Size1108 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1109 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1110 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1108:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx41 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.x = posx41
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn42,0)
                f.seek(-32,1)
                Size1111 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1112 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1113 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1111:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy41 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.y = posy41
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn42,0)
                f.seek(-32,1)
                Size1114 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1115 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1116 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1114:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz41 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.z = posz41
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn42,0)
                f.seek(-32,1)
                Size1117 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1118 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1119 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1117:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx41 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.x = rotx41
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn42,0)
                f.seek(-32,1)
                Size1120 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1121 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1122 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1120:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz41 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.z = rotz41
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn42,0)
                f.seek(-32,1)
                Size1123 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1124 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1125 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1123:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty41 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.y = roty41
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn42,0)
                f.seek(-32,1)
                Size1126 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1127 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1128 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1126:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx41 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.x = sclx41
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn42,0)
                f.seek(-32,1)
                Size1129 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1130 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1131 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1129:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly41 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.y = scly41
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn42,0)
                f.seek(-32,1)
                Size1132 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1133 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1134 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1132:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz41 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.z = sclz41
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn43,0)
                f.seek(-32,1)
                Size1135 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1136 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1137 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1135:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx42 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.x = posx42
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn43,0)
                f.seek(-32,1)
                Size1138 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1139 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1140 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1138:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy42 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.y = posy42
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn43,0)
                f.seek(-32,1)
                Size1141 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1142 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1143 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1141:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz42 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.z = posz42
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn43,0)
                f.seek(-32,1)
                Size1144 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1145 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1146 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1144:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx42 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.x = rotx42
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn43,0)
                f.seek(-32,1)
                Size1147 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1148 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1149 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1147:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz42 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.z = rotz42
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn43,0)
                f.seek(-32,1)
                Size1150 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1151 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1152 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1150:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty42 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.y = roty42
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn43,0)
                f.seek(-32,1)
                Size1153 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1154 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1155 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1153:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx42 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.x = sclx42
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn43,0)
                f.seek(-32,1)
                Size1156 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1157 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1158 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1156:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly42 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.y = scly42
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn43,0)
                f.seek(-32,1)
                Size1159 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1160 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1161 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1159:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz42 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.z = sclz42
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn44,0)
                f.seek(-32,1)
                Size1162 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1163 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1164 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1162:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx43 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.x = posx43
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn44,0)
                f.seek(-32,1)
                Size1165 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1166 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1167 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1165:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy43 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.y = posy43
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn44,0)
                f.seek(-32,1)
                Size1168 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1169 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1170 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1168:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz43 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.z = posz43
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn44,0)
                f.seek(-32,1)
                Size1171 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1172 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1173 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1171:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx43 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.x = rotx43
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn44,0)
                f.seek(-32,1)
                Size1174 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1175 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1176 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1174:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz43 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.z = rotz43
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn44,0)
                f.seek(-32,1)
                Size1177 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1178 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1179 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1177:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty43 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.y = roty43
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn44,0)
                f.seek(-32,1)
                Size1180 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1181 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1182 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1180:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx43 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.x = sclx43
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn44,0)
                f.seek(-32,1)
                Size1183 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1184 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1185 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1183:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly43 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.y = scly43
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn44,0)
                f.seek(-32,1)
                Size1186 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1187 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1188 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1186:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz43 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.z = sclz43
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 10:
            posxOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn45 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn46 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn47 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn48 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn49 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn50 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn51 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn52 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn53 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn54 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            if booleanPX1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn45,0)
                f.seek(-32,1)
                Size1189 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1190 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1191 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1189:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx44 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx44
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn45,0)
                f.seek(-32,1)
                Size1192 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1193 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1194 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1192:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy44 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy44
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn45,0)
                f.seek(-32,1)
                Size1195 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1196 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1197 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1195:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz44 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz44
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn45,0)
                f.seek(-32,1)
                Size1198 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1199 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1200 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1198:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx44 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx44
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn45,0)
                f.seek(-32,1)
                Size1201 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1202 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1203 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1201:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz44 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz44
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn45,0)
                f.seek(-32,1)
                Size1204 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1205 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1206 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1204:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty44 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty44
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn45,0)
                f.seek(-32,1)
                Size1207 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1208 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1209 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1207:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx44 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx44
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn45,0)
                f.seek(-32,1)
                Size1210 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1211 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1212 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1210:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly44 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly44
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn45,0)
                f.seek(-32,1)
                Size1213 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1214 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1215 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1213:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz44 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz44
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn46,0)
                f.seek(-32,1)
                Size1216 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1217 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1218 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1216:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx45 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx45
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn46,0)
                f.seek(-32,1)
                Size1219 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1220 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1221 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1219:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy45 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy45
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn46,0)
                f.seek(-32,1)
                Size1222 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1223 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1224 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1222:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz45 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz45
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn46,0)
                f.seek(-32,1)
                Size1225 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1226 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1227 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1225:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx45 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx45
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn46,0)
                f.seek(-32,1)
                Size1228 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1229 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1230 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1228:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz45 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz45
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn46,0)
                f.seek(-32,1)
                Size1231 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1232 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1233 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1231:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty45 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty45
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn46,0)
                f.seek(-32,1)
                Size1234 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1235 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1236 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1234:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx45 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx45
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn46,0)
                f.seek(-32,1)
                Size1237 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1238 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1239 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1237:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly45 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly45
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn46,0)
                f.seek(-32,1)
                Size1240 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1241 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1242 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1240:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz45 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz45
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn47,0)
                f.seek(-32,1)
                Size1243 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1244 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1245 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1243:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx46 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx46
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn47,0)
                f.seek(-32,1)
                Size1246 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1247 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1248 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1246:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy46 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy46
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn47,0)
                f.seek(-32,1)
                Size1249 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1250 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1251 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1249:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz46 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz46
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn47,0)
                f.seek(-32,1)
                Size1252 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1253 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1254 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1252:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx46 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx46
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn47,0)
                f.seek(-32,1)
                Size1255 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1256 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1257 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1255:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz46 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz46
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn47,0)
                f.seek(-32,1)
                Size1258 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1259 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1260 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1258:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty46 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty46
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn47,0)
                f.seek(-32,1)
                Size1261 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1262 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1263 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1261:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx46 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx46
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn47,0)
                f.seek(-32,1)
                Size1264 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1265 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1266 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1264:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly46 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly46
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn47,0)
                f.seek(-32,1)
                Size1267 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1268 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1269 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1267:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz46 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz46
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn48,0)
                f.seek(-32,1)
                Size1270 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1271 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1272 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1270:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx47 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx47
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn48,0)
                f.seek(-32,1)
                Size1273 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1274 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1275 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1273:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy47 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy47
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn48,0)
                f.seek(-32,1)
                Size1276 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1277 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1278 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1276:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz47 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz47
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn48,0)
                f.seek(-32,1)
                Size1279 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1280 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1281 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1279:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx47 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx47
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn48,0)
                f.seek(-32,1)
                Size1282 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1283 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1284 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1282:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz47 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz47
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn48,0)
                f.seek(-32,1)
                Size1285 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1286 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1287 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1285:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty47 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty47
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn48,0)
                f.seek(-32,1)
                Size1288 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1289 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1290 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1288:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx47 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx47
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn48,0)
                f.seek(-32,1)
                Size1291 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1292 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1293 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1291:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly47 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly47
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn48,0)
                f.seek(-32,1)
                Size1294 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1295 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1296 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1294:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz47 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz47
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn49,0)
                f.seek(-32,1)
                Size1297 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1298 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1299 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1297:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx48 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx48
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn49,0)
                f.seek(-32,1)
                Size1300 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1301 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1302 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1300:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy48 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy48
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn49,0)
                f.seek(-32,1)
                Size1303 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1304 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1305 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1303:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz48 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz48
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn49,0)
                f.seek(-32,1)
                Size1306 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1307 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1308 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1306:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx48 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx48
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn49,0)
                f.seek(-32,1)
                Size1309 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1310 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1311 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1309:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz48 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz48
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn49,0)
                f.seek(-32,1)
                Size1312 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1313 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1314 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1312:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty48 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty48
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn49,0)
                f.seek(-32,1)
                Size1315 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1316 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1317 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1315:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx48 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx48
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn49,0)
                f.seek(-32,1)
                Size1318 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1319 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1320 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1318:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly48 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly48
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn49,0)
                f.seek(-32,1)
                Size1321 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1322 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1323 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1321:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz48 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz48
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn50,0)
                f.seek(-32,1)
                Size1324 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1325 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1326 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1324:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx49 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.x = posx49
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn50,0)
                f.seek(-32,1)
                Size1327 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1328 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1329 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1327:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy49 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.y = posy49
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn50,0)
                f.seek(-32,1)
                Size1330 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1331 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1332 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1330:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz49 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.z = posz49
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn50,0)
                f.seek(-32,1)
                Size1333 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1334 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1335 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1333:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx49 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.x = rotx49
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn50,0)
                f.seek(-32,1)
                Size1336 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1337 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1338 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1336:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz49 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.z = rotz49
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn50,0)
                f.seek(-32,1)
                Size1339 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1340 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1341 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1339:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty49 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.y = roty49
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn50,0)
                f.seek(-32,1)
                Size1342 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1343 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1344 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1342:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx49 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.x = sclx49
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn50,0)
                f.seek(-32,1)
                Size1345 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1346 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1347 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1345:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly49 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.y = scly49
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn50,0)
                f.seek(-32,1)
                Size1348 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1349 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1350 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1348:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz49 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.z = sclz49
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn51,0)
                f.seek(-32,1)
                Size1351 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1352 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1353 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1351:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx50 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.x = posx50
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn51,0)
                f.seek(-32,1)
                Size1354 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1355 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1356 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1354:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy50 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.y = posy50
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn51,0)
                f.seek(-32,1)
                Size1357 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1358 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1359 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1357:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz50 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.z = posz50
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn51,0)
                f.seek(-32,1)
                Size1360 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1361 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1362 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1360:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx50 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.x = rotx50
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn51,0)
                f.seek(-32,1)
                Size1363 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1364 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1365 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1363:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz50 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.z = rotz50
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn51,0)
                f.seek(-32,1)
                Size1366 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1367 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1368 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1366:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty50 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.y = roty50
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn51,0)
                f.seek(-32,1)
                Size1369 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1370 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1371 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1369:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx50 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.x = sclx50
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn51,0)
                f.seek(-32,1)
                Size1372 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1373 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1374 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1372:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly50 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.y = scly50
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn51,0)
                f.seek(-32,1)
                Size1375 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1376 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1377 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1375:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz50 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.z = sclz50
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn52,0)
                f.seek(-32,1)
                Size1378 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1379 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1380 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1378:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx51 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.x = posx51
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn52,0)
                f.seek(-32,1)
                Size1381 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1382 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1383 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1381:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy51 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.y = posy51
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn52,0)
                f.seek(-32,1)
                Size1384 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1385 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1386 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1384:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz51 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.z = posz51
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn52,0)
                f.seek(-32,1)
                Size1387 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1388 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1389 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1387:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx51 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.x = rotx51
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn52,0)
                f.seek(-32,1)
                Size1390 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1391 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1392 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1390:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz51 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.z = rotz51
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn52,0)
                f.seek(-32,1)
                Size1393 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1394 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1395 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1393:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty51 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.y = roty51
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn52,0)
                f.seek(-32,1)
                Size1396 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1397 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1398 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1396:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx51 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.x = sclx51
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn52,0)
                f.seek(-32,1)
                Size1399 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1400 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1401 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1399:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly51 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.y = scly51
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn52,0)
                f.seek(-32,1)
                Size1402 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1403 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1404 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1402:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz51 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.z = sclz51
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn53,0)
                f.seek(-32,1)
                Size1405 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1406 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1407 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1405:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx52 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.x = posx52
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn53,0)
                f.seek(-32,1)
                Size1408 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1409 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1410 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1408:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy52 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.y = posy52
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn53,0)
                f.seek(-32,1)
                Size1411 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1412 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1413 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1411:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz52 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.z = posz52
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn53,0)
                f.seek(-32,1)
                Size1414 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1415 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1416 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1414:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx52 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.x = rotx52
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn53,0)
                f.seek(-32,1)
                Size1417 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1418 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1419 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1417:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz52 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.z = rotz52
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn53,0)
                f.seek(-32,1)
                Size1420 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1421 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1422 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1420:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty52 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.y = roty52
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn53,0)
                f.seek(-32,1)
                Size1423 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1424 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1425 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1423:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx52 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.x = sclx52
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn53,0)
                f.seek(-32,1)
                Size1426 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1427 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1428 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1426:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly52 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.y = scly52
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn53,0)
                f.seek(-32,1)
                Size1429 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1430 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1431 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1429:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz52 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.z = sclz52
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn54,0)
                f.seek(-32,1)
                Size1432 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1433 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1434 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1432:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx53 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].location.x = posx53
                    ob.pose.bones[9].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn54,0)
                f.seek(-32,1)
                Size1435 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1436 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1437 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1435:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy53 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].location.y = posy53
                    ob.pose.bones[9].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn54,0)
                f.seek(-32,1)
                Size1438 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1439 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1440 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1438:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz53 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].location.z = posz53
                    ob.pose.bones[9].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn54,0)
                f.seek(-32,1)
                Size1441 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1442 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1443 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1441:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx53 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].rotation_euler.x = rotx53
                    ob.pose.bones[9].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn54,0)
                f.seek(-32,1)
                Size1444 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1445 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1446 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1444:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz53 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].rotation_euler.z = rotz53
                    ob.pose.bones[9].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn54,0)
                f.seek(-32,1)
                Size1447 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1448 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1449 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1447:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty53 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].rotation_euler.y = roty53
                    ob.pose.bones[9].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn54,0)
                f.seek(-32,1)
                Size1450 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1451 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1452 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1450:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx53 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].scale.x = sclx53
                    ob.pose.bones[9].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn54,0)
                f.seek(-32,1)
                Size1453 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1454 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1455 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1453:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly53 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].scale.y = scly53
                    ob.pose.bones[9].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn54,0)
                f.seek(-32,1)
                Size1456 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1457 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1458 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1456:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz53 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].scale.z = sclz53
                    ob.pose.bones[9].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 11:
            posxOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn55 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn56 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn57 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn58 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn59 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn60 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn61 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn62 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn63 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn64 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            posxOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            posyOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            poszOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotxOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotyOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            rotzOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclxOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclyOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)
            sclzOn65 = unpack("<I", f.read(4))[0] & max(0xFFFF,0)

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True
            booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz = unpack("B", f.read(1))[0]==True

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn55,0)
                f.seek(-32,1)
                Size1459 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1460 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1461 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1459:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx54 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.x = posx54
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn55,0)
                f.seek(-32,1)
                Size1462 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1463 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1464 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1462:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy54 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.y = posy54
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn55,0)
                f.seek(-32,1)
                Size1465 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1466 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1467 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1465:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz54 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].location.z = posz54
                    ob.pose.bones[0].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn55,0)
                f.seek(-32,1)
                Size1468 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1469 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1470 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1468:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx54 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.x = rotx54
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn55,0)
                f.seek(-32,1)
                Size1471 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1472 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1473 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1471:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz54 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.z = rotz54
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn55,0)
                f.seek(-32,1)
                Size1474 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1475 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1476 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1474:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty54 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].rotation_euler.y = roty54
                    ob.pose.bones[0].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn55,0)
                f.seek(-32,1)
                Size1477 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1478 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1479 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1477:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx54 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.x = sclx54
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn55,0)
                f.seek(-32,1)
                Size1480 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1481 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1482 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1480:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly54 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.y = scly54
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn55,0)
                f.seek(-32,1)
                Size1483 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1484 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1485 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1483:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz54 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[0].scale.z = sclz54
                    ob.pose.bones[0].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn56,0)
                f.seek(-32,1)
                Size1486 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1487 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1488 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1486:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx55 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.x = posx55
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn56,0)
                f.seek(-32,1)
                Size1489 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1490 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1491 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1489:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy55 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.y = posy55
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn56,0)
                f.seek(-32,1)
                Size1492 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1493 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1494 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1492:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz55 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].location.z = posz55
                    ob.pose.bones[1].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn56,0)
                f.seek(-32,1)
                Size1495 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1496 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1497 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1495:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx55 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.x = rotx55
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn56,0)
                f.seek(-32,1)
                Size1498 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1499 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1500 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1498:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz55 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.z = rotz55
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn56,0)
                f.seek(-32,1)
                Size1501 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1502 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1503 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1501:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty55 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].rotation_euler.y = roty55
                    ob.pose.bones[1].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn56,0)
                f.seek(-32,1)
                Size1504 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1505 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1506 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1504:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx55 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.x = sclx55
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn56,0)
                f.seek(-32,1)
                Size1507 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1508 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1509 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1507:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly55 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.y = scly55
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn56,0)
                f.seek(-32,1)
                Size1510 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1511 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1512 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1510:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz55 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[1].scale.z = sclz55
                    ob.pose.bones[1].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn57,0)
                f.seek(-32,1)
                Size1513 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1514 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1515 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1513:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx56 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.x = posx56
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn57,0)
                f.seek(-32,1)
                Size1516 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1517 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1518 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1516:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy56 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.y = posy56
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn57,0)
                f.seek(-32,1)
                Size1519 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1520 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1521 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1519:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz56 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].location.z = posz56
                    ob.pose.bones[2].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn57,0)
                f.seek(-32,1)
                Size1522 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1523 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1524 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1522:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx56 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.x = rotx56
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn57,0)
                f.seek(-32,1)
                Size1525 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1526 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1527 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1525:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz56 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.z = rotz56
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn57,0)
                f.seek(-32,1)
                Size1528 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1529 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1530 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1528:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty56 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].rotation_euler.y = roty56
                    ob.pose.bones[2].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn57,0)
                f.seek(-32,1)
                Size1531 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1532 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1533 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1531:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx56 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.x = sclx56
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn57,0)
                f.seek(-32,1)
                Size1534 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1535 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1536 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1534:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly56 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.y = scly56
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn57,0)
                f.seek(-32,1)
                Size1537 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1538 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1539 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1537:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz56 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[2].scale.z = sclz56
                    ob.pose.bones[2].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn58,0)
                f.seek(-32,1)
                Size1540 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1541 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1542 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1540:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx57 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.x = posx57
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn58,0)
                f.seek(-32,1)
                Size1543 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1544 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1545 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1543:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy57 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.y = posy57
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn58,0)
                f.seek(-32,1)
                Size1546 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1547 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1548 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1546:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz57 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].location.z = posz57
                    ob.pose.bones[3].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn58,0)
                f.seek(-32,1)
                Size1549 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1550 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1551 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1549:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx57 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.x = rotx57
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn58,0)
                f.seek(-32,1)
                Size1552 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1553 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1554 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1552:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz57 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.z = rotz57
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn58,0)
                f.seek(-32,1)
                Size1555 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1556 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1557 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1555:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty57 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].rotation_euler.y = roty57
                    ob.pose.bones[3].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn58,0)
                f.seek(-32,1)
                Size1558 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1559 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1560 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1558:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx57 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.x = sclx57
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn58,0)
                f.seek(-32,1)
                Size1561 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1562 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1563 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1561:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly57 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.y = scly57
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn58,0)
                f.seek(-32,1)
                Size1564 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1565 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1566 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1564:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz57 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[3].scale.z = sclz57
                    ob.pose.bones[3].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn59,0)
                f.seek(-32,1)
                Size1567 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1568 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1569 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1567:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx58 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.x = posx58
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn59,0)
                f.seek(-32,1)
                Size1570 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1571 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1572 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1570:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy58 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.y = posy58
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn59,0)
                f.seek(-32,1)
                Size1573 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1574 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1575 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1573:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz58 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].location.z = posz58
                    ob.pose.bones[4].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn59,0)
                f.seek(-32,1)
                Size1576 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1577 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1578 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1576:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx58 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.x = rotx58
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn59,0)
                f.seek(-32,1)
                Size1579 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1580 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1581 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1579:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz58 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.z = rotz58
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn59,0)
                f.seek(-32,1)
                Size1582 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1583 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1584 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1582:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty58 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].rotation_euler.y = roty58
                    ob.pose.bones[4].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn59,0)
                f.seek(-32,1)
                Size1585 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1586 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1587 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1585:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx58 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.x = sclx58
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn59,0)
                f.seek(-32,1)
                Size1588 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1589 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1590 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1588:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly58 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.y = scly58
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn59,0)
                f.seek(-32,1)
                Size1591 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1592 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1593 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1591:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz58 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[4].scale.z = sclz58
                    ob.pose.bones[4].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn60,0)
                f.seek(-32,1)
                Size1594 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1595 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1596 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1594:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx59 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.x = posx59
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn60,0)
                f.seek(-32,1)
                Size1597 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1598 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1599 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1597:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy59 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.y = posy59
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn60,0)
                f.seek(-32,1)
                Size1600 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1601 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1602 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1600:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz59 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].location.z = posz59
                    ob.pose.bones[5].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn60,0)
                f.seek(-32,1)
                Size1603 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1604 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1605 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1603:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx59 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.x = rotx59
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn60,0)
                f.seek(-32,1)
                Size1606 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1607 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1608 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1606:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz59 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.z = rotz59
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn60,0)
                f.seek(-32,1)
                Size1609 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1610 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1611 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1609:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty59 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].rotation_euler.y = roty59
                    ob.pose.bones[5].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn60,0)
                f.seek(-32,1)
                Size1612 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1613 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1614 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1612:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx59 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.x = sclx59
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn60,0)
                f.seek(-32,1)
                Size1615 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1616 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1617 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1615:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly59 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.y = scly59
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn60,0)
                f.seek(-32,1)
                Size1618 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1619 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1620 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1618:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz59 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[5].scale.z = sclz59
                    ob.pose.bones[5].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn61,0)
                f.seek(-32,1)
                Size1621 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1622 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1623 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1621:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx60 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.x = posx60
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn61,0)
                f.seek(-32,1)
                Size1624 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1625 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1626 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1624:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy60 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.y = posy60
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn61,0)
                f.seek(-32,1)
                Size1627 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1628 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1629 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1627:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz60 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].location.z = posz60
                    ob.pose.bones[6].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn61,0)
                f.seek(-32,1)
                Size1630 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1631 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1632 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1630:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx60 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.x = rotx60
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn61,0)
                f.seek(-32,1)
                Size1633 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1634 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1635 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1633:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz60 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.z = rotz60
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn61,0)
                f.seek(-32,1)
                Size1636 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1637 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1638 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1636:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty60 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].rotation_euler.y = roty60
                    ob.pose.bones[6].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn61,0)
                f.seek(-32,1)
                Size1639 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1640 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1641 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1639:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx60 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.x = sclx60
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn61,0)
                f.seek(-32,1)
                Size1642 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1643 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1644 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1642:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly60 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.y = scly60
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn61,0)
                f.seek(-32,1)
                Size1645 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1646 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1647 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1645:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz60 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[6].scale.z = sclz60
                    ob.pose.bones[6].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn62,0)
                f.seek(-32,1)
                Size1648 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1649 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1650 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1648:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx61 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.x = posx61
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn62,0)
                f.seek(-32,1)
                Size1651 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1652 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1653 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1651:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy61 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.y = posy61
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn62,0)
                f.seek(-32,1)
                Size1654 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1655 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1656 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1654:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz61 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].location.z = posz61
                    ob.pose.bones[7].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn62,0)
                f.seek(-32,1)
                Size1657 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1658 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1659 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1657:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx61 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.x = rotx61
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn62,0)
                f.seek(-32,1)
                Size1660 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1661 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1662 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1660:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz61 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.z = rotz61
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn62,0)
                f.seek(-32,1)
                Size1663 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1664 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1665 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1663:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty61 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].rotation_euler.y = roty61
                    ob.pose.bones[7].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn62,0)
                f.seek(-32,1)
                Size1666 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1667 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1668 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1666:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx61 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.x = sclx61
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn62,0)
                f.seek(-32,1)
                Size1669 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1670 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1671 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1669:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly61 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.y = scly61
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn62,0)
                f.seek(-32,1)
                Size1672 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1673 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1674 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1672:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz61 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[7].scale.z = sclz61
                    ob.pose.bones[7].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn63,0)
                f.seek(-32,1)
                Size1675 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1676 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1677 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1675:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx62 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.x = posx62
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn63,0)
                f.seek(-32,1)
                Size1678 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1679 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1680 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1678:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy62 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.y = posy62
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn63,0)
                f.seek(-32,1)
                Size1681 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1682 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1683 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1681:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz62 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].location.z = posz62
                    ob.pose.bones[8].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn63,0)
                f.seek(-32,1)
                Size1684 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1685 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1686 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1684:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx62 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.x = rotx62
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn63,0)
                f.seek(-32,1)
                Size1687 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1688 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1689 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1687:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz62 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.z = rotz62
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn63,0)
                f.seek(-32,1)
                Size1690 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1691 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1692 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1690:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty62 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].rotation_euler.y = roty62
                    ob.pose.bones[8].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn63,0)
                f.seek(-32,1)
                Size1693 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1694 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1695 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1693:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx62 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.x = sclx62
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn63,0)
                f.seek(-32,1)
                Size1696 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1697 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1698 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1696:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly62 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.y = scly62
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn63,0)
                f.seek(-32,1)
                Size1699 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1700 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1701 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1699:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz62 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[8].scale.z = sclz62
                    ob.pose.bones[8].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn64,0)
                f.seek(-32,1)
                Size1702 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1703 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1704 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1702:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx63 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].location.x = posx63
                    ob.pose.bones[9].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn64,0)
                f.seek(-32,1)
                Size1705 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1706 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1707 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1705:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy63 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].location.y = posy63
                    ob.pose.bones[9].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn64,0)
                f.seek(-32,1)
                Size1708 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1709 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1710 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1708:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz63 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].location.z = posz63
                    ob.pose.bones[9].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn64,0)
                f.seek(-32,1)
                Size1711 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1712 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1713 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1711:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx63 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].rotation_euler.x = rotx63
                    ob.pose.bones[9].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn64,0)
                f.seek(-32,1)
                Size1714 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1715 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1716 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1714:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz63 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].rotation_euler.z = rotz63
                    ob.pose.bones[9].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn64,0)
                f.seek(-32,1)
                Size1717 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1718 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1719 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1717:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty63 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].rotation_euler.y = roty63
                    ob.pose.bones[9].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn64,0)
                f.seek(-32,1)
                Size1720 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1721 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1722 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1720:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx63 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].scale.x = sclx63
                    ob.pose.bones[9].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn64,0)
                f.seek(-32,1)
                Size1723 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1724 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1725 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1723:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly63 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].scale.y = scly63
                    ob.pose.bones[9].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn64,0)
                f.seek(-32,1)
                Size1726 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1727 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1728 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1726:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz63 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[9].scale.z = sclz63
                    ob.pose.bones[9].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

            if booleanPX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posxOn65,0)
                f.seek(-32,1)
                Size1729 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1730 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1731 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1729:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posx64 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].location.x = posx64
                    ob.pose.bones[10].keyframe_insert(data_path="location", index=0, frame=int(floatframe))

            if booleanPY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(posyOn65,0)
                f.seek(-32,1)
                Size1732 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1733 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1734 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1732:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posy64 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].location.y = posy64
                    ob.pose.bones[10].keyframe_insert(data_path="location", index=1, frame=int(floatframe))

            if booleanPZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(poszOn65,0)
                f.seek(-32,1)
                Size1735 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1736 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1737 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1735:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    posz64 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].location.z = posz64
                    ob.pose.bones[10].keyframe_insert(data_path="location", index=2, frame=int(floatframe))

            if booleanRX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotxOn65,0)
                f.seek(-32,1)
                Size1738 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1739 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1740 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1738:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotx64 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].rotation_euler.x = rotx64
                    ob.pose.bones[10].keyframe_insert(data_path="rotation_euler", index=0, frame=int(floatframe))

            if booleanRY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotyOn65,0)
                f.seek(-32,1)
                Size1741 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1742 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1743 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1741:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    rotz64 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].rotation_euler.z = rotz64
                    ob.pose.bones[10].keyframe_insert(data_path="rotation_euler", index=2, frame=int(floatframe))

            if booleanRZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(rotzOn65,0)
                f.seek(-32,1)
                Size1744 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1745 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1746 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1744:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    roty64 = -unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].rotation_euler.y = roty64
                    ob.pose.bones[10].keyframe_insert(data_path="rotation_euler", index=1, frame=int(floatframe))

            if booleanSX1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclxOn65,0)
                f.seek(-32,1)
                Size1747 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1748 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1749 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1747:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclx64 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].scale.x = sclx64
                    ob.pose.bones[10].keyframe_insert(data_path="scale", index=0, frame=int(floatframe))

            if booleanSY1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclyOn65,0)
                f.seek(-32,1)
                Size1750 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1751 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1752 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1750:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    scly64 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].scale.y = scly64
                    ob.pose.bones[10].keyframe_insert(data_path="scale", index=1, frame=int(floatframe))

            if booleanSZ1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz > 0:
                f.seek(sclzOn65,0)
                f.seek(-32,1)
                Size1753 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1754 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                Size1755 = unpack("<I", f.read(4))[0]-32 & max(0xFFFF,0)
                while f.tell() < Size1753:
                    floatframe = unpack("<f", f.read(4))[0]
                    framerate = unpack("<f", f.read(4))[0]
                    sclz64 = unpack("<f", f.read(4))[0]
                    unk01 = unpack("<f", f.read(4))[0]
                    ob.pose.bones[10].scale.z = sclz64
                    ob.pose.bones[10].keyframe_insert(data_path="scale", index=2, frame=int(floatframe))

        elif BoneCount == 12:
            pass

def ani_importer_read(filepath, Boolean1V2=False, Boolean2V2=False, V1=False, V6=False):
    with open(filepath,"rb") as f:
        if Boolean1V2:
            ani_importV2(f)

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        pass
                    
        
    

