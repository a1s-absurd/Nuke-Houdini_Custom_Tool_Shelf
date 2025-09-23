# Nuke-Houdini_Custom_Tool_Shelf
Python files to customize Nuke and Houdini interface by creating custom nodes for cleaner workflow.

🌀 Houdini Tools
- Version-Up HIP

1) Click the “Version Up” button in your custom shelf.
HIP file versions up only if the filename matches the filename_version.extension format.

2) Publish Project
Click “Publish Project.”
Choose a destination (OneDrive) and whether to include cache files.
The project copies to the shared drive.

3) Add OUT Null
Select one or multiple nodes.
Click “Add OUT Null.”
Null nodes with _OUT_ prefix are created, connected, positioned neatly, and colored black.
-----------------------------------------------------

🎬 Nuke Tools
1) Custom Write Node
Go to the toolbar → Custom → “Create Write Node.”
A Write node with prefilled paths appears based on your project/shot info.

2) Split EXR
Select a Read node pointing to a multi-channel EXR file.
Click the “Split EXR” button.
Shuffle nodes for each channel are created automatically.

3) Cleanup Script
From the menu: Tools → “Clean Up Script.”
All unnecessary nodes are removed and the graph is optimized.
