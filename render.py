import bpy


scene = bpy.context.scene

# Frame range
scene.frame_start = 1
scene.frame_end = 100
scene.frame_set(scene.frame_start)

# Output path
scene.render.filepath = "//frames/frame_"

# Render resolution
scene.render.resolution_x = 1920 # 3840
scene.render.resolution_y = 1080 # 2160
scene.render.fps = 24 # 30 # 60

# Image format
#scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.file_format = "OPEN_EXR"
scene.render.image_settings.color_mode = "RGBA"
scene.render.image_settings.color_depth = "16"
scene.render.image_settings.exr_codec = "ZIP"

# Render animation
bpy.ops.render.render(animation=True)
