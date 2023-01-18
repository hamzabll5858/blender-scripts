import bpy


model_name = "generic_tyre"

# Get the desired collection by name
collection = bpy.data.collections.get("models")

# Select all objects in the collection
for obj in collection.objects:
    obj.select_set(True)

# Set the active object to the first object in the collection
bpy.context.view_layer.objects.active = collection.objects[0]


# Store the selected objects in a variable
selected_objects = bpy.context.selected_objects

# Set the export path and file name
path = "../fbx/{model_name}.fbx".format(model_name=model_name)

# Set the export options
bpy.ops.export_scene.fbx(filepath=path, use_selection=True,
                        embed_textures=True,
                        bake_anim=False,
                        path_mode='COPY')

# Set the selected objects back
bpy.ops.object.select_all(action='DESELECT')
for obj in selected_objects:
    obj.select_set(True)
    
    
# Set the export path and file name
path = "../obj/{model_name}.obj".format(model_name=model_name)

# Set the export options
bpy.ops.export_scene.obj(filepath=path, use_selection=True)


# Set the selected objects back
bpy.ops.object.select_all(action='DESELECT')
for obj in selected_objects:
    obj.select_set(True)
    
# Set the export path and file name
path = "../dae/{model_name}.dae".format(model_name=model_name)
    
bpy.ops.wm.collada_export(filepath=path)


# Set the export path and file name
path = "../gltf/{model_name}.gltf".format(model_name=model_name)

bpy.ops.export_scene.gltf(filepath=path, 
                         export_materials='EXPORT',
                         export_format='GLTF_EMBEDDED',
                         export_apply=True,
                         use_selection=True,
                         export_animations=False)
                         
