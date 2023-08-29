
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip
import time
import os
import shutil

# Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files\\chrome-win64\\chrome.exe"
user_data_path = r"C:\Users\ryanc\AppData\Local\Google\Chrome for Testing\User Data"
chrome_options.add_argument(f"user-data-dir={user_data_path}")

# Initialize the WebDriver for Chrome
driver = webdriver.Chrome(options=chrome_options)

# Open the website
url = "https://app.runwayml.com/video-tools/teams/ryanclark173/ai-tools/gen-2"
driver.get(url)
time.sleep(1)

def move_to_directory():
    # Source and destination directories
    source_dir = r"C:\Users\ryanc\Downloads"
    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\RunwayClips"

    # Find files ending with (Original).mp4 in the source directory
    original_files = [f for f in os.listdir(source_dir) if f.__contains__('.mp4')]

    if not original_files:
        print("No files found with '.mp4' suffix in the source directory.")
        return False

    # Check how many RWML_vid(x) files are in the destination directory
    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('RWML_vid')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('RWML_vid')[1].split('.mp4')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    for f in original_files:
        max_num += 1
        new_name = f"RWML_vid{max_num}.mp4"
        shutil.move(os.path.join(source_dir, f), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {f} to {new_name}")
        return True


def main(image_path,prompt):
    try:
        screen_width, screen_height = pyautogui.size()

        # Calculate the center of the screen
        center_x = screen_width / 2
        center_y = screen_height / 2
        # find the upload button
        link_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='upload a file']")))

        # Click the <a> tag
        link_element.click()

        time.sleep(2)

        pyperclip.copy(image_path)
        # Simulate a Ctrl+V action to paste the copied content
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(7)

        # find the text button
        div_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Select text prompt mode']")))

        # Click the <div> tag
        div_element.click()
        time.sleep(2)
        pyperclip.copy(prompt)
        pyautogui.click(center_x, center_y+40)
        time.sleep(1)
        # Simulate a Ctrl+V action to paste the copied content
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(4)


        # Find the generate button
        button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Generate']")))

        # Click the <button> tag
        button_element.click()

        time.sleep(150)



        # Click in the center of the screen
        pyautogui.click(center_x, center_y)
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(0.2)  # Small delay between key presses
        pyautogui.press('enter')
        time.sleep(30)

        move_to_directory()

        driver.quit()
        return True

    except:
        driver.quit()


imgPath = 'C:\\Users\\ryanc\\OneDrive\\Documents\\YTE\\geek6.jpg'
prompt = 'smart man'
main(imgPath,prompt)