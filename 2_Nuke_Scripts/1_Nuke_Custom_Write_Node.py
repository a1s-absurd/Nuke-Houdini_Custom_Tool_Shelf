import nuke
import os


project  = "Film_Name"
sequence = "Sequence_Number"
shot    = "Shot_1"
version  = "v01"
render = "render"


base_path = os.path.join("D:\1_Compositing_Films", project, sequence, shot, render, version)
filename  = f"{shot}_{render}_{version}.####.exr"
output_path = os.path.join(base_path, filename).replace("\\", "/")

w = nuke.createNode("Write", inpanel=False)
w["file"].setValue(output_path)
w["channels"].setValue("rgba")
w["file_type"].setValue("exr")
w["compression"].setValue("Zip (16 scanlines)")

nuke.message(f"Custom write node generated, Please configure your directory name according to your projects")
