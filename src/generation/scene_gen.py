import blenderproc as bproc
import argparse
import numpy as np







objs = bproc.loader.load_obj("mymesh.obj")

# Changing poses

objs.set_location([2, 0, 1])
objs.set_rotation_euler([np.pi, 0, 0])
objs.apply_T(tmat)

# Camera configuration

bproc.camera.set_intrinsics_from_blender_params(lens=focal_length, lens_unit="MILLIMETERS")
bproc.camera.set_intrinsics_from_blender_params(lens=field_of_view, lens_unit="FOV")
bproc.camera.add_camera_pose(tmat) # tmat is a 4x4 numpy array

# Rendering

data = bproc.renderer.render()
bproc.renderer.enable_distance_output()
bproc.renderer.enable_depth_output()
bproc.renderer.enable_normals_output()
data = bproc.renderer.render_segmap(map_by=["instance", "class", "name"])
data = bproc.renderer.render_optical_flow()

# Writer

bproc.writer.write_hdf5()
# blenderproc vis hdf5 <path_to_file>
bproc_writer.write_coco_annotations()
# blenderproc vis coco <path_to_file>

# Key frames

# When calling bproc.renderer.render() blender will go over all keyframes in the interval [frame_start, frame_end - 1]
bproc.camera.add_camera_pose(matrix_world) # -> frame_end is increased by one
obj.set_location(location, frame=i) # assign object poses to a specific frame i

# Structure
"""<object loading>

<light creation>

for r in range(NUM_RUNS):
    bproc.utility.reset_keyframes()

    <setting random object poses>

    <setting random light poses & strengths>

    <camera sampling>

    <rendering>

    <writing to file>
"""
