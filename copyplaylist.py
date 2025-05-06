from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
from spotipy.exceptions import SpotifyException

# Configuración de credenciales
cid = 'your_cid'
secret = 'your_secreid'
source_playlist_id = 'idsource'  # Playlist de origen
target_playlist_id = 'idtarget'  # Playlist de destino

redirect_uri = 'http://localhost:8080'  # URI de redirección

def create_spotify_oauth():
    """
    Crea y retorna un objeto SpotifyOAuth para autenticación.
    
    Returns:
        SpotifyOAuth: El objeto de autenticación.
    """
    return SpotifyOAuth(
        client_id=cid,
        client_secret=secret,
        redirect_uri=redirect_uri,
        scope="playlist-read-private playlist-modify-public playlist-modify-private"
    )

# Autenticación
oauth = create_spotify_oauth()
sp = spotipy.Spotify(auth_manager=oauth)

# Abrir navegador para autenticación (si es necesario)
webbrowser.open(redirect_uri)

def get_playlist_tracks(playlist_id):
    """
    Obtiene todas las canciones de una playlist.
    
    Args:
        playlist_id (str): ID de la playlist.
        
    Returns:
        list: Lista de URIs de las canciones.
    """
    try:
        results = sp.playlist_items(playlist_id)
        tracks = results['items']
        
        # Manejar paginación si hay más de 100 canciones
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
            
        # Extraer URIs de las canciones
        uris = [item['track']['uri'] for item in tracks if item['track'] is not None]
        return uris
        
    except SpotifyException as e:
        print(f"Error al obtener canciones de la playlist: {e}")
        return []

def add_tracks_to_playlist(playlist_id, track_uris):
    """
    Añade canciones a una playlist.
    
    Args:
        playlist_id (str): ID de la playlist destino.
        track_uris (list): Lista de URIs de canciones a añadir.
    """
    try:
        # Spotify solo permite añadir 100 canciones a la vez
        for i in range(0, len(track_uris), 100):
            batch = track_uris[i:i+100]
            sp.playlist_add_items(playlist_id, batch)
        print(f"Se añadieron {len(track_uris)} canciones a la playlist.")
    except SpotifyException as e:
        print(f"Error al añadir canciones: {e}")

def clear_playlist(playlist_id):
    """
    Elimina todas las canciones de una playlist.
    
    Args:
        playlist_id (str): ID de la playlist a vaciar.
    """
    try:
        tracks = get_playlist_tracks(playlist_id)
        if tracks:
            sp.playlist_remove_all_occurrences_of_items(playlist_id, tracks)
            print(f"Se eliminaron {len(tracks)} canciones de la playlist.")
    except SpotifyException as e:
        print(f"Error al vaciar la playlist: {e}")

def copy_playlist(source_id, target_id, clear_target=False):
    """
    Copia canciones de una playlist a otra.
    
    Args:
        source_id (str): ID de la playlist origen.
        target_id (str): ID de la playlist destino.
        clear_target (bool): Si True, vacía la playlist destino antes de copiar.
    """
    print("Obteniendo canciones de la playlist de origen...")
    track_uris = get_playlist_tracks(source_id)
    
    if not track_uris:
        print("No se encontraron canciones en la playlist de origen.")
        return
    
    print(f"Se encontraron {len(track_uris)} canciones en la playlist de origen.")
    
    if clear_target:
        print("Vaciando playlist de destino...")
        clear_playlist(target_id)
    
    print("Copiando canciones a la playlist de destino...")
    add_tracks_to_playlist(target_id, track_uris)
    
    print("¡Proceso completado!")

if __name__ == "__main__":
    # Ejemplo de uso:
    copy_playlist(source_playlist_id, target_playlist_id, clear_target=True)