import os
from pydub import AudioSegment

def concatenate_audios(audio_files):
    combined = AudioSegment.empty()
    for file in audio_files:
        audio = AudioSegment.from_file(file)
        combined += audio
    return combined

def split_audio_into_segments(combined_audio, segment_length=150000):
    """Splits the audio into segments of specified length (default: 150,000 milliseconds or 2.5 minute)."""
    segments = []
    segment_start_time = 0
    segment_end_time = segment_length
    length_audio = len(combined_audio)
    while segment_start_time < length_audio:
        segment = combined_audio[segment_start_time:segment_end_time]
        segments.append(segment)
        segment_start_time += segment_length
        segment_end_time += segment_length
    return segments

def save_segments_to_flac(segments):
    file_paths = []
    for index, segment in enumerate(segments):
        file_name = f"segment_{index}.flac"
        segment.export(file_name, format="flac")
        file_paths.append(file_name)
        if index==2:
            break
    return file_paths


def main():
    if __name__ == "__main__":
        # Get all mp3 files
        audio_files = [
            file
            for file in os.listdir(os.getcwd())
            if os.path.isfile(file) and file.endswith(".mp3")
        ]

        # Concatenate and save audio files to combined_audio.flac
        combined = concatenate_audios(audio_files)

        # Split the concatenated audio into segments of 1 minute each
        segments = split_audio_into_segments(combined, segment_length=60000)  # 1 minute

        # Save each segment to a .flac file
        segment_file_paths = save_segments_to_flac(segments)

        
