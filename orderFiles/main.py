import os
import shutil

# path for files to be ordered

path = "YOUR_PATH"

# Create destination folders files if not exists

types = ["docs", "images", "cheatsheets"]

for folder in types:
    folder_path = os.path.join(path, folder)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files

for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(os.path.join(path, file), os.path.join(path, "images", file))
    elif file.endswith(".pdf"):
        shutil.move(os.path.join(path, file), os.path.join(path, "cheatsheets", file))
    else:
        shutil.move(os.path.join(path, file), os.path.join(path, "docs", file))