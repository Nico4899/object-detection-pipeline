import bpy


def unhide_object(obj_name):
    if obj_name in bpy.data.objects:
        bpy.data.objects[obj_name].hide_render = False


def unhide_objects(names):
    for name in names:
        unhide_object(name)