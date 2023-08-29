from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import shutil
import random

source_dir = "C:\\Users\\ryanc\\Downloads"  
dest_dir = "C:\\Users\\ryanc\\OneDrive\\Documents\\YTE\\AudioClips"

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

def search_with_query(driver, query):
    # Initialize the WebDriver (make sure you have the appropriate driver executable in your PATH)


    try:
        # Open a website
        driver.get(f"https://soundbible.com/search.php?q={query}")  # Replace with the URL you want to search on

                # Find all h3 elements on the page
        h3_elements = driver.find_elements(By.TAG_NAME, "h3")

        links = []

        # Iterate through each h3 element and find the <a> tags within it
        for h3_element in h3_elements:
            a_tags = h3_element.find_elements(By.TAG_NAME, "a")
            for a_tag in a_tags:
                link = a_tag.get_attribute("href")
                if link:
                    links.append(link)
        chosenLink = random.randint(0,len(links))
        driver.get(links[chosenLink]) 
        time.sleep(3)

        img_element = driver.find_element(By.XPATH, '//img[@src="img/mp3-100px.png"]')

        # Get the href attribute of the parent element
        parent_element = img_element.find_element(By.XPATH, './..')  # Select the parent element
        parent_href = parent_element.get_attribute("href")

        # Redirect the browser to the URL
        if parent_href:
            driver.get(parent_href)
                
        time.sleep(10)

    finally:
        # Close the browser window
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
    

def main(query):
    Cdriver = initialize_driver()
    search_with_query(Cdriver, query)
    move_and_rename_supplementary_audios(source_dir, dest_dir)
    return True