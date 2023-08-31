import os
import sys
import shutil
from PIL import Image
import imagehash

# Function to compute the hash of an image
def compute_hash(image_path):
    image = Image.open(image_path)
    return imagehash.average_hash(image)

def remove_duplicates(image_directory):
    # Dictionary to store hashes and corresponding file paths
    hashes = {}

    # List to store duplicate image paths
    duplicates = []

    # Iterate through the images in the directory
    for filename in os.listdir(image_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_directory, filename)
            image_hash = compute_hash(image_path)
            
            # Check if hash already exists (duplicate)
            if image_hash in hashes:
                duplicates.append(image_path)
            else:
                hashes[image_hash] = image_path

    # Remove duplicate images
    for duplicate_path in duplicates:
        os.remove(duplicate_path)
        print(f"Removed duplicate: {duplicate_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <image_directory_path>")
    else:
        image_directory = sys.argv[1]
        if not os.path.exists(image_directory):
            print("Invalid directory path.")
        else:
            remove_duplicates(image_directory)
