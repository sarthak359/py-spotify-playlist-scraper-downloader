from flask import Flask, redirect, session, url_for, request, send_file, render_template
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import yt_dlp
import os
import zipfile

load_dotenv()  # Load the variables from .env file

app = Flask(__name__)

# Set your secret key, client ID, and client secret here
app.secret_key = '61e7a503ec1b28bb0e1c7d5a141a6906'  # Change this to a strong secret key
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'
SCOPE = 'playlist-read-private user-library-read user-read-email playlist-read-collaborative'

# Set up Spotify API authentication
sp_oauth = SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)

@app.route('/')
def index():
    # Check if the user is logged in
    if 'token_info' in session:
        sp = spotipy.Spotify(auth=session['token_info']['access_token'])
        user_profile = sp.current_user()  # Fetch the user's profile information
        user_name = user_profile['display_name']  # Get the user's display name
        
        # Fetch user's playlists
        playlists_data = sp.current_user_playlists()
        playlists = [{'id': pl['id'], 'name': pl['name']} for pl in playlists_data['items']]
        
        return render_template('index.html', user=user_name, playlists=playlists)  # Pass user info and playlists to the template
    else:
        return render_template('index.html', user=None, playlists=None)

@app.route('/login')
def login():
    return redirect(sp_oauth.get_authorize_url())

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('index'))

@app.route('/download_playlists/<playlist_id>')
def download_playlists(playlist_id):
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('login'))

    sp = spotipy.Spotify(auth=token_info['access_token'])
    playlist_tracks = sp.playlist_tracks(playlist_id)

    temp_output_dir = 'temp'
    os.makedirs(temp_output_dir, exist_ok=True)

    ffmpeg_location = 'C:\\ffmpeg\\bin'  # Adjust this path as necessary

    downloaded_files = []

    # Download each track in the playlist
    for item in playlist_tracks['items']:
        track = item['track']
        track_name = f"{track['name']} by {track['artists'][0]['name']}".replace("/", "_")
        print(f'Starting download for: {track_name}')

        # Set up yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(temp_output_dir, f"{track_name}.%(ext)s"),
            'ffmpeg_location': ffmpeg_location,
            'default_search': 'ytsearch',
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([track_name])
            downloaded_files.append(os.path.join(temp_output_dir, f"{track_name}.mp3"))
            print(f'Download complete for: {track_name}')
        except Exception as e:
            print(f'Error downloading {track_name}: {e}')

    # Create a ZIP file of all downloaded MP3s
    zip_filename = os.path.join(temp_output_dir, f'playlist_{playlist_id}.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for file_path in downloaded_files:
            print(f'Adding {file_path} to ZIP file.')
            if os.path.isfile(file_path):
                zip_file.write(file_path, os.path.basename(file_path))
            else:
                print(f'File not found: {file_path}')

    return send_file(zip_filename, as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
