import os
import shutil

# Step 1: Store the extensions to check in a list
extensions_to_check = ['png', 'svg', 'jpg']

# Step 2: Create directories for each extension
script_dir = os.path.dirname(os.path.abspath(__file__))
for extension in extensions_to_check:
    directory_path = os.path.join(script_dir, extension)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Step 3: Check each file and move them to respective directories
for filename in os.listdir(script_dir):
    if os.path.isfile(filename):
        file_extension = filename.split('.')[-1]
        if file_extension in extensions_to_check:
            source_path = os.path.join(script_dir, filename)
            destination_path = os.path.join(script_dir, file_extension, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {file_extension} directory.")
