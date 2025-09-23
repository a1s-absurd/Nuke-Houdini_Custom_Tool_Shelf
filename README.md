# Nuke-Houdini_Custom_Tool_Shelf
Python files to customize Nuke and Houdini interface by creating custom nodes for cleaner workflow.

🎨 Custom Houdini & Nuke Tools

Welcome to the Pipeline Helper Pack — a collection of custom Python tools for Nuke 🖌️ and Houdini 🌀.
These scripts automate repetitive tasks, enforce naming conventions, and speed up your compositing/FX workflows.
This toolkit provides:

✅ Pre-configured Write nodes with automatic shot path generation.
✅ One-click EXR splitting into Shuffle nodes.
✅ Nuke script cleanup and optimization.
✅ Houdini versioning & project publishing with cache options.
✅ Auto OUT-Null node creation with proper layout & color coding.

🧰 Features
🎬 Nuke Tools
Tool	Icon	Description
Custom Write Node	📝	Creates Write nodes with automatic paths based on project/sequence/shot/version. Consistent naming guaranteed.
Split EXR Button	🧩	Adds a “Split EXR” button to menu. Automatically generates multiple Shuffle nodes from a multi-channel EXR.
Nuke Script Cleanup	🧹	Removes unnecessary/error nodes, disables unused branches, and optimizes the node graph for speed.
🌀 Houdini Tools
Tool	Icon	Description
Version-Up HIP	🔄	Checks HIP file name (must match filename_version.extension) and versions up only if valid.
Project Publishing	☁️	Copies the current project to a shared drive (e.g. OneDrive). Offers dialog to include/exclude cache files.
Add OUT Null	🎯	Adds and connects Null nodes to selected nodes. Auto-names with _OUT_, positions neatly with .moveToGoodPosition(), and colors them black.
⚙️ Installation
🎬 Nuke

Copy Python scripts into your ~/.nuke folder.

Add button/menu integration code to your menu.py.

🌀 Houdini

Copy Python scripts into Documents/houdiniXX.X/scripts/python.

Create a custom shelf tool in Houdini and link the Python code.

💡 Tip: Name your shelf “Pipeline Tools” with nice icons for quick access.

📝 Usage Guide
🎬 Nuke

📝 Custom Write Node

Toolbar → Custom → “Create Write Node.”

Generates a Write node with prefilled paths.

🧩 Split EXR

Select a Read node pointing to a multi-channel EXR.

Click “Split EXR.”

Shuffle nodes for each pass are auto-created.

🧹 Cleanup Script

Tools → “Clean Up Script.”

Graph optimized in one click.

🌀 Houdini

🔄 Version-Up HIP

Click “Version Up” on your custom shelf.

Only versions up if name pattern is correct.

☁️ Publish Project

Click “Publish Project.”

Choose OneDrive/Shared folder & include/exclude cache files.

🎯 Add OUT Null

Select nodes → “Add OUT Null.”

Creates Null nodes with _OUT_ prefix, black color, and neat layout.

📦 Requirements

Nuke: v11+ with Python support.

Houdini: v18+ with Python 3 support.

Access to OneDrive or shared drive for publishing.
