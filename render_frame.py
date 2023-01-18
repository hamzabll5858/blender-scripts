import bpy

# Set the frame to render
bpy.context.scene.frame_set(1)

# Set the output path and file name
bpy.context.scene.render.filepath = "//..\\..\\renders\\-01.png"

# Render the frame
bpy.ops.render.render(write_still=True)

bpy.context.scene.render.filepath = "//..\\..\\renders\\-##"