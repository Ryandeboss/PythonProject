# Need: liapix, talkingImageGenorator, AudioEffectsScraper, AnotherVoiceCloner
# Extra: Voice Diarization, Voice enhancer, 3dworld genorator, maybe coolEffectsGenorator/Scraper

# Logistics
from ChatGPTAPI import main as CGPT


# Voice cloner and genorator
from YTGetVoiceVid import main as YTGV #(takes 3 args, method, channel_name, query)
from AudioSegmenter import main as ASG 
from ElevenlabsAPIv2 import main as ELA2 # Takes 3 argument,  
                                         # name of output file,
                                         # the description of the voice,
                                         # and the lines to be said

# AI image genorators
from ClickDrop import main as SDXL1 # takes 1 arg, prompt, and returns true when done. Ouput saved in ClickdropImgs folder
from DalleIMG_GEN import main as Dalle # takes 1 arg, prompt, and returns true when done. Ouput saved in OtherImgs folder


# AI img-vid genorator
from Kaiber import main as Kaiber # Takes 2 argument: image path, and a prompt. Returns true when done, returns false if fails
from RWML import main as Runway # Takse 2 arguments: image path, and a prompt. Returns true when done

# Background animator
from Liapix import main as BackgroundAnimator # Takes 1 arguement: image path, Returns true when done

# Lip Sync
from ImgToVIdGen import main as ITVG # Helps use images as lip sync material
from ComnnectColabToDrive import main as CCTGD # These three modules take videos with a face and make it talk.
from ColabAutomation import main as CA # Takes two arguments, video path and audio path
from DownloadGDrive import main as DTDG  # takes 0 arguments

# Suplementary video clips scraper
from PBVideoScraper import main as PBVS # Returns true or false based in whether it was able to get the video

# Sound Effects scrapper
from SoundBibleScraper import main as SBS # Returns true when done

# backgroundMusic
from PBMusicScraper import main as PBMS # Returns true when done





Query = '' 

method = eval(input('How would you like to searh Youtube (1 for quesry, 2 for channel name): '))
if method == 1:
    query = input('Whose voice would you like to seach Youtube for?: ')
    YTGV(method = 'query',query = query+' speaking') 
    ASG()
    ELA2(query)
if method == 2:
    channel_name = input('Which youtube channel? (Must be exact spelling): ')
    
    YTGV(method = 'channel', channel_username = channel_name)
    ASG()
    ELA2(channel_name)
