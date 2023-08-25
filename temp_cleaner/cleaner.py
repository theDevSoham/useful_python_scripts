import os
import shutil
import ctypes

# Check if the script is run with administrative privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def clean_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

def main():
    if not is_admin():
        print("This script requires administrative privileges to delete files.")
        return

    temp_directory = os.environ.get("TEMP")
    temp_directory_alt = "C:\\Windows\\Temp"  # Additional common temp directory
    prefetch_directory = "C:\\Windows\\Prefetch"

    directories_to_clean = [temp_directory, temp_directory_alt, prefetch_directory]

    for directory in directories_to_clean:
        if os.path.exists(directory):
            print(f"Cleaning {directory}...")
            clean_directory(directory)
            print(f"Finished cleaning {directory}\n")
        else:
            print(f"{directory} does not exist\n")

if __name__ == "__main__":
    main()
