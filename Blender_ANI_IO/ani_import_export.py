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
            for i in range(BoneCount):
                boneiddd = unpack("B", f.read(1))[0]

            for i, bidx in enumerate(keyM):
                if bidx[1] == 8994:
                    f.seek(bidx[0]-32,0)
                    print(f.tell())




def ani_exportV2_all_move_non_parser(f):
    pass
                
                

            
            
            


                
    
def ani_importer_read(filepath):
    with open(filepath,"rb") as f:
        ani_importV2(f)

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        ani_exportV2_all_move_non_parser(f)
