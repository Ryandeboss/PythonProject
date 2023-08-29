API_KEY = ''
USER_ID = ''

import requests
import argparse
import shutil
import os

API_ENDPOINT = "https://clipdrop-api.co/text-to-image/v1"

def move_to_directory():
    # Source and destination directories
    source_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE"
    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\ClickdropImgs"

    # Find files ending with (Original).mp4 in the source directory
    original_files = [f for f in os.listdir(source_dir) if f.__contains__('.png')]

    if not original_files:
        print("No files found with '.png' suffix in the source directory.")
        return False

    # Check how many liapix_vid(x) files are in the destination directory
    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('clickDrop_img')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('clickDrop_img')[1].split('.png')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    for f in original_files:
        max_num += 1
        new_name = f"clickDrop_img{max_num}.png"
        shutil.move(os.path.join(source_dir, f), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {f} to {new_name}")
        return True

def main(prompt):
    # Ensure the prompt length is less than or equal to 1000 characters
    if len(prompt) > 1000:
        print("Error: Prompt text length exceeds 1000 characters.")
        return

    # Prepare the multipart/form-data request
    files = {
        'prompt': (None, prompt)
    }
    header = { 'x-api-key': API_KEY}
    response = requests.post(API_ENDPOINT, files=files, headers=header)
    
    # If response contains an image
    if response.headers['content-type'] == 'image/png':
        with open('output.png', 'wb') as file:
            file.write(response.content)
    else:
        print("Error:", response.text)
    
    move_to_directory()

    return True

if __name__ == "__main__":

    Theprompt = 'Superman'
    main(Theprompt)