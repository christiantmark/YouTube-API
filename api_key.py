from googleapiclient.discovery import build


api_key = 'AIzaSyCXxOIPYExX6J3UCGB6V6bbc0ibg8kLWlw'

youtube = build('youtube', 'v3', developerKey = api_key)

request = youtube.channels().list(
    part = 'statistics',
    forUsername = 'tseries'
)

response = request.execute()

print(response)