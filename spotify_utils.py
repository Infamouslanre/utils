import spotipy
from spotipy.oauth2 import SpotifyOAuth

def fetch_new_releases():
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    followed_artists = sp.current_user_followed_artists(limit=50)
    followed_artist_ids = [artist['id'] for artist in followed_artists['artists']['items']]

    new_releases_list = []
    for artist_id in followed_artist_ids:
        artist_new_releases = sp.artist_albums(artist_id, album_type='album', limit=10)
        for album in artist_new_releases['items']:
            album_name = album['name']
            artists = ', '.join([artist['name'] for artist in album['artists']])
            release_date = album['release_date']
            album_link = album['external_urls']['spotify']
            album_image = album['images'][0]['url'] if album['images'] else None
            new_releases_list.append((album_name, artists, release_date, album_link, album_image))

    return new_releases_list

def fetch_new_releases_sorted():
    new_releases_list = fetch_new_releases()
    new_releases_list.sort(key=lambda x: x[2], reverse=True)
    return new_releases_list
