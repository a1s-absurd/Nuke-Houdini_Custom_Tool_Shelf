import hou

def add_out_nulls_to_selected():
    selected_nodes = hou.selectedNodes()

    if not selected_nodes:
        hou.ui.displayMessage("No nodes selected. Select one or more nodes first.")
        return

    for node in selected_nodes:
        parent = node.parent()

        # Build name: _OUT_<originalname>
        out_name = "_OUT_" + node.name()

        # Create Null node
        null_node = parent.createNode("null", out_name)

        # Connect it to the selected node
        null_node.setInput(0, node)

        # Move to good position
        null_node.moveToGoodPosition()

        # Color black (RGB 0,0,0)
        null_node.setColor(hou.Color((0, 0, 0)))

        # Optionally select the new null node
        null_node.setSelected(True, clear_all_selected=False)

    hou.ui.displayMessage("Added _OUT_ Null nodes to {} node(s).".format(len(selected_nodes)))

# Run the tool
add_out_nulls_to_selected()
