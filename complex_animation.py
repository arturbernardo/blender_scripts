import bpy
import math

#A
bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, -6, 0), scale=(1, 1, 1))
a_door = bpy.context.object
a_door.name = "A"

a_door.location.z = -10
a_door.keyframe_insert(data_path = "location", frame = 1)
a_door.rotation_euler.z = math.radians(0) #
a_door.keyframe_insert(data_path = "rotation_euler", frame = 1) #

a_door.location.z = 0
a_door.keyframe_insert(data_path = "location", frame = 80)
a_door.rotation_euler.z = math.radians(360) #
a_door.keyframe_insert(data_path = "rotation_euler", frame = 80) #

#B
bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
b_door = bpy.context.object
b_door.name = "B"

b_door.location.z = -10
b_door.keyframe_insert(data_path = "location", frame = 1)
b_door.rotation_euler.z = math.radians(0) #
b_door.keyframe_insert(data_path = "rotation_euler", frame = 1) #

b_door.location.z = 0
b_door.keyframe_insert(data_path = "location", frame = 80)
b_door.rotation_euler.z = math.radians(360) #
b_door.keyframe_insert(data_path = "rotation_euler", frame = 80) #

#C
bpy.ops.mesh.primitive_cube_add(align='WORLD', location=(0, 6, 0), scale=(1, 1, 1))
c_door = bpy.context.object
c_door.name = "C"

c_door.location.z = -10
c_door.keyframe_insert(data_path = "location", frame = 1)
c_door.rotation_euler.z = math.radians(0) #
c_door.keyframe_insert(data_path = "rotation_euler", frame = 1) #

c_door.location.z = 0
c_door.keyframe_insert(data_path = "location", frame = 80)
c_door.rotation_euler.z = math.radians(360) #
c_door.keyframe_insert(data_path = "rotation_euler", frame = 80) #
