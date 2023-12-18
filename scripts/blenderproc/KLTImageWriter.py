import bpy
import os


def setup_render_settings(output_path, resolution_x=1920, resolution_y=1080):
    bpy.context.scene.render.image_settings.file_format = 'PNG'  # or 'JPEG'
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    bpy.context.scene.render.filepath = output_path


def render_images(output_dir):
    original_camera = bpy.context.scene.camera
    for obj in bpy.data.objects:
        if obj.type == 'CAMERA':
            # Set the current camera
            bpy.context.scene.camera = obj

            # Set the output file path
            file_name = f"render_{obj.name}.png"
            output_path = os.path.join(output_dir, file_name)
            bpy.context.scene.render.filepath = output_path

            # Render the scene
            bpy.ops.render.render(write_still=True)

    # Reset the original camera
    bpy.context.scene.camera = original_camera


def main(output_dir, resolution_x=1920, resolution_y=1080):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    setup_render_settings(output_dir, resolution_x, resolution_y)
    render_images(output_dir)


if __name__ == "__main__":
    main("../../output")
