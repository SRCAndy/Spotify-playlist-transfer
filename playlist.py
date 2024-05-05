
from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import spotipy
import os
from spotipy.exceptions import SpotifyException

cid = 'Your_ClientID'
secret = 'Your_SecretID'
playlist_id = 'The_destination_Playlist'

redirect_uri = 'http://localhost:8080'  # Replace with your desired redirect URI

def create_spotify_oauth():
    """
    Creates and returns a SpotifyOAuth object for authentication.

    Returns:
        SpotifyOAuth: The SpotifyOAuth object.
    """
    return SpotifyOAuth(
        client_id=cid,
        client_secret=secret,
        redirect_uri=redirect_uri,
        scope="user-library-read playlist-modify-public playlist-modify-private"
    )

oauth = create_spotify_oauth()

sp = spotipy.Spotify(auth_manager=oauth)

# Start a local server to handle the authentication callback
webbrowser.open(redirect_uri)

def get_playlist_song_uris(playlist_id):
    """
    Retrieves the URIs of all songs in a given playlist.

    Args:
        playlist_id (str): The ID of the playlist.

    Returns:
        list: A list of song URIs.
    """
    results = sp.playlist_items(playlist_id)
    try:
        uris = [item['track']['uri'] for item in results['items']]
    except KeyError as e:
        print(f"Error: {e}")
        # Handle the exception here
    return uris

def remove_playlist_tracks(playlist_id, uris):
    """
    Removes all occurrences of specified tracks from a playlist.

    Args:
        playlist_id (str): The ID of the playlist.
        uris (list): A list of song URIs to be removed.
    """
    try:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, uris)
    except SpotifyException as e:
        print(f"Error: {e}")

def count_playlist_tracks(playlist_id):
    """
    Counts the number of tracks in a playlist.

    Args:
        playlist_id (str): The ID of the playlist.

    Returns:
        int: The number of tracks in the playlist.
    """
    results = sp.playlist_items(playlist_id)
    return results['total']

def show_tracks(results):
    """
    Adds tracks to the playlist.

    Args:
        results (dict): The results containing the tracks to be added.
    """
    for idx in range(0, len(results['items']), 100):
        uris = [item['track']['uri'] for item in results['items'][idx:idx+100]]
        sp.playlist_add_items(playlist_id, uris)

def add_liked_songs_to_playlist():
    """
    Adds all liked songs to the playlist.
    """
    results = sp.current_user_saved_tracks()

    show_tracks(results)

    while results['next']:
        results = sp.next(results)
        show_tracks(results)

    print("All liked songs have been added to the playlist!")

if __name__ == "__main__":
    # Wait until all playlist tracks are removed
    print("Waiting for all tracks to be removed...")
    while count_playlist_tracks(playlist_id) > 0:
        print(f"Tracks remaining: {count_playlist_tracks(playlist_id)}")
        remove_playlist_tracks(playlist_id, get_playlist_song_uris(playlist_id))
    add_liked_songs_to_playlist()