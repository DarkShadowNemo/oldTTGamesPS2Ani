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
                    
                
                    
                        

def ani_importer_read(filepath, Beta_ani=False, Norm_ani=False):
    with open(filepath,"rb") as f:
        ani_importV2(f)

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        pass
                    
        
    

