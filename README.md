# app_handler.py
This file is used to register a handler on each frame change in blender. I use it to change resolution of camera, change model to wireframe and vice versa
!NOTE! resolution will not change in rendering mode, It only changes in UI mode

# render_frame.py
Due to above mentioned problem I render first frame separatly. This file helps me do that

# export.py
To export the selected model to all formats including fbx, gltf, obj, dae to certain path

# print_info.py
Will print model name and print vertices, polygon and tris count