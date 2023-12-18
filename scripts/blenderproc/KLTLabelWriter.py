import bpy
import os
import json
import mathutils


def generate_labels_for_camera(camera):
    labels = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            # Calculate bounding box coordinates for obj as seen by camera
            bbox_coords = calculate_bounding_box(obj, camera)
            labels.append({
                'object': obj.name,
                'bounding_box': bbox_coords
            })
    return labels


def calculate_bounding_box(obj, camera):
    # Get the object's bounding box corners
    bbox_corners = [obj.matrix_world @ vertex for vertex in obj.bound_box]

    # Project each corner to 2D
    projected = [project_3d_to_2d(camera, corner) for corner in bbox_corners]

    # Filter out None values (points behind the camera)
    projected = [p for p in projected if p is not None]

    # If no points are visible, return None
    if not projected:
        return None

    # Find the min and max points to form the bounding box
    min_x = min([p[0] for p in projected])
    max_x = max([p[0] for p in projected])
    min_y = min([p[1] for p in projected])
    max_y = max([p[1] for p in projected])

    # Return the bounding box as [min_x, min_y, max_x, max_y]
    return [min_x, min_y, max_x, max_y]


def project_3d_to_2d(camera, coord_3d):
    # The coordinate in 3D space to be projected
    coord_3d = mathutils.Vector(coord_3d)

    # The transformation matrix from 3D to screen space
    mat_world_to_camera = camera.matrix_world.inverted()
    mat_camera_to_screen = camera.calc_matrix_camera(
        bpy.context.evaluated_depsgraph_get(), x=bpy.context.scene.render.resolution_x, y=bpy.context.scene.render.resolution_y
    )

    # Convert the 3D coordinate to camera space, then to screen space
    coord_camera = mat_world_to_camera @ coord_3d
    coord_screen = mat_camera_to_screen @ coord_camera

    # Normalize the screen coordinate
    if coord_screen.z > 0:
        return coord_screen.x / coord_screen.z / 2 + 0.5, coord_screen.y / coord_screen.z / 2 + 0.5
    else:
        return None  # The point is behind the camera


def write_labels_to_file(labels, output_path):
    with open(output_path, 'w') as file:
        json.dump(labels, file, indent=4)


def write_labels_for_scene(output_dir):
    for camera in bpy.data.objects:
        if camera.type == 'CAMERA':
            labels = generate_labels_for_camera(camera)
            label_file = f"{camera.name}_labels.json"
            output_path = os.path.join(output_dir, label_file)
            write_labels_to_file(labels, output_path)


def main(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    write_labels_for_scene(output_dir)


if __name__ == "__main__":
    main("../../output")
