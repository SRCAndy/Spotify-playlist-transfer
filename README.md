Spotify Playlist Manipulation
This Python script uses the Spotipy library to interact with the Spotify Web API. It allows you to manipulate playlists, including reading tracks from a user's saved tracks and adding them to a playlist.

Prerequisites
To use this script, you will need:

1. Python installed on your machine. You can download Python from here.# Spotify Playlist Manipulation

This Python script uses the Spotipy library to interact with the Spotify Web API. It allows you to manipulate playlists, including reading tracks from a user's saved tracks and adding them to a playlist.

## Prerequisites

To use this script, you will need:

1. Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

2. The Spotipy library. You can install it using pip:

    ```
    pip install spotipy
    ```

3. A Spotify Developer account. You can create one [here](https://developer.spotify.com/dashboard/).

4. A Spotify app registered on the Spotify Developer Dashboard. This will provide you with a Client ID and a Client Secret.

5. The ID of the destination playlist where you want to add tracks.

## Setup

1. Replace `'Your_ClientID'` and `'Your_SecretID'` in the script with your Spotify app's Client ID and Client Secret, respectively.

2. Replace `'The_destination_Playlist'` with the ID of your destination playlist.

3. If necessary, replace `'http://localhost:8080'` with your desired redirect URI. This should match the redirect URI set in your Spotify app settings on the Spotify Developer Dashboard.

## Running the Script

To run the script, simply navigate to the directory containing the script in your terminal and run:

```
python playlist.py
```

The script will authenticate with Spotify, read tracks from the user's saved tracks, and add them to the specified playlist.

The Spotipy library. You can install it using pip:

A Spotify Developer account. You can create one here.

A Spotify app registered on the Spotify Developer Dashboard. This will provide you with a Client ID and a Client Secret.

The ID of the destination playlist where you want to add tracks.

Setup
Replace 'Your_ClientID' and 'Your_SecretID' in the script with your Spotify app's Client ID and Client Secret, respectively.

Replace 'The_destination_Playlist' with the ID of your destination playlist.

If necessary, replace 'http://localhost:8080' with your desired redirect URI. This should match the redirect URI set in your Spotify app settings on the Spotify Developer Dashboard.

Running the Script
To run the script, simply navigate to the directory containing the script in your terminal and run:

The script will authenticate with Spotify, read tracks from the user's saved tracks, and add them to the specified playlist.
