bl_info = {
        'name'			: 'Finding Nemo Simple Animation Importer Exporter Experimental',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 0, 1),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Import',
	'description'           : 'Import Ani aka Animation',
	'category'		: 'Ani-Importer and Ani-Exporter',
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from.import ani_import_export2 #ani_export

class ImportAniAkaAnimation(bpy.types.Operator, ImportHelper):
        bl_idname  = 'ani_import_export_.ani'
        bl_label   = 'Import Animations 4 Nemo'
        bl_options = {'UNDO'}
        filename_ext = '.ani'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the ani aka Animation.',
                type	    = bpy.types.OperatorFileListElement
        )
        Boolean1V2: BoolProperty(
                name = "boolean 1",
                description = "only imports bool1"
        )
        Boolean2V2: BoolProperty(
                name = "boolean 2",
                description = "only imports bool2"
        )
        V1: BoolProperty(
                name = "twoc v1",
                description = "imports twoc v1"
        )
        V6: BoolProperty(
                name = "link v6",
                description = "imports link v6"
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.ani', options = {'HIDDEN'})
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(ani_import_export2)
                for path in paths: ani_import_export2.ani_importer_read(path, Boolean1V2 = self.Boolean1V2, Boolean2V2 = self.Boolean2V2, V1 = self.V1, V6 = self.V6,)
                return {'FINISHED'}

class ExportAniAkaAnimation(bpy.types.Operator, ExportHelper):
        bl_idname  = 'ani_export_export_.ani'
        bl_label   = 'Export Animations 4 Nemo'
        bl_options = {'UNDO'}
        filename_ext = '.ani'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the ani aka Animation.',
                type	    = bpy.types.OperatorFileListElement
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.ani', options = {'HIDDEN'})
        
        def execute(self, context):
                importlib.reload(ani_import_export2)
                ani_import_export2.ani_exporter_write(self.filepath)
                return {'FINISHED'}
                

        
        

        
	
def menu_func_export(self, context):
        self.layout.operator(ExportAniAkaAnimation.bl_idname, text='Ani aka Animation (.ani)')
def menu_func_import(self, context):
        self.layout.operator(ImportAniAkaAnimation.bl_idname, text='Ani aka Animation (.ani)')
def register():
        bpy.utils.register_class(ImportAniAkaAnimation)
        bpy.utils.register_class(ExportAniAkaAnimation)
        bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
        bpy.utils.unregister_class(ImportAniAkaAnimation)
        bpy.utils.unregister_class(ExportAniAkaAnimation)
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
if __name__ == '__main__': register()
