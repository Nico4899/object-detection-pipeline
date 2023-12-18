import bpy


def hide_object(obj_name):
    if obj_name in bpy.data.objects:
        bpy.data.objects[obj_name].hide_render = True


def hide_objects(names):
    for name in names:
        hide_object(name)
