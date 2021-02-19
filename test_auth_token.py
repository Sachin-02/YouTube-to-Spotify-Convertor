# This file can be run as a quick way to test if the authentication
# token is working or if it has expired

import os
import requests

spotify_oauth_token = os.environ.get("SPOTIFY_OAUTH_TOKEN")
spotify_user_id = os.environ.get("SPOTIFY_USER_ID")


def get_playlists(user_id: str, oauth_token: str):
    url = "https://api.spotify.com/v1/users/{user_id}/playlists".format(user_id=user_id)
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + oauth_token,
        },
    )
    data = response.json()
    return data


if __name__ == "__main__":
    playlists = get_playlists(spotify_user_id, spotify_oauth_token)
    print(playlists)
