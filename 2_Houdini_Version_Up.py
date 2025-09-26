import hou
import os
import re

def version_up_current_hip():
  
    current_path = hou.hipFile.path() 
    
    if not current_path:
        hou.ui.displayMessage("Current HIP is unsaved. Save the file first with the required naming format:\n\n<name>_v###.hipnc (e.g. hero_shot_v001.hipnc)")
        return

    
    dirname, filename = os.path.split(current_path)

   
    pattern = r'^(?P<base>.+)_v(?P<ver>\d+)\.(?P<ext>hip|hipnc|hiplc)$'
    m = re.match(pattern, filename, re.IGNORECASE)
    if not m:
       
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

   
    if os.path.exists(new_path):
        choice = hou.ui.displayMessage(
            "Target file already exists:\n\n{}\n\nOverwrite?".format(new_path),
            buttons=("Overwrite", "Cancel"),
            severity=hou.severityType.Warning
        )
        if choice != 0:
       
            hou.ui.displayMessage("Operation cancelled. No file written.")
            return

   
    try:
        hou.hipFile.save(new_path)
    except Exception as e:
        hou.ui.displayMessage("Failed to save new HIP:\n\n{}".format(str(e)))
        return

    hou.ui.displayMessage("Saved new version:\n\n{}".format(new_path))


version_up_current_hip()
