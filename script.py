import os
import spotify
import youtube

spotify_oauth_token = os.environ.get("SPOTIFY_OAUTH_TOKEN")
spotify_user_id = os.environ.get("SPOTIFY_USER_ID")

if __name__ == "__main__":
    # intializing an instance of the youtube and spotify classes
    yt = youtube.Youtube()
    spotify = spotify.Spotify(spotify_user_id, spotify_oauth_token)

    yt_playlist_id = yt.get_playlist_id("Spotify")
    unfiltered_song_list = yt.get_song_list(yt_playlist_id)
    spotify_playlist_id = spotify.create_playlist("From Youtube")
    filtered_songs = spotify.filter_titles(unfiltered_song_list)
    # adding each song to the playlist
    for song in filtered_songs:
        track_uri = spotify.get_spotify_song_uri(song)
        # if a search result came back from the spotify API
        if track_uri != None:
            spotify.add_song_to_playlist(spotify_playlist_id, track_uri)
            print("Added {song} to the playlist".format(song=song))
