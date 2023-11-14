import bpy

# Adiciona esfera
sphere = bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# Adiciona curva bezier
curve = bpy.ops.curve.primitive_bezier_circle_add(radius=6, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# Adiciona câmera
camera = bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(1.10871, 0.0132652, 1.14827), scale=(1, 1, 1))

# Adiciona constraint Follow Path à câmera
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["BezierCircle"]

# Adiciona constraint Track To à câmera
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Icosphere"]

# Animação do constraint Follow Path
bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')

bpy.context.scene.frame_set(1)
bpy.context.object.constraints["Follow Path"].offset = 0
bpy.context.object.constraints["Follow Path"].keyframe_insert(data_path="offset")

bpy.context.scene.frame_set(60)
bpy.context.object.constraints["Follow Path"].offset = 30
bpy.context.object.constraints["Follow Path"].keyframe_insert(data_path="offset")

bpy.context.scene.frame_set(200)
bpy.context.object.constraints["Follow Path"].offset = 100
bpy.context.object.constraints["Follow Path"].keyframe_insert(data_path="offset")
