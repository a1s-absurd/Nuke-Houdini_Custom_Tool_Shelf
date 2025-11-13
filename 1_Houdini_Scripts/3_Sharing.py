import hou, os, shutil


proj_dir = hou.expandString("$HIP")
proj_name = os.path.basename(proj_dir)


target_root = hou.ui.selectFile(
    start=hou.expandString("$HOME"),
    title="Select OneDrive or Shared Drive Folder",
    file_type=hou.fileType.Directory
)

if not target_root:
    hou.ui.displayMessage("No destination selected. Cancelled.")
else:
    target_root = os.path.dirname(target_root)
    dest_path = os.path.join(target_root, proj_name + "_shared")

    include_cache = hou.ui.displayMessage(
        "Include cache files in publish?",
        buttons=("Yes", "No"),
        default_choice=1
    )


    skip_dirs = ["cache", "sim", "geo", "temp"] if include_cache == 1 else []

    def ignore_cache(dir, files):
        ignored = []
        for d in files:
            if d in skip_dirs:
                ignored.append(d)
        return ignored

 
    try:
        shutil.copytree(proj_dir, dest_path, ignore=ignore_cache if include_cache == 1 else None)
        hou.ui.displayMessage(f"Project published to:\n{dest_path}")
    except Exception as e:
        hou.ui.displayMessage(f"Error copying project:\n{str(e)}")
