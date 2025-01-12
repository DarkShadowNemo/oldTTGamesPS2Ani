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

        for i in range(BoneCount):
            m1 = unpack("<I", f.read(4))[0] & 0xFFFF
            m2 = unpack("<I", f.read(4))[0] & 0xFFFF
            m3 = unpack("<I", f.read(4))[0] & 0xFFFF
            m4 = unpack("<I", f.read(4))[0] & 0xFFFF
            m5 = unpack("<I", f.read(4))[0] & 0xFFFF
            m6 = unpack("<I", f.read(4))[0] & 0xFFFF
            m7 = unpack("<I", f.read(4))[0] & 0xFFFF
            m8 = unpack("<I", f.read(4))[0] & 0xFFFF
            m9 = unpack("<I", f.read(4))[0] & 0xFFFF

        f.seek(EntrySize2-32,0)
            

        for i in range(BoneCount):
            booleansOnOffKeys1Posx = unpack("B", f.read(1))[0]
            booleansOnOffKeys2Posy = unpack("B", f.read(1))[0]
            booleansOnOffKeys3Posz = unpack("B", f.read(1))[0]
            booleansOnOffKeys4Rotx = unpack("B", f.read(1))[0]
            booleansOnOffKeys3Roty = unpack("B", f.read(1))[0]
            booleansOnOffKeys5Rotz = unpack("B", f.read(1))[0]
            booleansOnOffKeys6Sclx = unpack("B", f.read(1))[0]
            booleansOnOffKeys7Scly = unpack("B", f.read(1))[0]
            booleansOnOffKeys8Sclz = unpack("B", f.read(1))[0]

        f.seek(EntrySize3-32,0)
        for i in range(BoneCount):
            unknown01 = unpack("B", f.read(1))[0]

        #WIP have not figure it out yet the rest due to importing





def ani_exportV2_all_move_non_parser(f):
    ob = bpy.context.object
    f.write(pack("<I", 2))
    f.write(pack("<I", 32))
    f.write(pack("<I", 44))
    f.write(pack("<f", bpy.context.scene.frame_end))
    f.write(pack("<H", len(ob.pose.bones)))
    f.write(pack("<H", 9))
    f.write(pack("<I", 1))
    f.write(pack("<I", 68))
    f.write(pack("<I", 36*len(ob.pose.bones)+32+36))
    f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)))
    for pbone in ob.pose.bones:
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)))
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
    f.write(pack("<H", 0))
    for pbone in ob.pose.bones:
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 36*len(ob.pose.bones)+32+36+9*len(ob.pose.bones)+len(ob.pose.bones)+2+4+4+4+32))
        for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
            f.write(pack("<f", frame_))
            f.write(pack("<f", frame_/30))
            f.write(pack("<f", pbone.head.x))
            f.write(pack("<f", 0))

            bpy.context.scene.frame_set(frame_)

    #WIP have not figure it out yet the rest due to exporting
                
                

            
            
            


                
    
def ani_importer_read(filepath):
    with open(filepath,"rb") as f:
        ani_importV2(f)

def ani_exporter_write(filepath):
    with open(filepath,"wb") as f:
        ani_exportV2_all_move_non_parser(f)
