#!usr/bin/python
import requests, pandas

VOD_URL = 'https://www.twitch.tv/videos/136025964'

# Parses VOD ID number from the URL
vod_id = VOD_URL[VOD_URL.rfind( '/') + 1:] 

# Request with timestamp 0 to get error message
response = requests.get('https://rechat.twitch.tv/rechat-messages?start=0&video_id=v' + vod_id).json()

# Retrieves details of error message and splits into a list of words
detail = response['errors'][0]['detail'].split(' ')

# Start and stop timestamps
start = int(detail[4])
stop = int(detail[6])

timestamp = start

response = requests.get('https://rechat.twitch.tv/rechat-messages?start=' + str(timestamp) + '&video_id=v' + vod_id).json()
data_attributes = [x['attributes'] for x in response['data']]
d = pandas.DataFrame(data_attributes)
