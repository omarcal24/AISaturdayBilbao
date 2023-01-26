import pandas as pd
from tqdm import tqdm
import lyricsgenius
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import azapi
import os

download_path = os.path.join(os.getcwd(),"track_lyrics")
N_TRACKS = 200

# Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5b083e73f8eb4634b48df2564599aa16",
                                                           client_secret="9796967666864a2690268eb8b81a87c6"))


#### get df
df_tracks = pd.read_csv(f"tracks.csv")

# get lyrics
lyrics = []
genres = []
df_test = df_tracks.sample(N_TRACKS)

for id,track in tqdm(df_test.iterrows()):
    sleep_time = random.randint(5,10)
    track_name = track["name"]
    artist = track["artists"]

    API = azapi.AZlyrics("duckduckgo", accuracy=0.5)
    API.artist = artist
    API.title = track_name
    API.getLyrics(save=True, ext='.txt')

    time.sleep(sleep_time)
'''
df_test["lyrics"] = lyrics   
df_test["genres"] = genres

df_test.to_csv(f"augmented_dataset__N{N_TRACKS}.csv")
'''