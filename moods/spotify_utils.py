# moods/spotify_utils.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

client_credentials_manager = SpotifyClientCredentials(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_songs_for_mood(mood):
    mood_playlists = {
        'happy': '6FO1ov3BIoIyjTWUtNLrUD',
        'sad': '0SxaRg6LF1BYnT35VFWen1',
        'angry': '05XuZKPM0eIq2k8qLLUvZ7',
        'anxious': '5VSe1ZlxNnaOKN9gyAKGUz',
        'neutral': '0jo6XJx3PD3kxi9A27kLwx'
    }
    playlist_id = mood_playlists.get(mood, mood_playlists['neutral'])
    print(f"Fetching songs for mood: {mood}, Playlist ID: {playlist_id}")
    
    try:
        results = sp.playlist_tracks(playlist_id)
        tracks = [
            {
                'name': track['track']['name'],
                'artists': [{'name': artist['name']} for artist in track['track']['artists']],
                'preview_url': track['track']['preview_url'],
                'album': {
                    'images': track['track']['album']['images']
                }
            }
            for track in results['items'] if track['track']['preview_url']
        ]
        print(f"Tracks fetched: {tracks}")
        return tracks
    except Exception as e:
        print(f"Error fetching tracks: {e}")
        return []
