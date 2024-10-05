# Spotify Playlist Downloader

## Overview

The **Spotify Playlist Downloader** is a Python application that allows users to log in to their Spotify accounts, view their playlists, and download the audio tracks from selected playlists. The application utilizes the Spotipy library for Spotify API interactions and yt-dlp for downloading audio.

## Features

- User authentication with Spotify using OAuth2.
- Displays user playlists for easy selection.
- Downloads audio tracks in MP3 format.
- Compiles downloaded tracks into a ZIP file for convenient downloading.
- API keys and sensitive information are securely managed using environment variables, ensuring they are not exposed in the source code or public repositories.

## Requirements

- Python 3.8 or higher
- Required libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd Spotify-Playlist-Downloader
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project with the following content:
   ```env
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

4. Replace `your_spotify_client_id` and `your_spotify_client_secret` with your actual Spotify API credentials.

## Running the Application

To start the Flask application, run the following command in your Command Prompt:

```bash
python app.py
```

Visit `http://localhost:5000` in your web browser to access the application.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SPOTIFY_CLIENT_ID=your_spotify_client_id`
`SPOTIFY_CLIENT_SECRET=your_spotify_client_secret`




## How to Use

1. Click the **Login with Spotify** button to authenticate your account.
2. Select a playlist from your account.
3. Click the **Download** button to download the tracks as a ZIP file.

## Additional Information

- Make sure to keep your `.env` file secure and do not share it publicly.
- You can add your Spotify API credentials to the `.env` file as mentioned above to ensure your application can access the Spotify API.


## Conclusion

This project showcases my skills in Python programming, web development, and API integration. Feel free to explore the code and contribute!


## Documentation

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)


## License

[MIT](https://choosealicense.com/licenses/mit/)

- Disclaimer: This project is intended for educational purposes only. It is the responsibility of users to ensure they comply with copyright laws and the terms of service of Spotify and YouTube Music. The use of this project for downloading copyrighted material without permission is strictly prohibited.


