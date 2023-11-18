import bpy

# Select cube
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['Cube']

#add object to context
obj = bpy.context.active_object

#create modifier and nodes
bpy.ops.node.new_geometry_nodes_modifier()
modifier = bpy.context.object.modifiers['GeometryNodes']
node_group = modifier.node_group
node_string_to_curve = node_group.nodes.new('GeometryNodeStringToCurves')
node_value_to_string= node_group.nodes.new('FunctionNodeValueToString')
node_value = node_group.nodes.new('ShaderNodeValue')
#probably exists
node_output = node_group.nodes.get("Group Output")
if (node_output == None):
    node_output = node_group.nodes.new('NodeGroupOutput')

#Remove default input
to_be_removed = node_group.nodes.get("Group Input")
if (to_be_removed != None):
    node_group.nodes.remove(to_be_removed)

# Conect output to input
node_group.links.new(node_value.outputs[0], node_value_to_string.inputs[0])
node_group.links.new(node_value_to_string.outputs[0], node_string_to_curve.inputs[0])
node_group.links.new(node_string_to_curve.outputs[0], node_output.inputs[0])
