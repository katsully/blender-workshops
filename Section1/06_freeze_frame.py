import bpy

ctxt = bpy.context


# Active object
ob = ctxt.object

new_mat = bpy.data.materials.new(name="Lerping")
mat_name = new_mat.name
r_val = 0.0
b_val = 1.0
new_mat.use_nodes = True
nodes = new_mat.node_tree.nodes
nodes["Principled BSDF"].inputs[0].default_value = (r_val, 0, b_val, 1)

if ob.type == 'ARMATURE':
    armature = ob.data

meshes = []
for obj in ctxt.scene.objects:
    if (obj.type == 'MESH' and obj.name != 'Plane'):
        obj.data.materials[0] = new_mat
        meshes.append(obj)


x = 0
while x <= 138:
    r_val += .007
    b_val -= .007
    print(b_val)
    ctxt.scene.frame_set(x)
    cleaned_copy = ob.copy()
    cleaned_copy.data = ob.data.copy()
    cleaned_copy.animation_data_clear()
    cleaned_copy.hide_render = True
    cleaned_copy.hide_viewport = True
    cleaned_copy.keyframe_insert(data_path="hide_viewport", frame=0)
    cleaned_copy.keyframe_insert(data_path="hide_render", frame=0)
    cleaned_copy.hide_render = False
    cleaned_copy.hide_viewport = False
    cleaned_copy.keyframe_insert(data_path="hide_viewport", frame=x)
    cleaned_copy.keyframe_insert(data_path="hide_render", frame=x)
    
    
    # get some specific node:
    # returns None if the node does not exist
    base = nodes.get("Principled BSDF")
    base.inputs[0].default_value = (r_val, 0, b_val, 1)
    # add keyframe to strength at frame 1
    base.inputs[0].keyframe_insert("default_value", frame=x)

    ctxt.collection.objects.link(cleaned_copy)
    for m in meshes:
        new_mesh = m.copy()
        new_mesh.modifiers["Armature"].object = bpy.data.objects[cleaned_copy.name]
        new_mesh.parent = cleaned_copy
        # hide the static pose at the beginning
        new_mesh.hide_render = True
        new_mesh.hide_viewport = True
        new_mesh.keyframe_insert(data_path="hide_viewport", frame=0)
        new_mesh.keyframe_insert(data_path="hide_render", frame=0)
        # add in the static pose at the point the animation passes through
        new_mesh.hide_render = False
        new_mesh.hide_viewport = False
        new_mesh.keyframe_insert(data_path="hide_viewport", frame=x)
        new_mesh.keyframe_insert(data_path="hide_render", frame=x)
        ctxt.collection.objects.link(new_mesh)
    
    x += 1
    # lerp from blue to red
    r_val += .007
    b_val -= .007
    

# hide the orignal animation
for m in meshes:
    m.hide_render = True
    m.hide_viewport = True
    m.keyframe_insert(data_path="hide_viewport", frame=0)
    m.keyframe_insert(data_path="hide_render", frame=0)