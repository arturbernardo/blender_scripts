
#source
#https://www.youtube.com/watch?v=uDtEkjbD_-g
import bpy

#delete original camera if exists
item='CAMERA'
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type=item)
bpy.ops.object.delete()

# create parameters
cube_count = 10
location_offset = 3
frame_count = 300

# set the end frame
bpy.context.scene.frame_end = frame_count

# create a row of cubes along the Y-axis
for i in range(cube_count):
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, i * location_offset, 0))

# create an empty for tracking
bpy.ops.object.empty_add()
empty = bpy.context.active_object

# animate the location property of the empty
empty.keyframe_insert("location", frame=1)
empty.location.y = cube_count * location_offset
empty.keyframe_insert("location", frame=frame_count)

# add a camera into the scene
bpy.ops.object.camera_add()
camera = bpy.context.active_object
camera.location.x = 15
camera.location.y = cube_count * location_offset / 2
camera.location.z = 2

# add a constraint to track the empty
bpy.ops.object.constraint_add(type="TRACK_TO")
camera.constraints["Track To"].target = empty
