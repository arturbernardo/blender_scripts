import bpy
import numpy as np
from math import sin

virtualSin = bpy.data.meshes.new('sin')

n = 100
virtualSin.vertices.add(n)
virtualSin.edges.add(n-1)

yDots = np.linspace( 0, 10, 100 )

for i, y in zip( range(n), yDots ):       
    virtualSin.vertices[i].co = (0, y, sin(y))
    
    if i < n - 1:
        virtualSin.edges[i].vertices = (i, i+1)

sin = bpy.data.objects.new('sin', virtualSin)
bpy.context.scene.collection.objects.link(sin)
