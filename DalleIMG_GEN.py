# DalleIMG_GEN.py

import requests
import json
import os
import shutil

API_ENDPOINT = "https://api.openai.com/v1/images/generations"
HEADERS = {
    "Authorization": "",
    "Content-Type": "application/json"
}


def move_to_directory():
    # Source and destination directories
    source_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE"
    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\OtherImgs"

    # Find files ending with (Original).mp4 in the source directory
    original_files = [f for f in os.listdir(source_dir) if f.__contains__('.png')]

    if not original_files:
        print("No files found with '.png' suffix in the source directory.")
        return False

    # Check how many liapix_vid(x) files are in the destination directory
    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('Dalle_img')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('Dalle_img')[1].split('.png')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    for f in original_files:
        max_num += 1
        new_name = f"Dalle_img{max_num}.png"
        shutil.move(os.path.join(source_dir, f), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {f} to {new_name}")
        return True

def download_image(url, output_filename):
    response = requests.get(url)
    with open(output_filename, 'wb') as file:
        file.write(response.content)

def main(prompt):
    payload = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload))
    response_json = response.json()

    if 'data' in response_json:
        for idx, image_data in enumerate(response_json['data']):
            image_url = image_data['url']
            download_image(image_url, f"output_{idx}.png")
    else:
        print("Error:", response_json)

    move_to_directory()
    return True

if __name__ == "__main__":
    thePrompt = 'Super man'

    main(thePrompt)
