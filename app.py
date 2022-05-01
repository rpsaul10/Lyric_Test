from flask import Flask, render_template, session, request

import LyricTest

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if not ('song' in session):
        session['song'] = ''
        return render_template("index.html")

    songName = request.form['song_name']
    artistName = request.form['artist_name']

    try:
        lyric_song = LyricTest.getLyricSong(song=songName, artist=artistName).replace('"', "")
        if not lyric_song == "":
            return render_template("index.html", song=lyric_song, label_song=songName, label_artist=artistName)
        return render_template("index.html", song="The lyrics of the song are forbidden, try another one.",
                               label_song=songName, label_artist=artistName)
    except TypeError:
        return render_template("index.html", song="The song is not available, try another one.", label_song=songName,
                               label_artist=artistName)


if __name__ == '__main__':
    app.run()
