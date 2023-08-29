from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History
from moviepy.editor import AudioFileClip
from pydub import AudioSegment
import os
set_api_key("")




def main(Keyword, desc, lines):
    if __name__ == "__main__":
        voice = clone(
            name=Keyword, # SHOULD MATCH THE SEARCH WORD USED IN YTGetVoiceVid.py
            description=desc,
            files=["training_audio/segment_0.flac", "training_audio/segment_1.flac", "training_audio/segment_2.flac", "training_audio/segment_3.flac", "training_audio/segment_4.flac" ]
        )   
    
        audio = generate(text=lines, voice=voice)

        # Assuming the audio is a byte-like object, save it temporarily as a wav file
        flac_filename = f"{voice.name}.flac"
        with open(flac_filename, 'wb') as f:
            f.write(audio)
            
        # Delete all files in the training_audio folder
        for filename in os.listdir('training_audio'):
            file_path = os.path.join('training_audio', filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

        


