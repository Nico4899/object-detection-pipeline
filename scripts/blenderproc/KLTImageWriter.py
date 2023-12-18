import bpy
import os


def setup_render_settings(output_path, resolution_x=1920, resolution_y=1080):
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.resolution_x = resolution_x
    bpy.context.scene.render.resolution_y = resolution_y
    bpy.context.scene.render.filepath = output_path


def setup_advanced_render_settings(samples=64, use_denoising=True):
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = samples
    bpy.context.scene.cycles.use_denoising = use_denoising


def get_file_name(camera, index):
    return f"render_{camera.name}_{index}.png"


def safe_render(camera, output_path):
    try:
        bpy.context.scene.camera = camera
        bpy.context.scene.render.filepath = output_path
        bpy.ops.render.render(write_still=True)
    except Exception as e:
        print(f"Error rendering image from {camera.name}: {e}")


def render_batch(cameras, batch_size, output_dir):
    batch = []
    for index, camera in enumerate(cameras):
        batch.append(camera)
        if len(batch) >= batch_size:
            render_and_save(batch, output_dir, index)
            batch = []

    if batch:
        render_and_save(batch, output_dir, index)


def render_and_save(cameras, output_dir, start_index):
    for i, camera in enumerate(cameras):
        file_name = get_file_name(camera, start_index + i)
        output_path = os.path.join(output_dir, file_name)
        safe_render(camera, output_path)

    bpy.ops.wm.memory_statistics()


def render_images(output_dir, batch_size=10):
    original_camera = bpy.context.scene.camera
    cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
    setup_advanced_render_settings()

    render_batch(cameras, batch_size, output_dir)

    bpy.context.scene.camera = original_camera


def main(output_dir, resolution_x=1920, resolution_y=1080, batch_size=10):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    setup_render_settings(output_dir, resolution_x, resolution_y)
    render_images(output_dir, batch_size)


if __name__ == "__main__":
    main("../../output")
