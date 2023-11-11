import bpy
from math import sin

for i in range(20):
    x, y, z = 0, i*2, sin(i)*2
    bpy.ops.mesh.primitive_cube_add(
        location = [x, y, z]
    )
    
