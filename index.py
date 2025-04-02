import os
import shutil

source_folder = r"C:\Users\path\"

extension_map = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx"],
    "Software": [".exe", ".msi", ".jar"],
    "Archives": [".zip", ".rar", ".7z"],
    "Web": [".html", ".php"],
    "Databases": [".sql"],
    "Videos": [".mp4"],
    "3D Models": [".fbx", ".blend"],
    "Spreadsheets": [".xls", ".xlsx"],
}

for folder in extension_map.keys():
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    
    if os.path.isfile(file_path):
        for folder, extensions in extension_map.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                destination_folder = os.path.join(source_folder, folder)
                shutil.move(file_path, destination_folder)
                print(f"Moved: {file} -> {destination_folder}")
                break
