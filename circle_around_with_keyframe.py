import bpy
import math

# Limpar a cena atual
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Adicionar um objeto vazio (como um ponto de controle)
bpy.ops.object.empty_add(location=(0, 0, 0))

# Configurar a animação
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 360
radius = 3.0  # Ajuste conforme necessário

# Adicionar keyframes para animação circular
obj = bpy.context.object

for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end + 1):
    angle = frame * 1  # Ajuste conforme necessário
    angleRad = math.radians(angle)
    x = radius * math.cos(angleRad)
    y = radius * math.sin(angleRad)
    obj.location = (x, y, 0)
    obj.keyframe_insert(data_path="location", index=-1, frame=frame)

# Reproduzir a animação
bpy.ops.screen.animation_play()
