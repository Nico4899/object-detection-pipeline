import bpy
import random
import os
import mathutils

from KLTCameraSampler import sample_cameras
from KLTImageWriter import main as render_main

def initialize_scene():
    # Clear existing objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Set render engine to Cycles for more realistic rendering (can use 'BLENDER_EEVEE' for faster, less realistic rendering)
    bpy.context.scene.render.engine = 'CYCLES'

    # Set the rendering resolution
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.resolution_percentage = 100

    # Set the world background, can be plain color or use an HDRI image for more realistic lighting
    bpy.data.worlds['World'].use_nodes = True
    bg = bpy.data.worlds['World'].node_tree.nodes['Background']
    bg.inputs[0].default_value = (0.8, 0.8, 0.8, 1)  # Grey background, adjust the RGB values as needed

    setup_camera()
    setup_lighting()


def load_package_units(filepath):
    # Load the model from a file
    if os.path.exists(filepath):
        bpy.ops.import_scene.obj(filepath=filepath)
    else:
        print(f"File not found: {filepath}")


def place_package_unit(obj, position, rotation):
    obj.location = position
    obj.rotation_euler = rotation


def randomize_units():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            # Randomize position
            random_position = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0, 5))
            # Randomize rotation
            random_rotation = (random.uniform(0, 3.14), random.uniform(0, 3.14), random.uniform(0, 3.14))

            place_package_unit(obj, random_position, random_rotation)


def setup_camera():
    # Create a new camera object
    bpy.ops.object.camera_add()
    camera = bpy.context.object

    # Set camera lens and other properties
    camera.data.type = 'PERSP'  # or 'ORTHO' for orthographic projection
    camera.data.lens = 35  # Adjust focal length as needed

    # Position and orient the camera
    camera.location = (10, 10, 10)  # Example position
    camera.rotation_euler = (0.9, 0, 1.57)  # Example rotation

    # Optionally, add more cameras with different positions and orientations


def setup_lighting():
    # Basic single light setup
    bpy.ops.object.light_add(type='POINT', location=(5, 5, 5))
    light = bpy.context.object
    light.data.energy = 1000  # Adjust intensity as needed

    # Additional lights can be added for more complex lighting scenarios


def calculate_target_location():
    total_location = mathutils.Vector((0, 0, 0))
    count = 0
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            total_location += obj.location
            count += 1
    if count > 0:
        return total_location / count
    else:
        return mathutils.Vector((0, 0, 0))  # Default to the origin if no objects are found


def main():
    initialize_scene()

    # Update the path to where the FBX files are stored
    data_path = os.path.join(os.path.dirname(__file__), '../../data/base_data')

    # Load each package unit as an FBX file
    load_package_units(os.path.join(data_path, 'klt_642.fbx'))
    load_package_units(os.path.join(data_path, 'klt_643.fbx'))
    load_package_units(os.path.join(data_path, 'klt_4315.fbx'))
    load_package_units(os.path.join(data_path, 'klt_6414.fbx'))

    # Apply randomization
    randomize_units()

    target_location = calculate_target_location()
    sample_cameras(10, target_location)

    render_main("../../output")


if __name__ == "__main__":
    main()
