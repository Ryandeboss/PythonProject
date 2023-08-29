# Direct Kaiber prompts should be organized in this way: 
# Subject, prepositional details, setting, meta modifiers, and styling:
    # Subject: main focus of vid
    # Prep details: Details of subject or minor elements in vid
    # Setting: Background and lighting
    # meta modifiers: 



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
url = "https://kaiber.ai/create"
driver.get(url)

# Print the first 1000 characters of the page source for debugging
# print(driver.page_source[:1000])

def set_video_length(driver, desired_length):
    # Find the current video length element
    # Replace this XPath with the appropriate one for your page


    # Calculate the difference between desired and current length
    difference = desired_length - 8

    # Depending on the difference, click the + or - button the required number of times
    if difference > 0:  # Need to increase video length
        plus_button = driver.find_element(By.XPATH, "//button[text()='+']")
        for _ in range(difference):
            plus_button.click()
    elif difference < 0:  # Need to decrease video length
        minus_button = driver.find_element(By.XPATH, "//button[text()='-']")
        for _ in range(-difference):
            minus_button.click()

valid_movements = [
    "None",
    "Zoom In",
    "Zoom Out",
    "Rotate Clockwise",
    "Rotate Counter-Clockwise",
    "Up",
    "Down",
    "Left",
    "Right"
]

def camera_movement(driver, movement):
    """
    Adjust the camera movement based on the provided option.
    
    Parameters:
    - driver: The active Selenium WebDriver instance.
    - movement: A string representing the desired camera movement.
    """
    # Check if the movement option is valid
    if movement not in valid_movements:
        raise ValueError(f"Invalid camera movement option: {movement}")
    
    # Find the button with the desired movement and click it
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[.//span[text()='{movement}']]"))
        )
        button.click()

        # location = button.location
        # size = button.size

        # # Calculate the center of the element
        # center_x = location['x'] + (size['width'] / 2)
        # center_y = location['y'] + (size['height'] / 2)

        # # Adjust for the browser chrome and window position
        # # (This step may require some manual adjustment depending on your browser and setup)
        # chrome_adjustment_x = 10  # Example value, adjust as needed
        # chrome_adjustment_y = 80  # Example value, adjust as needed

        # absolute_x = center_x + chrome_adjustment_x
        # absolute_y = center_y + chrome_adjustment_y

        # # Use pyautogui to move to the element's location
        # pyautogui.moveTo(absolute_x, absolute_y)
        # pyautogui.click()

    except Exception as e:
        print(f"An error occurred while trying to adjust camera movement: {e}")



def move_to_directory(prompt):
    # Source and destination directories
    source_dir = r"C:\Users\ryanc\Downloads"
    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\KaiberClips"

    # Find files in the source directory that contain the prompt
    original_files = [f for f in os.listdir(source_dir) if prompt in f]

    if not original_files:
        print("No files found with the prompt in the source directory.")
        return False

    # Check how many supplementary_vid(x) files are in the destination directory
    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('kaiber_vid')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('kaiber_vid')[1].split('.mp4')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    for f in original_files:
        max_num += 1
        new_name = f"kaiber_vid{max_num}.mp4"
        shutil.move(os.path.join(source_dir, f), os.path.join(dest_dir, new_name))
        print(f"Moved and renamed {f} to {new_name}")

    return True


    
image_path = "C:\\Users\\ryanc\\OneDrive\\Pictures\\Saved Pictures\\geek6.jpg"

prompt = 'Super Man'

def main(image_path,prompt):
    try:
        # Click the button to open the dialog box
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//p[text()='Begin with an initial image']]"))
        )
        button.click()
        print("Clicked the initial button.")

        print("Clicked the 'show all files...' button.")

        time.sleep(2)  # wait for a couple of seconds before typing
        pyperclip.copy(image_path)
        # Simulate a Ctrl+V action to paste the copied content
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Continue to prompt.']]"))
        )
        button.click()
        time.sleep(3)
        span_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '(describe subject)')]"))
        )
        span_element.click()

        # Assuming clicking the span brings focus to an input field, we'll send "A chicken" to it
        # If there's a different behavior, you might need to adjust the following code
        active_element = driver.switch_to.active_element
        active_element.send_keys(prompt)

        span_element = WebDriverWait(driver, 10).until(  # Choose style 
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Photo-realistic']"))
        )
        span_element.click()

        button = WebDriverWait(driver, 10).until(   # Proceed to the video settings page
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Video settings')]"))
        )
    
        time.sleep(2)
    # Do something with the button, e.g., click it
        button.click()
        print('Clicked Video Settings')
        try:
            set_video_length(driver, 3)  # Set video length to 10s
            print('Set Videos Length')
        except: pass

        try:
            camera_movement(driver, "Zoom In") # Choose camera movment
            print('Set Camera movment')
        except: pass
        time.sleep(2)
        try:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Generate previews')]"))
            )
            
            # # Scroll the button into view (optional but can help if the button is off-screen)
            driver.execute_script("arguments[0].scrollIntoView();", button)

            
            # Click the button
            button.click()
        except: 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print('needed to use autogui for Generate previews')
            pyautogui.moveTo(1200, 890)
            time.sleep(3)

            # Click at the current mouse position
            pyautogui.click()
            print('Clicked Generate previews')

        time.sleep(5)

        wait = WebDriverWait(driver, 1)  # Using a shorter wait for each iteration
        timeout = 60  # Maximum time (seconds) you want to wait for the img tags to appear
        end_time = time.time() + timeout

        while time.time() < end_time:
            try:
                # Check for the presence of img tags
                img_element = wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@alt, 'preview-')]")))
                # If found, click the first one and break out of the loop
                img_element.click()
                print("Clicked the first image!")
                
                break
            except:
                # If not found, loop will continue checking until the timeout
                continue
        else:
            print("Timeout reached without finding any img tags.")
        
        time.sleep(5)
        # img_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='/button_create.png']")))

        # driver.execute_script("arguments[0].scrollIntoView();", img_element)
        # time.sleep(.5)
        # # Click the element
        # img_element.click()
        for _ in range(7):
            pyautogui.press('tab')
            time.sleep(0.2)  # Small delay between key presses
        time.sleep(.5)
        pyautogui.press('enter')
        print("Clicked the image with src='/button_create.png'!")
        time.sleep(160)

        screen_width, screen_height = pyautogui.size()

        # Calculate the center of the screen
        center_x = screen_width / 2
        center_y = screen_height / 2
        pyautogui.click((center_x-50), center_y)

        for _ in range(5):
            pyautogui.press('tab')
            time.sleep(0.2)  # Small delay between key presses

        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(10)
        move_to_directory(prompt)
        time.sleep(10)
        return True

    except Exception as e:
        print(f"Error during execution: {e.message}")
        return False

    finally:
        driver.quit()  

    
if __name__ == "__main__":
    main(image_path,prompt)
    move_to_directory(prompt)
 








