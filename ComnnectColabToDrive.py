from selenium import webdriver
import pyautogui
import pyperclip        
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files\\chrome-win64\\chrome.exe"
user_data_path = r"C:\Users\ryanc\AppData\Local\Google\Chrome for Testing\User Data"
chrome_options.add_argument(f"user-data-dir={user_data_path}")

# Initialize the WebDriver for Chrome
driver = webdriver.Chrome(options=chrome_options)

cell_ids = ['Qgo-oaI3JU2u', 'nDuM7tfZ1F0t', 'XgF4794r7sWK', 'ZgtO08V28ANf']

def checkIfFileMade():
    gauth = GoogleAuth()
    
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("saved_credentials.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()

    # Save the current credentials to a file
    gauth.SaveCredentialsFile("saved_credentials.txt")

    drive = GoogleDrive(gauth)
    folder_list = drive.ListFile({'q': f"title='Test' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
    if not folder_list:
        print("Folder not found.")
    else:
        folder = folder_list[0]
        file_list = drive.ListFile({'q': f"'{folder['id']}' in parents and trashed=false"}).GetList()
        
        # Check if the folder is not empty
        if file_list:
            print(f"Folder '{folder['title']}' is not empty. Deleting contents...")
            
            # Delete everything inside the folder
            for file in file_list:
                print(f"Deleting {file['title']}...")
                file.Delete()
            print(f"All contents of '{folder['title']}' have been deleted.")
            return True
        else:
            print(f"Folder '{folder['title']}' is empty and will attempt to connect to google drive")
            return False

def main(cell_ids = ['Qgo-oaI3JU2u', 'nDuM7tfZ1F0t', 'XgF4794r7sWK', 'ZgtO08V28ANf']):
    try:
        # Navigate to the website
        driver.get("https://colab.research.google.com/github/justinjohn0306/Wav2Lip/blob/master/Wav2Lip_simplified_v5.ipynb#")
        driver.execute_script(f"window.location.hash = 'scrollTo={cell_ids[3]}';")
        screen_width, screen_height = pyautogui.size()
        # Calculate the center coordinates
        center_x, center_y = screen_width / 2, ((screen_height / 2)-50)     
        pyautogui.click(20, (center_y+60))   
        for _ in range(7):
            pyautogui.press('tab')
            time.sleep(0.2)  # Small delay between key presses
        pyautogui.press('enter')
        for _ in range(20):
            pyautogui.press('backspace')
            time.sleep(0.1)  # Optional: Introduce a small delay between key presses
        time.sleep(3)
        pyautogui.write('cd /content/sample_data/')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.write('mv anscombe.json /content/drive/My\ Drive/Test/')
        pyautogui.press('enter')
        time.sleep(15)
        result = checkIfFileMade()
        if result == True:
            driver.quit()

        if result == False:
            pyautogui.click(center_x, (center_y+60))  
            pyautogui.hotkey('ctrl', 'm', 'b')
            time.sleep(2)
            pyperclip.copy("from google.colab import drive")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyperclip.copy("drive.mount('/content/drive', force_remount=True)")
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('shift', 'enter')

            for _ in range(4):
                pyautogui.press('tab')
                time.sleep(0.5)  # Small delay between key presses
            pyautogui.press('enter')
            time.sleep(10)
            pyautogui.click(center_x, (center_y))  

            for _ in range(2):
                pyautogui.press('tab')
                time.sleep(0.2)  # Small delay between key presses
            pyautogui.press('enter')

            time.sleep(5)

            for _ in range(2):
                pyautogui.press('tab')
                time.sleep(0.2)  # Small delay between key presses
            pyautogui.press('enter')
            time.sleep(5)
            for _ in range(14):
                pyautogui.press('tab')
                time.sleep(0.2)  # Small delay between key presses
            pyautogui.press('enter')

            time.sleep(5)
            pyautogui.hotkey('ctrl', 'm', 'i')
            time.sleep(10)


    finally:
        driver.quit()

main(cell_ids)