def split_exr():

    sel = nuke.selectedNode()
    if sel.Class() != "Read":
        nuke.message("Please select a Read node that imports a .exr file.")
        return
    
    channels = nuke.channels(sel.name())
    layers = sorted(set([c.split('.')[0] for c in channels]))

    for layer in layers:
        shuffle = nuke.createNode("Shuffle")
        shuffle["in"].setValue(layer)
        shuffle["postage"].setValue(1)
        shuffle["label"].setValue(layer)
        shuffle.setInput(0, sel)
        shuffle.setName(f"Shuffle_{layer}")
        shuffle.setYpos(sel.ypos() + 100)
        shuffle.setXpos(sel.xpos() + 150 * layers.index(layer))

    nuke.message(f"Created {len(layers)} Shuffle nodes from EXR.")
custom_menu.addCommand("Split EXR", "split_exr()")
