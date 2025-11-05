import os
import shutil
from tkinter import Tk, filedialog

# create window

window = Tk()
window.withdraw()

# path for files to be ordered


path = filedialog.askdirectory(title="Select the folder to order")

# Create destination folders files if not exists

extensions = {
    ".jpg": "images",
    ".pdf": "cheatsheets",
    "*": "docs"
}

for folder in set(extensions.values()):
    folder_path = os.path.join(path, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in extensions:
            destino = os.path.join(path, extensions[ext], file)
            shutil.move(file_path, destino)
