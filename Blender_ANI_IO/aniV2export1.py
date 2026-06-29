from struct import unpack, pack, error
import bpy
import os
import mathutils
import math

def ani_exportV2pt1_(f):
    ob = bpy.context.object
    f.write(pack("<I", 2))
    f.write(pack("<H", 32))
    f.write(pack("<H", 0))
    f.write(pack("<H", 44))
    f.write(pack("<H", 0))
    f.write(pack("<f", bpy.context.scene.frame_end))
    f.write(pack("<H", len(ob.pose.bones)))
    f.write(pack("<H", 9))
    f.write(pack("<I", 1))
    f.write(pack("<H", 68))
    f.write(pack("<H", 0))
    f.write(pack("<H", 36+36*len(ob.pose.bones)+32))
    f.write(pack("<H", 0))
    f.write(pack("<H", 36+36*len(ob.pose.bones)+9*len(ob.pose.bones)+32))
    f.write(pack("<H", 0))

    if len(ob.pose.bones) == 0:
        pass
    elif len(ob.pose.bones):
        for pbone in ob.pose.bones:
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
            f.write(pack("<I", f.tell()+36*len(ob.pose.bones)+9*len(ob.pose.bones)+1*len(ob.pose.bones)+32))
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
            f.write(pack("<I", f.tell()+4+16*bpy.context.scene.frame_end+8+4+32))
            f.write(pack("<I", f.tell()+4+16*bpy.context.scene.frame_end+8+4+32))
            f.write(pack("<I", f.tell()+4+16*bpy.context.scene.frame_end))
            for frame_ in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1):
                f.write(pack("<f", frame_))
                f.write(pack("<f", frame_/30))
                f.write(pack("<f", pbone.head.x/10))
                f.write(pack("<f", 0))
                bpy.context.scene.frame_set(frame_)
            f.write(pack("<I", 0))
            f.write(pack("<I", 131073))
    

    
        
    
