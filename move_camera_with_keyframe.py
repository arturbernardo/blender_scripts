import bpy
from math import radians

# Limpa a cena atual
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Adiciona uma esfera
bpy.ops.mesh.primitive_uv_sphere_add(radius=2, location=(0, 0, 0))
sphere = bpy.context.active_object

# Adiciona uma câmera
bpy.ops.object.camera_add(location=(0, -5, 0), rotation=(radians(90), 0, 0))
camera = bpy.context.active_object

# Configuração de constraints
bpy.ops.object.constraint_add(type='TRACK_TO')
constraint = camera.constraints.new(type='TRACK_TO')
constraint.target = sphere
constraint.track_axis = 'TRACK_NEGATIVE_Z'

# Configuração da animação
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 250

# Adiciona keyframes para a animação da posição da câmera
camera.location.x = 5
camera.keyframe_insert(data_path="location", index=0, frame=1)
camera.location.x = -5
camera.keyframe_insert(data_path="location", index=0, frame=250)

# Renderização
#bpy.context.scene.render.image_settings.file_format = 'PNG'
#bpy.context.scene.render.filepath = "//output.png"
#bpy.ops.render.render(write_still=True)
