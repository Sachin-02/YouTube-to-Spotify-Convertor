import requests
import os
import json
from typing import List


class Spotify:
    def __init__(self, user_id: str, auth_token: str):
        self.user_id = user_id
        self.auth_token = auth_token

    def read_playlists(self):
        """ Returns all the playlist data for a user. """

        url = "https://api.spotify.com/v1/users/{user_id}/playlists".format(
            user_id=self.user_id
        )
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + self.auth_token,
            },
        )
        data = response.json()
        playlist_data = data["items"]
        return playlist_data

    def print_playlists(self):
        """ Prints the name of each playlist and how many tracks that playlist has. """

        playlist_data = self.read_playlists()
        for playlist in playlist_data:
            print(
                "The playlist "
                + playlist["name"]
                + " contains "
                + str(playlist["tracks"]["total"])
                + " tracks."
            )

    def filter_titles(self, song_list: List[str]) -> List[str]:
        """ Filters a list of titles so they are more likely to provide search results. """

        # Removes text to the right of the key character
        split_chars = ["(", "|", "[", "."]
        for char in split_chars:
            i = 0
            for song in song_list:
                song_list[i] = song.split(char)[0]
                i = i + 1
        # removes any of the key words from the string
        replace_words = [
            "Lyrics",
            "lyrics",
            "LYRICS",
            "Lyric",
            "lyric",
            "LYRIC",
            "VIDEO",
            "video",
            "Video",
            "ft",
            "feat",
        ]
        for word in replace_words:
            i = 0
            for song in song_list:
                song_list[i] = song.replace(word, "")
                i = i + 1
        return song_list

    def create_playlist(self, playlist_name: str) -> str:
        """ Returns the playlist id of a newly created playlist. """

        url = "https://api.spotify.com/v1/users/{user_id}/playlists".format(
            user_id=self.user_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.auth_token,
        }
        data = json.dumps({"name": playlist_name, "public": "false"})
        response = requests.post(url, headers=headers, data=data)
        data = response.json()
        playlist_id = data["id"]
        return playlist_id

    def get_spotify_song_uri(self, search: str) -> str:
        """ Returns the track_uri of the first song from a search result."""

        url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": "Bearer " + self.auth_token}
        params = {
            "q": "{search}".format(search=search),
            "type": "track",
            "market": "from_token",
            "limit": 1,
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        # if there are no search results, return none
        if data["tracks"]["total"] == 0:
            print("No results for this search")
            return None
        # return the uri of the first track from the search result
        else:
            track_uri = data["tracks"]["items"][0]["uri"]
            return track_uri

    def add_song_to_playlist(self, playlist_id: str, song_uri: str):
        """ Adds a song to a playlist using the uri and a playlist id. """
        song_uri = song_uri
        url = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(
            playlist_id=playlist_id
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.auth_token,
        }
        data = json.dumps({"uris": [song_uri]})
        response = requests.post(url, headers=headers, data=data)
