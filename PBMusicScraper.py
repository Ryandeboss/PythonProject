from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import shutil

download_dir = r"C:\Users\ryanc\Downloads"
source_dir = r"C:\Users\ryanc\Downloads"  
dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\MusicClips"

def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Program Files\\chrome-win64\\chrome.exe"
    user_data_path = r"C:\Users\ryanc\AppData\Local\Google\Chrome for Testing\User Data"
    chrome_options.add_argument(f"user-data-dir={user_data_path}")
    download_dir = r"C:\Users\ryanc\Downloads"
    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def replace_spaces_with_percent20(input_string):
    output_string = input_string.replace(" ", "%20")
    return output_string

def wait_for_new_mp3_file(folder_path, initial_state, wait_duration=5):
    while True:
        current_state = set(os.listdir(folder_path))
        new_files = current_state - initial_state
        
        # Filter out files with .crdownload extension and only consider .mp3 files
        new_mp3_files = [file for file in new_files if file.lower().endswith('.mp3')]

        if new_mp3_files:
            # Wait for the new .mp3 file to be present for the specified duration
            time.sleep(wait_duration)
            if all(file in current_state for file in new_mp3_files):
                return True
        
        time.sleep(1)  # Wait for 1 second before checking again

def search_pixapay(driver, query):
    try:
        folder_path = r"C:\Users\ryanc\Downloads"  
        initial_state = set(os.listdir(folder_path))

        prepedQuery = replace_spaces_with_percent20(query)
        driver.get('https://pixabay.com/music/search/'+prepedQuery)
        time.sleep(3)
        download_buttons = driver.find_elements(By.XPATH, '//button[@aria-label="Download"]')

        if download_buttons:
            # Click the first download button
            first_download_button = download_buttons[0]
            first_download_button.click()
            
        new_file_added = wait_for_new_mp3_file(folder_path, initial_state)
        if new_file_added:
            driver.quit()
    except:
        driver.quit()

def move_and_rename_supplementary_audios(source_dir, dest_dir):
    try:
        files = os.listdir(source_dir)

        # Filter files to include only mp3 files
        mp3_files = [file for file in files if file.lower().endswith('.mp3')]

        # Get the newest mp3 file
        newest_mp3 = max(mp3_files, key=lambda f: os.path.getctime(os.path.join(source_dir, f)))

        existing_files = [f for f in os.listdir(dest_dir) if f.startswith('supplementary_audio')]
        if existing_files:
            existing_numbers = [int(f.split('supplementary_audio')[1].split('.mp3')[0]) for f in existing_files]
            max_num = max(existing_numbers)
        else:
            max_num = 0

        # Move and rename files
        max_num += 1
        new_name = f"supplementary_audio{max_num}.mp3"
        shutil.move(os.path.join(source_dir, newest_mp3), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {newest_mp3} to {new_name}")

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False



def main():
    driver = initialize_driver()
    search_pixapay(driver, 'serious piano sad')
    move_and_rename_supplementary_audios(source_dir, dest_dir)
    return True
