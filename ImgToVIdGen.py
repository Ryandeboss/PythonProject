import subprocess
import os
import shutil

def main(image_path, duration, output_path="output.mp4"):
    """
    Creates an MP4 video from an image with a specified duration.

    Parameters:
    - image_path (str): Path to the input image.
    - duration (int): Duration of the video in seconds.
    - output_path (str, optional): Path to the output MP4 video. Defaults to "output.mp4".

    Returns:
    - None
    """
    
    # Use ffmpeg to create the video
    cmd = [
        "ffmpeg",
        "-loop", "1",               # Loop the image
        "-i", image_path,           # Input image path
        "-c:v", "libx264",          # Video codec
        "-t", str(duration),        # Duration
        "-pix_fmt", "yuv420p",      # Pixel format
        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",  # Scale to even dimensions
        output_path                 # Output file
    ]
    
    subprocess.run(cmd)

    dest_dir = r"C:\Users\ryanc\OneDrive\Documents\YTE\StillFaceVids"  # Assuming current directory for simplicity; modify as needed
    source_dir = "."  # Assuming the output video is created in the current directory; modify as needed

    existing_files = [f for f in os.listdir(dest_dir) if f.startswith('supplementary_vid')]
    if existing_files:
        # Extract all numbers from existing filenames
        existing_numbers = [int(f.split('supplementary_vid')[1].split('.mp4')[0]) for f in existing_files]
        max_num = max(existing_numbers)
    else:
        max_num = 0

    # Move and rename file
    max_num += 1
    new_name = f"atillFace{max_num}.mp4"
    shutil.move(os.path.join(source_dir, output_path), os.path.join(dest_dir, new_name))
    print(f"Moved and renamed {output_path} to {new_name}")

if __name__ == "__main__":

    image_path = r"C:\Users\ryanc\OneDrive\Documents\YTE\geek6.jpg"
    duration = 10
    
    main(image_path, duration)

