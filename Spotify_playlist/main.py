from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# Connect to Spotify APP
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR CLIENT ID",
        client_secret="YOUR CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)
# User Date
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD: ")
# Extract songs
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
songs = response.text

soup = BeautifulSoup(songs,'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)
# Verify songs
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# Create Playlist
playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
print(playlist)
# Add songs
sp.playlist_add_items(playlist_id=playlist['id'],items=song_uris)
