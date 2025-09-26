import hou

def add_out_nulls_to_selected():
    selected_nodes = hou.selectedNodes()

    if not selected_nodes:
        hou.ui.displayMessage("No nodes selected. Select one or more nodes first.")
        return

    for node in selected_nodes:
        parent = node.parent()

       
        out_name = "_OUT_" + node.name()

      
        null_node = parent.createNode("null", out_name)

        null_node.setInput(0, node)

        null_node.moveToGoodPosition()

      
        null_node.setColor(hou.Color((0, 1, 0)))

        
        null_node.setSelected(True, clear_all_selected=False)

    hou.ui.displayMessage("Added _OUT_ Null nodes to {} node(s).".format(len(selected_nodes)))

# Run the tool
add_out_nulls_to_selected()
