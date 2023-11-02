#https://www.youtube.com/watch?v=Xrixs_XuDQo

import csv
import bpy

bar_spacing = 1.5
bar_width = 1

with open('/sample.csv') as f:
    readout = list(csv.reader(f))

for a in readout:
    placement = readout.index(a)
    bpy.ops.mesh.primitive_plane_add(size=1)
    new_bar = bpy.context.object
    
    for vert in new_bar.data.vertices:
        vert.co[1] += 0.5
        vert.co[0] += placement*bar_spacing + 0.5
        
    new_bar.scale = (bar_width, float(a[1]), 1)
    
    bpy.ops.object.text_add()
    bpy.context.object.data.align_x = 'LEFT'
    bpy.context.object.data.align_y = 'CENTER'
    bpy.ops.transform.rotate(value=1.5708)
    bpy.ops.transform.translate(value=(placement*bar_spacing + 0.5, -0.5, 0))
    bpy.context.object.data.body = a[0]
    
print (dir(bpy))

