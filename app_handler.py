import bpy

model_name = "generic_tyre"
model_material_name = "generic_tyre"

def change_material(new_material_name,old_material_name):

    obj = bpy.data.objects[model_name]

    # Find the material index by name
    mat_index = -1
    for i, mat_slot in enumerate(obj.material_slots):
        if mat_slot.name == old_material_name:
            mat_index = i
            break

    # If the material was found
    if mat_index != -1:
        # Get the new material by name
        new_mat = bpy.data.materials.get(new_material_name)
        # If the new material exists
        if new_mat:
            # Assign the new material to the object
            obj.material_slots[mat_index].material = new_mat
        else:
            print(f"Material {new_mat_name} not found.")
    else:
        print(f"Material {old_mat_name} not found.")





def run_script_on_keyframe(scene):
    if bpy.context.scene.frame_current == 1:
        # Set the render resolution
        bpy.context.scene.render.resolution_x = 1200
        bpy.context.scene.render.resolution_y = 1200
    else:
        # Set the render resolution
        bpy.context.scene.render.resolution_x = 1920
        bpy.context.scene.render.resolution_y = 1080
        
    # Set the aspect ratio
    bpy.context.scene.render.pixel_aspect_x = 1
    bpy.context.scene.render.pixel_aspect_y = 1
    
    if bpy.context.scene.frame_current in [13,14,15]:
        # Add the wireframe modifier
        
        obj = bpy.data.objects[model_name]
        

        
        if obj.modifiers.get("Wireframe") is not None:
            obj.modifiers.remove(obj.modifiers.get("Wireframe"))  
        
        mod = obj.modifiers.new(name="Wireframe", type='WIREFRAME')
        
        mod.use_replace = False
        mod.use_even_offset = True
        mod.use_relative_offset = True
        mod.thickness = 0.02
        mod.material_offset = 1
        
        bpy.ops.object.modifier_move_to_index({'object': obj},modifier='Wireframe', index=0)
        
        # Disable all modifiers
        for mod in obj.modifiers:
            if mod.name != "Wireframe":
                mod.show_viewport = False
                mod.show_render = False
            
        change_material("white","generic_tyre")
        
        
    else:        
        obj = bpy.data.objects[model_name]
        if obj.modifiers.get("Wireframe") is not None:
            obj.modifiers.remove(obj.modifiers.get("Wireframe"))  
            
        # Disable all modifiers
        for mod in obj.modifiers:
            if mod.name != "Wireframe":
                mod.show_viewport = True
                mod.show_render = True
        
        change_material(model_material_name,"white")
            
    

bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(run_script_on_keyframe)
