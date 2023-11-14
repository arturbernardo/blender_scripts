import bpy

sphere = bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
curve = bpy.ops.curve.primitive_bezier_circle_add(radius=6, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

camera = bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(1.10871, 0.0132652, 1.14827), scale=(1, 1, 1))
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["BezierCircle"]
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Icosphere"]
bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')
