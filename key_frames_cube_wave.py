import bpy

number = 9
counter = 0
counter2 = 0
counter3 = 0

scene = bpy.context.scene
scene.frame_start = 0
scene.frame_end = 165

collection = bpy.data.collections.new("Cubes")
bpy.context.scene.collection.children.link(collection)

for b in range(0, number):
    counter2 += 2
    counter3 = 0
    for c in range(0, number):
        bpy.ops.mesh.primitive_cube_add(size=2, location=(counter3+2, counter2-2, counter-2))
        counter3 += 2
        bpy.ops.object.move_to_collection(collection_index=2)
        

cubes = bpy.data.collections["Cubes"].objects
offset = 0

for cube in cubes:
    cube.scale = [1,1,1]
    cube.keyframe_insert(data_path = "scale", frame = 1 + offset)
    cube.scale = [1,1,7]
    cube.keyframe_insert(data_path = "scale", frame = 50 + offset)
    cube.scale = [1,1,.5]
    cube.keyframe_insert(data_path = "scale", frame = 70 + offset)
    cube.scale = [1,1,1]
    cube.keyframe_insert(data_path = "scale", frame = 80 + offset)
    offset += 1
    
def frame_change_post(scene, dg):
    objeto = bpy.context.object
    frame = scene.frame_current
    scales = bpy.context.object.scale
    print(f"frame {frame} ------------------ {scales}")

    
bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(frame_change_post)
