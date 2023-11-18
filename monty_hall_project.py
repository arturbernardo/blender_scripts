import bpy
import random
import math

# camera
bpy.ops.object.camera_add()
camera = bpy.context.object
camera.location = [22, 0, 13]
camera.rotation_euler = [math.radians(63), 0, math.radians(90)]

#banner
bpy.ops.mesh.primitive_cube_add(align='WORLD', rotation=(math.radians(90), 0, math.radians(90)), location=(0, -3, 4), scale=(2, 2, 2))
banner = bpy.context.object
banner.name = 'banner'

#Material
material = bpy.data.materials.new(name="bannerMaterial")
material.diffuse_color = (1.0, 0.0, 1.0, 1.0)

#create modifier and nodes
bpy.ops.node.new_geometry_nodes_modifier()
modifier = bpy.context.object.modifiers['GeometryNodes']
node_group = modifier.node_group
node_string_to_curve = node_group.nodes.new('GeometryNodeStringToCurves')
node_value_to_string= node_group.nodes.new('FunctionNodeValueToString')

node_resample = node_group.nodes.new('GeometryNodeResampleCurve')
node_resample.mode = 'LENGTH'
node_resample.inputs[3].default_value = 0.01

node_fill = node_group.nodes.new('GeometryNodeFillCurve')
# Better topology
node_fill.mode = 'NGONS' #Triangles is default

node_value = node_group.nodes.new('ShaderNodeValue')

node_material = node_group.nodes.new('GeometryNodeSetMaterial')
node_material.inputs[2].default_value = bpy.data.materials["bannerMaterial"]


#probably exists
node_output = node_group.nodes.get("Group Output")
if (node_output == None):
    node_output = node_group.nodes.new('NodeGroupOutput')

#Remove default input if exists
to_be_removed = node_group.nodes.get("Group Input")
if (to_be_removed != None):
    node_group.nodes.remove(to_be_removed)

# Conect output to input
node_group.links.new(node_value.outputs[0], node_value_to_string.inputs[0])
node_group.links.new(node_value_to_string.outputs[0], node_string_to_curve.inputs[0])
node_group.links.new(node_string_to_curve.outputs[0], node_resample.inputs[0])
node_group.links.new(node_resample.outputs[0], node_fill.inputs[0])
node_group.links.new(node_fill.outputs[0], node_material.inputs[0])
node_group.links.new(node_material.outputs[0], node_output.inputs[0])

#Create doors
#A
bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, -6, 0), scale=(1, 1, 1))
a_door = bpy.context.object
a_door.name = "A"

#B
bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
b_door = bpy.context.object
b_door.name = "B"

#C
bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 6, 0), scale=(1, 1, 1))
c_door = bpy.context.object
c_door.name = "C"

# Monty Hall animation
counter = 0
starting_frame = 62
step_frame = 12
double_step_frame = 24

portas = [0, 0, 0]
porta_premiada = random.randint(0, 2)
portas[porta_premiada] = 1
escolha_jogador = random.randint(0, 2)
portas_disponiveis = [i for i in range(3) if i != escolha_jogador and portas[i] == 0]
porta_revelada = random.choice(portas_disponiveis)

if (porta_revelada == 0):
    a_door.location.x = 0
    a_door.keyframe_insert(data_path = "location", frame = starting_frame)
    a_door.location.x = -100
    a_door.keyframe_insert(data_path = "location", frame = starting_frame + step_frame)
    a_door.scale = [1,1,1]
    a_door.keyframe_insert(data_path = "scale", frame = starting_frame + step_frame)
    a_door.scale = [0,0,0]
    a_door.keyframe_insert(data_path = "scale", frame = starting_frame + double_step_frame)

if (porta_revelada == 1):
    b_door.location.x = 0
    b_door.keyframe_insert(data_path = "location", frame = starting_frame)
    b_door.location.x = -100
    b_door.keyframe_insert(data_path = "location", frame = starting_frame + step_frame)
    b_door.scale = [1,1,1]
    b_door.keyframe_insert(data_path = "scale", frame = starting_frame + step_frame)
    b_door.scale = [0,0,0]
    b_door.keyframe_insert(data_path = "scale", frame = starting_frame + double_step_frame)

if (porta_revelada == 2):
    c_door.location.x = 0
    c_door.keyframe_insert(data_path = "location", frame = starting_frame)
    c_door.location.x = -100
    c_door.keyframe_insert(data_path = "location", frame = starting_frame + step_frame)
    c_door.scale = [1,1,1]
    c_door.keyframe_insert(data_path = "scale", frame = starting_frame + step_frame)
    c_door.scale = [0,0,0]
    c_door.keyframe_insert(data_path = "scale", frame = starting_frame + double_step_frame)

if (escolha_jogador == porta_premiada):
    frame_atual = bpy.context.scene.frame_current
    
    node_value.outputs[0].default_value = counter
    node_value.outputs[0].keyframe_insert(data_path = "default_value", frame = starting_frame + frame_atual)
    
    counter += 1
        
    node_value.outputs[0].default_value = counter
    node_value.outputs[0].keyframe_insert(data_path = "default_value", frame = starting_frame + frame_atual + 1)
