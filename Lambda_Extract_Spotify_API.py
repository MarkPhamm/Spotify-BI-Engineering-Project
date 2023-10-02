import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    cilent_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=cilent_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/2YRe7HRKNRvXdJBp9nXFza"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    # Initialize an empty list to store all the tracks
    all_tracks = []
    
    # Initialize the offset to 0
    offset = 0
    
    # Set the limit to the maximum allowed (100 tracks per request)
    limit = 100
    
    while True:
        # Retrieve the next batch of tracks
        batch = sp.playlist_tracks(playlist_URI, offset=offset, limit=limit)
    
        # Add the batch of tracks to the list
        all_tracks.extend(batch['items'])
    
        # Check if there are more tracks to retrieve
        if len(batch['items']) < limit:
            break
    
        # Increment the offset for the next request
        offset += limit
    
    # Continue with the rest of your code to process the data
    
    # The code that follows can remain the same as in your original code
    spotify_data = {
        'href': batch['href'],  # The last href from the loop
        'items': all_tracks
    }
    # spotify_data = sp.playlist_tracks(playlist_URI)   
    cilent = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    cilent.put_object(
        Bucket="spotify-bi-engineering-project",
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(spotify_data)
        )
