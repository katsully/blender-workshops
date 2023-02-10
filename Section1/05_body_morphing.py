import bpy
import math

ctxt = bpy.context


arm = ctxt.scene.objects['Armature']
head_bone = arm.pose.bones['Head']
left_leg = arm.pose.bones['LeftUpLeg']
right_leg = arm.pose.bones['RightUpLeg']
# set rotation mode to Euler XYZ, easier to understand than default quaternions
head_bone.rotation_mode = 'XYZ'
left_leg.rotation_mode = 'XYZ'
right_leg.rotation_mode = 'XYZ'
axis = 'Z'



x = 0
angle = 0
while x <= 138:
    head_bone.rotation_euler.rotate_axis(axis, math.radians(angle))
    left_leg.rotation_euler.rotate_axis('Y', math.radians(angle))
    right_leg.rotation_euler.rotate_axis('Z', math.radians(angle))
    bpy.ops.object.mode_set(mode='OBJECT')
    head_bone.keyframe_insert(data_path='rotation_euler', frame=x)
    left_leg.keyframe_insert(data_path='rotation_euler', frame=x)
    right_leg.keyframe_insert(data_path='rotation_euler', frame=x)
    angle += .57
    x += 1
    
    
   