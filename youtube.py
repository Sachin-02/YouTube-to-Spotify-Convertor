import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from typing import List


class Youtube:
    def __init__(self):
        self.youtube_client = self.create_youtube_client()

    def create_youtube_client(self):
        """ Logs into Youtube. Copied from the code snippets section of the YouTube API. """

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes
        )
        credentials = flow.run_console()

        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials
        )
        return youtube_client

        # end of copied code from the YouTube API

    def get_playlist_id(self, playlist_name: str) -> str:
        """ Reads through the user's youtube playlists and returns the id of the playlist specified. """

        request = self.youtube_client.playlists().list(
            part="snippet,contentDetails", mine=True
        )
        response = request.execute()
        data = response
        playlist_id = "_"
        for playlist in data["items"]:
            if playlist["snippet"]["title"] == playlist_name:
                playlist_id = playlist["id"]
        return playlist_id

    def get_song_list(self, playlist_id: str) -> List[str]:
        """ Reads the titles of each video in a playlist and returns them as a list of strings. """

        request = self.youtube_client.playlistItems().list(
            part="snippet,contentDetails", maxResults=50, playlistId=playlist_id
        )
        response = request.execute()
        data = response
        unfiltered_song_list = []
        for song in data["items"]:
            title = song["snippet"]["title"]
            unfiltered_song_list.append(title)
        return unfiltered_song_list
