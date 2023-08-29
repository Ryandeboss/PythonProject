from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pytube import YouTube
from moviepy.editor import *
import os
import re
import requests
import json

DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_videos(query, max_duration=1200):  # default max_duration set to 20 minutes (1200 seconds)
    # Helper function to convert ISO 8601 duration to seconds
    def iso8601_duration_to_seconds(duration):
        hours = 0
        minutes = 0
        seconds = 0
        time_part = re.search('PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?((?P<seconds>\d+)S)?', duration)
        if time_part:
            hours = int(time_part.group('hours')) if time_part.group('hours') else 0
            minutes = int(time_part.group('minutes')) if time_part.group('minutes') else 0
            seconds = int(time_part.group('seconds')) if time_part.group('seconds') else 0
        return hours * 3600 + minutes * 60 + seconds

    try:
        service = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = service.search().list(q=query, part="id,snippet", maxResults=50).execute()

        video_ids = []
        total_duration = 0

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                video_id = search_result['id']['videoId']
                video_details = service.videos().list(part="contentDetails", id=video_id).execute()
                duration = video_details['items'][0]['contentDetails']['duration']
                video_duration = iso8601_duration_to_seconds(duration)
                if total_duration + video_duration <= max_duration:
                    video_ids.append(video_id)
                    total_duration += video_duration

        return video_ids

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")

def get_youtube_channel_id(channel_name, key):
  """Returns the ID of the YouTube channel with the given name."""

  url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + channel_name + '&type=channel&key=' + key
  response = requests.get(url)

  if response.status_code == 200:
    data = json.loads(response.content)
    channels = data['items']

    if channels:
      channel = channels[0]
      return channel['id']
    else:
      return None

  else:
    print('Error searching for channel.')

def iso8601_duration_to_seconds(duration):
    hours = 0
    minutes = 0
    seconds = 0
    time_part = re.search('PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?((?P<seconds>\d+)S)?', duration)
    if time_part:
        hours = int(time_part.group('hours')) if time_part.group('hours') else 0
        minutes = int(time_part.group('minutes')) if time_part.group('minutes') else 0
        seconds = int(time_part.group('seconds')) if time_part.group('seconds') else 0
    return hours * 3600 + minutes * 60 + seconds


def search_popular_videos(channel_id, max_duration=420): # the duration is about 1200 seconds
    try:
        service = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = service.search().list(
            channelId=channel_id,
            part="id,snippet",
            order="date",
            maxResults=50
        ).execute()

        video_results = search_response.get('items', [])

        # Fetch video statistics and sort by view count to approximate popularity
        video_ids = [video['id']['videoId'] for video in video_results if video['id']['kind'] == 'youtube#video']
        video_details = service.videos().list(part="statistics", id=",".join(video_ids)).execute()
        sorted_videos = sorted(video_details['items'], key=lambda x: int(x['statistics']['viewCount']), reverse=True)

        # Select videos based on duration
        selected_video_ids = []
        total_duration = 0

        for video in sorted_videos:
            video_id = video['id']
            video_content_details = service.videos().list(part="contentDetails", id=video_id).execute()
            duration = video_content_details['items'][0]['contentDetails']['duration']
            video_duration = iso8601_duration_to_seconds(duration)
            if total_duration + video_duration <= max_duration:
                selected_video_ids.append(video_id)
                total_duration += video_duration

        return selected_video_ids

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
        return []

def download_audio(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"

    # Create a YouTube object
    yt = YouTube(url)

    # Get the audio stream with the highest quality
    audio_stream = yt.streams.filter(only_audio=True, file_extension="webm").first()

    # Download the audio
    audio_file_path = audio_stream.download()

    # Convert the webm file to mp3 using moviepy
    audio = AudioFileClip(audio_file_path)
    audio.write_audiofile(audio_file_path.replace(".webm", "VOICEAUDIO.mp3"))

    # Delete the original webm file
    os.remove(audio_file_path)


def main(method = "query", channel_username = "Kentucky Ballistics",query = "Donkey from Shreck"):
    if __name__ == "__main__":
        method = "query"
        video_ids = []
        if method == "channel":
            channel_username = "Kentucky Ballistics"
            channel_id = get_youtube_channel_id(channel_username,DEVELOPER_KEY)
            if channel_id:
                video_ids = search_popular_videos(channel_id['channelId'])
            else:
                print(f"Unable to find channel ID for username: {channel_username}")
        elif method == "query":
            query = "Donkey from Shreck"
            video_ids = search_videos(query)
        
        for video_id in video_ids:
            download_audio(video_id)


main()
