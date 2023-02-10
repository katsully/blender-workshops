import bpy
from random import randint, uniform
from math import pi
import math
import random

for mesh in bpy.data.meshes:
    if mesh is not bpy.data.meshes['Plane']:
        bpy.data.meshes.remove(mesh)

# all caps variable indicates we don't want these values to change
RND_VAL = 1.3
cubes = []

# create the cubes
for i in range(50):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(uniform(-RND_VAL, RND_VAL),uniform(-RND_VAL, RND_VAL),uniform(-RND_VAL, RND_VAL)), scale=(uniform(.5,1),uniform(.5,1),uniform(.5,1)) )
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bevel(offset=0.05, segments=4)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    new_mat = bpy.data.materials.new(name='Test')
    new_mat.use_nodes = True
    nodes = new_mat.node_tree.nodes
    nodes["Principled BSDF"].inputs[0].default_value = (random.random(),random.random(),random.random(),1)

    bpy.context.active_object.data.materials.append(new_mat)
    # store the cubes in a list
    cubes.append(bpy.context.active_object)
    
frame_number = 0

# set your keyframes and move the cubes    
for i in range(0,100):
    for cube in cubes:
        bpy.context.scene.frame_set(frame_number)
        cube.rotation_euler.z += .5
        cube.keyframe_insert(data_path='rotation_euler', index=2)
    frame_number += 5
        
    
    
    