import bpy



total_bones = 0

# Iterate over all objects in the scene
for obj in bpy.data.objects:
    # Check if the object is a rig
    if obj.type == 'ARMATURE':
        # If it is, add the number of bones in the rig to the total
        total_bones += len(obj.data.bones)
        
# Get the selected object
obj = bpy.context.selected_objects[0]

# Disable all modifiers
for mod in obj.modifiers:
    mod.show_viewport = False
    mod.show_render = False

# Get the number of vertices
vertices = len(obj.data.vertices)

# Get the number of polygons
polygons = len(obj.data.polygons)

# Get the number of tris
tris = 0      
for poly in obj.data.polygons:
    vertice = poly.vertices
    triangles = len(vertice) - 2
    tris += triangles




# Print the results
print(total_bones)
print(obj.name)
print(polygons)
print(tris)
print(vertices)


for mod in obj.modifiers:
    mod.show_viewport = True
    mod.show_render = True
