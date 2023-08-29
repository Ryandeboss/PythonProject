import os
import shutil
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def main(folder_id = '', local_save_path = r"C:\Users\ryanc\OneDrive\Documents\YTE\LipSyncClips"):
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
    
    # List all files in the specified Google Drive folder
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    
    # Ensure the local directory exists
    if not os.path.exists(local_save_path):
        os.makedirs(local_save_path)
    
    # Download files to the specified local directory and delete from Drive
    for file in file_list:
        print(f"Downloading {file['title']}...")
        file.GetContentFile(os.path.join(local_save_path, file['title']))
        print(f"Downloaded {file['title']} to {local_save_path}. Now deleting from Drive...")
        file.Delete()
        print(f"Deleted {file['title']} from Drive.")

    existing_files = [f for f in os.listdir(local_save_path) if f.startswith('supplementary_vid')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('supplementary_vid')[1].split('.mp4')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename files
    original_files = os.listdir(local_save_path)
    for f in original_files:
        max_num += 1
        new_name = f"supplementary_vid{max_num}.mp4"
        shutil.move(os.path.join(local_save_path, f), os.path.join(local_save_path, new_name))
        print(f"Moved and renamed {f} to {new_name}")

# Example usage:
folder_id = ''
local_save_path = r"C:\Users\ryanc\OneDrive\Documents\YTE\LipSyncClips"
main()
