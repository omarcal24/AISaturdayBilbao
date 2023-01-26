import pandas as pd
from tqdm import tqdm
import lyricsgenius
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

N_TRACKS = 500

# Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="5b083e73f8eb4634b48df2564599aa16",
                                                           client_secret="9796967666864a2690268eb8b81a87c6"))
                                                       
## genius API 
GENIUS_TOKEN = "aXihRuMWBGV8mnv89rLHeS6ywIVluSsnaMnQr0W79qwe6XwGrdE0zoanTZBlNYne"
genius = lyricsgenius.Genius(GENIUS_TOKEN)

#### get df
df_tracks = pd.read_csv(f"tracks.csv")

# get lyrics
lyrics = []
genres = []
df_test = df_tracks.sample(N_TRACKS)



for id,track in tqdm(df_test.iterrows()):
    sleep_time = random.randint(7,20)
    song = genius.search_song(track["name"],track["artists"])
    sp_query = sp.search(q='artist:' + track["artists"], type='artist') 
    try:
        lyrics.append(song.lyrics)
    except:
        lyrics.append("Not found")
    try:
        genres.append(sp_query["artists"]["items"][0]["genres"])
    except KeyError:
        genres.append("Not found")   
    except IndexError:
        genres.append("Not found")
    except Exception as e:
        print(e)

    time.sleep(sleep_time)

df_test["lyrics"] = lyrics   
df_test["genres"] = genres

df_test.to_csv(f"augmented_dataset__N{N_TRACKS}.csv")
