import bpy
import math

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

for n in range (1, 10):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(x_nodo_pos, 0, 0))
    esfera = bpy.context.object
    esfera.name = "nodo_"+str(n)
    bpy.context.view_layer.objects.active = esfera
    bpy.ops.rigidbody.object_add(type='ACTIVE')
    esfera.rigid_body.collision_shape = 'SPHERE'
    sphere_list.append(esfera)
    x_nodo_pos = esfera.location.x + esfera.dimensions.x

for n in range(0, len(sphere_list) - 1):
    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(sphere_list[n].location.x + sphere_list[n].dimensions.x/2, 0, 0), scale=(1, 1, 1))
    bpy.ops.rigidbody.constraint_add()
    bpy.context.object.rigid_body_constraint.type = 'POINT'
    bpy.context.object.rigid_body_constraint.object1 = sphere_list[n]
    bpy.context.object.rigid_body_constraint.object2 = sphere_list[n+1]


names = ("nodo_5",)
def frame_change_post(scene, dg):
    frame = scene.frame_current
    for name in names:
        objeto = dg.objects.get(name)
        matriz_atual = objeto.matrix_world.copy()
        matriz_anterior = objeto.matrix_world.copy()

        # Calcula a diferença na matriz de transformação (matriz de deslocamento)
        diferenca_matriz = matriz_atual.inverted() @ matriz_anterior

        # Obtém o intervalo de tempo entre os dois frames
        intervalo_tempo = 1 / bpy.context.scene.render.fps  # Use a taxa de quadros da renderização

        # Calcula a velocidade dividindo a matriz de deslocamento pelo intervalo de tempo
        velocidade = diferenca_matriz.to_translation() / intervalo_tempo

        # Adiciona a velocidade calculada à lista
        velocidades.append((frame, velocidade))
        print(f"frame {frame} ------------------")
            
velocidades = []
bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(frame_change_post)
