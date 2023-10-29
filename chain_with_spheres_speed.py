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

# Substitua 'NomeDoObjeto' pelo nome do objeto que você deseja rastrear
nome_do_objeto = 'nodo_8'

# Obtém uma referência para o objeto
objeto = bpy.data.objects.get(nome_do_objeto)

# Define os frames inicial e final para calcular a velocidade
frame_inicial = 1
frame_final = bpy.context.scene.frame_end

# Lista para armazenar as velocidades calculadas frame a frame
velocidades = []

for frame in range(frame_inicial, frame_final + 1):
    # Define o frame atual
    bpy.context.scene.frame_set(frame)

    if frame > frame_inicial:
        # Obtém as matrizes de transformação dos objetos para os dois frames
        matriz_atual = objeto.matrix_world.copy()
        bpy.context.scene.frame_set(frame - 1)
        matriz_anterior = objeto.matrix_world.copy()
        bpy.context.scene.frame_set(frame)

        # Calcula a diferença na matriz de transformação (matriz de deslocamento)
        diferenca_matriz = matriz_atual.inverted() @ matriz_anterior

        # Obtém o intervalo de tempo entre os dois frames
        intervalo_tempo = 1 / bpy.context.scene.render.fps  # Use a taxa de quadros da renderização

        # Calcula a velocidade dividindo a matriz de deslocamento pelo intervalo de tempo
        velocidade = diferenca_matriz.to_translation() / intervalo_tempo

        # Adiciona a velocidade calculada à lista
        velocidades.append((frame, velocidade))


# Agora você tem uma lista de tuplas contendo o número do frame e a velocidade do objeto em cada frame
for frame, velocidade in velocidades:
    # length calcula a magnitude. Calculando a hipotenusa. Caso necessario, calcula isso em 3D. 
    #Deve ter alguma relacao com a area da superfice da dimensao que corresponde a hipotenusa.
    magnitude = velocidade.length
    print(f"Frame {frame}: Velocidade ({velocidade.x}, {velocidade.y}, {velocidade.z}), Magnitude: {magnitude}")
    
    
#bpy.context.scene.frame_set(1)

#bpy.ops.screen.animation_play()
