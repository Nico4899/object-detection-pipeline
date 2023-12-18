import bpy
import random
import math

class CameraProperties:
    def __init__(self):
        self.focal_length = 35  # Default focal length
        self.sensor_size = 36   # Default sensor size (mm)
        # Add other relevant properties


def position_camera(camera, min_distance, max_distance, angle_range):
    distance = random.uniform(min_distance, max_distance)
    angle = random.uniform(angle_range[0], angle_range[1])

    camera.location.x = distance * math.sin(angle)
    camera.location.y = distance * math.cos(angle)
    camera.location.z = random.uniform(1.0, 3.0)  # Adjust Z-axis as needed


def orient_camera(camera, target_location):
    direction = target_location - camera.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()


def sample_cameras(num_samples, target_location):
    for _ in range(num_samples):
        bpy.ops.object.camera_add()
        camera = bpy.context.object

        position_camera(camera, 5, 15, (0, math.pi * 2))
        orient_camera(camera, target_location)

        # Set additional camera properties as needed
