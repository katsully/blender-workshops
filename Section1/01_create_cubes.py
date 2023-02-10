import bpy
from random import randint, uniform
import math

# delete all meshes except the background, allows you to run this multiple times
for mesh in bpy.data.meshes:
    if mesh is not bpy.data.meshes['Plane']:
        bpy.data.meshes.remove(mesh)

# this number will be used to determine the bounding box of the generated cubes
RND_VAL = 1.5

# create a for loop that runs 50 times
for i in range(50):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(uniform(-RND_VAL, RND_VAL),uniform(-RND_VAL, RND_VAL),uniform(-RND_VAL, RND_VAL)), scale=(uniform(.5,1),uniform(.5,1),uniform(.5,1)) )
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bevel(offset=0.05, segments=4)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')