def clean_up_script():
 
    count_removed = 0
    count_disabled = 0

    for node in nuke.allNodes():
        try:
          
            if node.Class() == "Viewer":
                continue
            if node.error() or node["disable"].value():
                node["disable"].setValue(True)
                count_disabled += 1
            
            if node.Class() in ["StickyNote", "BackdropNode"] and not node.inputs():
                nuke.delete(node)
                count_removed += 1
        except Exception as e:
            continue

   
    nuke.root().begin()
    nuke.autoplace_all_nodes()
    nuke.message(f"Cleanup complete.\nRemoved: {count_removed} | Disabled: {count_disabled}")

custom_menu.addCommand("Clean Up Script", "clean_up_script()")
