import bpy


#Variables
x_nodo_pos = 0
sphere_list = []

# cria gravidade na cena
intensidade_gravidade = 9.81
scene = bpy.context.scene
scene.gravity = (0, 0, -intensidade_gravidade) 

# Cria objetos
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(x_nodo_pos, 0, 0))
esfera = bpy.context.object
esfera.name = "nodo_0"
bpy.context.view_layer.objects.active = esfera
bpy.ops.rigidbody.object_add(type='PASSIVE')
esfera.rigid_body.collision_shape = 'SPHERE'
sphere_list.append(esfera)
#x_nodo_pos = esfera.location.x + esfera.dimensions.x

for n in range (1, 20):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(x_nodo_pos, 0, 0))
    esfera = bpy.context.object
    esfera.name = "nodo_"+str(n)
    bpy.context.view_layer.objects.active = esfera
    bpy.ops.rigidbody.object_add(type='ACTIVE')
    esfera.rigid_body.collision_shape = 'SPHERE'
    sphere_list.append(esfera)
    x_nodo_pos = esfera.location.x + esfera.dimensions.x
    print(esfera.name)
    print(esfera.dimensions.x)

for n in range(0, len(sphere_list) - 1):
    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(sphere_list[n].location.x + sphere_list[n].dimensions.x/2, 0, 0), scale=(1, 1, 1))
    bpy.ops.rigidbody.constraint_add()
    bpy.context.object.rigid_body_constraint.type = 'POINT'
    bpy.context.object.rigid_body_constraint.object1 = sphere_list[n]
    bpy.context.object.rigid_body_constraint.object2 = sphere_list[n+1]