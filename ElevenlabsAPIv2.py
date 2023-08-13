from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History
from moviepy.editor import AudioFileClip
from pydub import AudioSegment
set_api_key("SuperSecret")



def main(Keyword):
    if __name__ == "__main__":
        voice = clone(
            name=Keyword, # SHOULD MATCH THE SEARCH WORD USED IN YTGetVoiceVid.py
            description="An old American male voice with a slight hoarseness in his throat. Perfect for news.",
            files=["./segment_0.flac", "./segment_1.flac", "./segment_2.flac", "./segment_3.flac", "./segment_4.flac" ]
        )

        audio = generate(text="Some very long text to be read by the voice.", voice=voice)

        # Assuming the audio is a byte-like object, save it temporarily as a wav file
        temp_filename = "temp_audio.wav"
        with open(temp_filename, 'wb') as f:
            f.write(audio)

        # Convert and save as .flac using moviepy
        audio_clip = AudioFileClip(temp_filename)
        flac_filename = f"{voice.name}.flac"
        audio_clip.write_audiofile(flac_filename, codec='flac')

