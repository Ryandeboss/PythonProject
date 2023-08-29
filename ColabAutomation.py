from selenium import webdriver
import pyautogui
import pyperclip        
import time

# Create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files\\chrome-win64\\chrome.exe"
user_data_path = r"C:\Users\ryanc\AppData\Local\Google\Chrome for Testing\User Data"
chrome_options.add_argument(f"user-data-dir={user_data_path}")

# Initialize the WebDriver for Chrome
driver = webdriver.Chrome(options=chrome_options)




        # for cell_id in cell_ids:
        #     # Use JavaScript to change the URL fragment
        #     driver.execute_script(f"window.location.hash = 'scrollTo={cell_id}';")
        #     time.sleep(3)
        #     screen_width, screen_height = pyautogui.size()

        #     # Calculate the center coordinates
        #     center_x, center_y = screen_width / 2, ((screen_height / 2)-80)

        #     # Click in the middle of the screen
        #     pyautogui.click(center_x, center_y)  
        #     for _ in range(4):
        #         pyautogui.press('tab')
        #         time.sleep(0.5)  # Small delay between key presses

        #     time.sleep(3)

def first_cell(cell_ids, center_x, center_y):
    driver.execute_script(f"window.location.hash = 'scrollTo={cell_ids[0]}';")
    time.sleep(2)
    # Click in the middle of the screen
    pyautogui.click(center_x, (center_y-60))             
  
    # Use pyautogui to simulate pressing Shift + Enter
    pyautogui.hotkey('shift', 'enter')
    pyautogui.press('enter')
    time.sleep(1)

    for _ in range(3):
        pyautogui.press('tab')
        time.sleep(0.5)  # Small delay between key presses
    pyautogui.press('enter')

    time.sleep(30)

def second_cell(cell_ids, center_x, center_y):
    driver.execute_script(f"window.location.hash = 'scrollTo={cell_ids[1]}';")
    time.sleep(2)
    # Click in the middle of the screen
    pyautogui.click(center_x, center_y)             

    pyautogui.hotkey('shift', 'enter')
    pyautogui.press('enter')
  
    # Use pyautogui to simulate pressing Shift + Enter
    time.sleep(30)
    for _ in range(5):
        pyautogui.press('tab')
        time.sleep(0.5)  # Small delay between key presses
    pyautogui.press('enter')

    time.sleep(2)  # wait for a couple of seconds before typing
    pyperclip.copy("C:\\Users\\ryanc\\OneDrive\\Documents\\YTE\\TestVid.mp4")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(70)

def third_cell(cell_ids, center_x, center_y):
    driver.execute_script(f"window.location.hash = 'scrollTo={cell_ids[2]}';")
    time.sleep(2)        

    pyautogui.hotkey('shift', 'enter')
    pyautogui.press('enter')
  
    # Use pyautogui to simulate pressing Shift + Enter
    time.sleep(30)
    for _ in range(6):
        pyautogui.press('tab')
        time.sleep(0.5)  # Small delay between key presses
    pyautogui.press('enter')

    time.sleep(2)  # wait for a couple of seconds before typing
    pyperclip.copy("C:\\Users\\ryanc\\OneDrive\\Documents\\YTE\\temp_audio.wav")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(40)

def forth_cell(cell_ids):
    driver.execute_script(f"window.location.hash = 'scrollTo={cell_ids[3]}';")
    time.sleep(2)
    # Click in the middle of the screen
    # pyautogui.click(center_x, center_y)             

    pyautogui.hotkey('shift', 'enter')
    pyautogui.press('enter')
    time.sleep(50)

def download():
    # Setup for mouse clicks:
    screen_width, screen_height = pyautogui.size()
    # Calculate the x and y coordinates
    x = 20
    y = screen_height // 2
    # Move the mouse to the specified coordinates

    #### Finding Terminal Widget

    # Move the mouse to the specified coordinates
    pyautogui.moveTo(x, y)
    # Click at the current mouse position
    pyautogui.click()
    for _ in range(7):
        pyautogui.press('tab')
        time.sleep(0.2)  # Small delay between key presses
    pyautogui.press('enter')
    
    time.sleep(20)
    for _ in range(10):
        pyautogui.press('backspace')
        time.sleep(0.1)  # Optional: Introduce a small delay between key presses
    pyautogui.write('cd /content/Wav2Lip/results/')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('mv result_voice.mp4 /content/drive/My\ Drive/LipSyncVideo/')
    pyautogui.press('enter')
    time.sleep(50)

def main():
    cell_ids = ['Qgo-oaI3JU2u', 'nDuM7tfZ1F0t', 'XgF4794r7sWK', 'ZgtO08V28ANf']
    try:
        # Navigate to the website
        driver.get("https://colab.research.google.com/github/justinjohn0306/Wav2Lip/blob/master/Wav2Lip_simplified_v5.ipynb#")
        screen_width, screen_height = pyautogui.size()
        # Calculate the center coordinates
        center_x, center_y = screen_width / 2, ((screen_height / 2)-50)


        first_cell(cell_ids, center_x, center_y)
        second_cell(cell_ids, center_x, center_y)
        third_cell(cell_ids, center_x, center_y)
        forth_cell(cell_ids)
        download()
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'm', 'i')
        time.sleep(10)
    finally:
        driver.quit()

videoPath = "C:\\Users\\ryanc\\OneDrive\\Documents\\YTE\\TestVid.mp4"

audioPath = "C:\\Users\\ryanc\\OneDrive\\Documents\\YTE\\temp_audio.wav"

main(videoPath, audioPath)
