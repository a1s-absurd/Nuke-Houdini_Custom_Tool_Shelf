# Nuke-Houdini_Custom_Tool_Shelf
Python files to customize Nuke and Houdini interface by creating custom nodes for cleaner workflow.

Custom Tools for Houdini & Nuke

This repository contains custom Python scripts designed to streamline workflows in Nuke and Houdini. These scripts automate common tasks like versioning, EXR splitting, publishing, and node cleanup, reducing repetitive manual work and enforcing naming/organization standards.

These scripts provide:

Automated creation of standardized Write nodes.

Splitting of multi-channel EXR files into separate Shuffle nodes.

Node graph cleanup and optimization.

Version-up checks for Houdini HIP files.

Publishing projects to a shared drive with cache options.

Automatic addition of OUT Null nodes with proper positioning and color coding.

Features
Nuke Tools

Custom Write Node

Creates a Write node with a preconfigured output path based on shot info (project, sequence, shot number, version).

Ensures consistent naming conventions across projects.

Split EXR Button

Adds a “Split EXR” button in the menu.

Automatically generates multiple Shuffle nodes for each pass/channel in a multi-channel EXR file.

Nuke Script Cleanup

Cleans up the Nuke file by:

Removing unnecessary or error nodes.

Disabling unused branches.

Optimizing the node graph for performance and readability.

Houdini Tools

Version-Up Check

Checks the current HIP file name against a recommended pattern (filename_version.extension).

Versions up only if the naming convention matches.

Project Publishing

Copies the contents of the current Houdini project to a shared drive (preferably OneDrive).

Offers a dialog box to choose whether to include or exclude cache files.

Add OUT Null Node

Adds and connects a Null node to selected nodes.

Automatically names it with the _OUT_ prefix.

Positions it using .moveToGoodPosition() for neat graph layout.

Colors the node black for quick identification.

Installation
Nuke

Copy the Python scripts to your ~/.nuke directory.

Add the menu integration code to your menu.py file to show buttons like Split EXR.

Houdini

Copy the Python scripts to your Documents/houdiniXX.X/scripts/python folder.

Create a custom shelf tool and assign the Python scripts to the buttons.

Usage
Nuke

Custom Write Node

Go to the toolbar → Custom → “Create Write Node.”

A Write node with prefilled paths appears based on your project/shot info.

Split EXR

Select a Read node pointing to a multi-channel EXR file.

Click the “Split EXR” button.

Shuffle nodes for each channel are created automatically.

Cleanup Script

From the menu: Tools → “Clean Up Script.”

All unnecessary nodes are removed and the graph is optimized.

Houdini

Version-Up HIP

Click the “Version Up” button in your custom shelf.

HIP file versions up only if the filename matches the filename_version.extension format.

Publish Project

Click “Publish Project.”

Choose a destination (OneDrive) and whether to include cache files.

The project copies to the shared drive.

Add OUT Null

Select one or multiple nodes.

Click “Add OUT Null.”

Null nodes with _OUT_ prefix are created, connected, positioned neatly, and colored black.

Requirements

Nuke: v11+ with Python support.

Houdini: v18+ with Python 3 support.

Access to OneDrive or any shared drive for publishing.
