import requests

API_KEY_LABEL = "apikey="
API_KEY = "29aeabb2b877f655784dbbf82592d33d"
METHOD = "matcher.lyrics.get"
BASE_URL = "https://api.musixmatch.com/ws/1.1/"
FORMAT = "?format=json&callback=callback"
ARTIST_LABEL = "q_artist="
TRACK_LABEL = "q_track="


def buildFinalURL(songName, artistName):
    first_part = BASE_URL + METHOD + FORMAT + f'&{TRACK_LABEL}{songName.replace(" ", "%20")}'
    second_part = f'&{ARTIST_LABEL}{artistName.replace(" ", "%20")}' + f'&{API_KEY_LABEL}{API_KEY}'
    return first_part + second_part


def getLyricSong(song, artist):
    response = requests.get(buildFinalURL(song, artist))
    data = response.json()
    return data['message']['body']['lyrics']['lyrics_body']


if __name__ == '__main__':
    try:
        print(getLyricSong("", "John Lennon"))
    except TypeError:
        print("No song")