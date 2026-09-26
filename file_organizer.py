import os
import shutil

# Put the path of the messy folder you want to clean up here
# (For testing, create a dummy folder with a few random files first!)
# Use a generic path or input for your target directory
target_dir = r"C:\path\to\your\folder"

os.chdir(target_dir)

for file in os.listdir():
    if os.path.isdir(file):
        continue

    # Get file extension
    ext = file.split(".")[-1].lower()

    # Create folders based on extensions
    if ext in ["jpg", "jpeg", "png", "gif"]:
        folder = "Images"
    elif ext in ["pdf", "docx", "txt", "xlsx"]:
        folder = "Documents"
    elif ext in ["py", "html", "css", "js"]:
        folder = "Code"
    else:
        folder = "Others"

    # Create folder if it doesn't exit and move file
    if not os.path.exists(folder):
        os.makedirs(folder)
    shutil.move(file, os.path.join(folder, file))

print("Files organized successfully!")    

