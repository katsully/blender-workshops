import bpy
from random import randint, uniform
from math import pi
import random

# if you want to use predetermined colors
colors = [
    (0.0, 1.0, 0.7, 1.0),
    (0.6, 0.0, 1.0, 1.0),
    (0.9, 0.5, 0.0, 1.0),
    (1.0, 0.5 ,1.0, 1.0)
    ]

frame_number = 0
        
rig = bpy.data.objects['Armature']
# go through each mesh in your avatar
for obj in bpy.data.objects:
    if obj.parent == rig:
        mat = obj.data.materials[0]
        new_mat = bpy.data.materials.new(name='Test')
        new_mat.use_nodes = True
        nodes = new_mat.node_tree.nodes
        nodes["Principled BSDF"].inputs[0].default_value = random.choice(colors)
        #nodes["Principled BSDF"].inputs[0].default_value = (random.random(),random.random(),random.random(),1)
        obj.data.materials[0] = new_mat
    
    # change the colors and set your keyframes    
for i in range(0,50):
    bpy.context.scene.frame_set(frame_number)
    for obj in bpy.data.objects:
        if obj.parent == rig:
            nodes = obj.data.materials[0].node_tree.nodes
            nodes["Principled BSDF"].inputs[0].default_value = random.choice(colors)
            #nodes["Principled BSDF"].inputs[0].default_value = (random.random(),random.random(),random.random(),1)
            nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path='default_value')
    frame_number += 10