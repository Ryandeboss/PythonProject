from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyautogui
import pyperclip
import time
import os
import shutil
import random
download_dir = r"C:\Users\ryanc\Downloads"

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

def search_pixabay(driver, query):
    # Click on the search input to activate it
    search_activator = driver.find_element(By.NAME, "search")
    search_activator.click()
    
    # Give it a brief moment to ensure the input is activated
    time.sleep(1)
    
    # Use pyautogui to shift focus from address bar to the webpage
    for _ in range(12):  # Press 'Tab' 3 times, adjust as needed
        pyautogui.press('tab')
        time.sleep(0.5)  # Wait a bit between key presses
    
    # Use pyautogui to type the query
    pyperclip.copy(query)  # Copy the query to clipboard
    pyautogui.hotkey('ctrl', 'v')  # Paste the query
    pyautogui.press('enter')  # Press Enter to submit

    # wait for results to load
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')



def click_video_pixabay(driver,timeout=10):
    
    class_name = "cell--B7yKd"
    try:
        # Wait until the first div with the desired class is present
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        element = driver.find_elements(By.CLASS_NAME, class_name)
        randomNum = random.randint(0,(len(element)-1))
        element[randomNum].click()
        return random.randint(0,(len(element)-1))
    except TimeoutException:
        print(f"No <div> elements found with class: {class_name} within {timeout} seconds.")
        return "no results"

# def IfPopUp():
#     time.sleep(10)
#     screen_width, screen_height = pyautogui.size()
#     # Calculate the x and y coordinates
#     x = screen_width // 2
#     y = screen_height // 2
#     pyautogui.moveTo(x, y)
#     pyautogui.click()
#     for _ in range(5):
#         pyautogui.press('tab')
#         time.sleep(0.2)  # Small delay between key presses
#     pyautogui.press('enter')
#     time.sleep(1)
#     for _ in range (2):
#         pyautogui.press('up')
#         time.sleep(0.1)
#     time.sleep(60)

def download_video_pixabay(driver,download_dir):
    # wait for video page to load
    download_button_xpath = "//button[.//span[text()='Download']]"
    download_button = driver.find_element(By.XPATH, download_button_xpath)
    download_button.click()
    time.sleep(3)

    xpath_pattern = "//input[contains(@value, 'medium.mp4')]/following-sibling::span[1]"

    # Find the <span> element
    xpath_pattern = "//span[@class='radioIcon--M5u5S']"

    # Find all matching <span> elements
    span_elements = driver.find_elements(By.XPATH, xpath_pattern)

    # Check if there are at least four elements and click on the fourth one
    if len(span_elements) >= 0:
        span_elements[int(len(span_elements)-1)].click()  # List indexing starts at 0, so the fourth element is at index 3
    else:
        print("Less than four matching <span> elements found.")
    time.sleep(3)

    download_link_xpath = "//a[.//span[contains(text(), 'Download')]]"
    initial_link = driver.find_element(By.XPATH, download_link_xpath)
    initial_link.click()
    initial_url = driver.current_url
    for i in range(25):
        time.sleep(1)
        if driver.current_url != initial_url:
            return False



def move_to_directory():
    # Source and destination directories
    source_dir = r"C:\Users\ryanc\Downloads"
    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\VidClips"

    # Find files ending with (Original).mp4 in the source directory
    original_files = [f for f in os.listdir(source_dir) if f.__contains__('(Original)')]

    if not original_files:
        print("No files found with '(Original).mp4' suffix in the source directory.")
        return False

    # Check how many supplementary_vid(x) files are in the destination directory
    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('supplementary_vid')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('supplementary_vid')[1].split('.mp4')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    for f in original_files:
        max_num += 1
        new_name = f"supplementary_vid{max_num}.mp4"
        shutil.move(os.path.join(source_dir, f), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {f} to {new_name}")
        return True
def main(query):
    attempts = 0
    driver = initialize_driver()
    url = 'https://pixabay.com/videos/'
    driver.get(url)
    search_pixabay(driver, query)
    res = click_video_pixabay(driver)
    if res == 'no results':
        return False
    elif res == False:
        if attempts >= 10:
            return False
        randomNum = random.randint(0,10)
        attempts += attempts
    download_video_pixabay(driver, download_dir)
    driver.quit()
    move_to_directory()
    return True

main('angry man')