import bpy
import random
import math


def add_light(light_type='POINT', location=(0, 0, 0), energy=1000):
    bpy.ops.object.light_add(type=light_type, location=location)
    light = bpy.context.object
    light.data.energy = energy
    return light


def randomize_light(light):
    # Adjust these ranges based on your scene's scale
    light.location = (
        random.uniform(-20, 20),
        random.uniform(-20, 20),
        random.uniform(1, 20)
    )
    light.data.energy = random.uniform(500, 5000)

    # Randomize color (optional)
    light.data.color = (
        random.random(),
        random.random(),
        random.random()
    )

    # Randomize shadow size and softness for applicable light types
    if hasattr(light.data, 'shadow_soft_size'):
        light.data.shadow_soft_size = random.uniform(0.1, 3.0)

    # Randomize light direction for directional lights like 'SUN' or 'SPOT'
    if light.data.type in ['SUN', 'SPOT']:
        light.rotation_euler = (
            random.uniform(0, math.pi * 2),
            random.uniform(0, math.pi * 2),
            random.uniform(0, math.pi * 2)
        )


def sample_lights(num_lights=5):
    num_lights = min(num_lights, 10)
    for _ in range(num_lights):
        light_type = random.choice(['POINT', 'SUN', 'SPOT', 'AREA'])
        light = add_light(light_type=light_type)
        randomize_light(light)

