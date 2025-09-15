import hou
import os
import re

def version_up_current_hip():
    # Get current hip file path
    current_path = hou.hipFile.path()  # returns '' for new/unsaved scene
    
    if not current_path:
        hou.ui.displayMessage("Current HIP is unsaved. Save the file first with the required naming format:\n\n<name>_v###.hipnc (e.g. hero_shot_v001.hipnc)")
        return

    # Use only filename for pattern matching (but we will preserve directory)
    dirname, filename = os.path.split(current_path)

    # Recommended pattern: <basename>_vNNN.<ext>
    # Accepts .hip, .hipnc, .hiplc and variable number of digits (but prefer 3+)
    pattern = r'^(?P<base>.+)_v(?P<ver>\d+)\.(?P<ext>hip|hipnc|hiplc)$'
    m = re.match(pattern, filename, re.IGNORECASE)
    if not m:
        # Do NOT attempt to version up if not matching
        hou.ui.displayMessage(
            "Filename does not follow the required pattern:\n\n"
            "<name>_v###.hip( nc | lc )\n\n"
            "Example: hero_shot_v001.hipnc\n\n"
            "No action taken."
        )
        return

    base = m.group('base')
    ver_str = m.group('ver')
    ext = m.group('ext')

    # parse and increment version number (preserve zero padding length)
    ver_len = len(ver_str)
    try:
        ver_num = int(ver_str)
    except ValueError:
        hou.ui.displayMessage("Version number parsing error. No action taken.")
        return

    next_ver_num = ver_num + 1
    next_ver_str = str(next_ver_num).zfill(ver_len)

    new_filename = f"{base}_v{next_ver_str}.{ext}"
    new_path = os.path.join(dirname, new_filename)

    # If a file with new_path already exists, prompt user for overwrite or cancel
    if os.path.exists(new_path):
        choice = hou.ui.displayMessage(
            "Target file already exists:\n\n{}\n\nOverwrite?".format(new_path),
            buttons=("Overwrite", "Cancel"),
            severity=hou.severityType.Warning
        )
        if choice != 0:
            # user clicked Cancel
            hou.ui.displayMessage("Operation cancelled. No file written.")
            return

    # Save (this will change the current HIP path to new_path)
    try:
        hou.hipFile.save(new_path)
    except Exception as e:
        hou.ui.displayMessage("Failed to save new HIP:\n\n{}".format(str(e)))
        return

    hou.ui.displayMessage("Saved new version:\n\n{}".format(new_path))

# Run tool
version_up_current_hip()
