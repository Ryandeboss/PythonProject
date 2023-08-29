from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pyperclip
import time
import shutil
import os
# Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files\\chrome-win64\\chrome.exe"
user_data_path = r"C:\Users\ryanc\AppData\Local\Google\Chrome for Testing\User Data"
chrome_options.add_argument(f"user-data-dir={user_data_path}")


def move_to_directory():
    # Source and destination directories
    source_dir = r"C:\Users\ryanc\Downloads"
    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\Liapix"

    # Find files ending with (Original).mp4 in the source directory
    original_files = [f for f in os.listdir(source_dir) if f.__contains__('.mp4')]

    if not original_files:
        print("No files found with '.mp4' suffix in the source directory.")
        return False

    # Check how many liapix_vid(x) files are in the destination directory
    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('liapix_vid')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('liapix_vid')[1].split('.mp4')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    for f in original_files:
        max_num += 1
        new_name = f"liapix_vid{max_num}.mp4"
        shutil.move(os.path.join(source_dir, f), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {f} to {new_name}")
        return True


def main(image_path):
    # Initialize the WebDriver for Chrome
    driver = webdriver.Chrome(options=chrome_options)

    url = "https://convert.leiapix.com"
    driver.get(url)
    time.sleep(3)
    upload_icon_img = driver.find_element(By.XPATH, '//img[@alt="upload icon"]')
    # Click on the <img> tag
    upload_icon_img.click()
    time.sleep(1)

    pyperclip.copy(image_path)
    # Simulate a Ctrl+V action to paste the copied content
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    time.sleep(30)

    share_icon_button = driver.find_element(By.XPATH, '//img[@alt="share icon"]')
    share_icon_button.click()

    # Wait for 15 seconds
    time.sleep(30)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-click*=\"$parent.$parent.$parent.transitionModal('mp4'); $root.sendGAEvent({object: 'Social', action: 'Save as MP4'})\"]"))
    )

    # Click the element to invoke the functions
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[ng-click*=\"exportFile(); $root.sendGAEvent({object: 'Export', action: 'Save'})\"]"))
    )

    # Click the div element to invoke the functions
    element.click()

    time.sleep(30)
    move_to_directory()
    time.sleep(10)

    


    driver.quit()
    return True

main(r'C:\Users\ryanc\OneDrive\Documents\YTE\geek6.jpg')