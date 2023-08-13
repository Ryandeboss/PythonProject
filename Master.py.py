from YTGetVoiceVid import main as YTGV #(takes 3 args, method, channel_name, query)
from AudioSegmenter import main as ASG 
from ElevenlabsAPIv2 import main as ELA2 # Takes 1 argument, name of output file, 
                                         # should be equal to either the query or channel_name.

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