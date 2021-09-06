from flask import Flask, render_template, request, redirect, session
from pytube.extract import video_info_url
from yt_scrap import audio_stream_fetcher, normal_results, video_info_results, video_stream_fetcher
import os
import json

app = Flask(__name__)

@app.route('/play_temp', methods =["GET", "POST"])
def play_temp():
    if request.method == "POST":
       video_url_raw = str(request.form.get("play_btn"))
    #    video_url = f'https://www.youtube.com/watch?v={video_url_raw}'
    #    video_info_url = video_info_results(str(video_url))
    #    video_url_stream = video_stream_fetcher(video_url)
    #    audio_url_stream = audio_stream_fetcher(video_url)
       return redirect(f'/play/{video_url_raw}')

@app.route('/play/<video_url_raw>')
def play(video_url_raw):
    video_url = f'https://www.youtube.com/watch?v={video_url_raw}'
    video_info_url = video_info_results(str(video_url))
    video_url_stream = video_stream_fetcher(video_url)
    audio_url_stream = audio_stream_fetcher(video_url)
    return render_template("play.html", url=video_url,url_stream=video_url_stream, url_info=video_info_url, url_id=video_url_raw, url_audio_stream=audio_url_stream)

@app.route('/search_temp', methods =["GET", "POST"])
def search_temp():
    if request.method == "POST":
       search_term = request.form.get("ytsearch")
       return redirect(f'/search/q={search_term}')

@app.route('/search/q=<search_term>')
def search_show(search_term):
    return render_template("search.html", items=normal_results(search_term), search_title=search_term.capitalize())

@app.route('/credits')
def credits_page():
    credits_list=["https://simpleicons.org/", "https://www.heroku.com/", "https://github.com/joetats/youtube_search", "https://github.com/alexmercerind/youtube-search-python", "https://flask.palletsprojects.com/en/", "https://newtoallofthis123.github.io/About", "https://github.com/pytube/pytube", "https://github.com", "https://youtube.com", "https://pypi.org/project/ytps/", "https://realfavicongenerator.net/"]
    return render_template("credits.html", urls=credits_list)

@app.route('/license')
def license_page():
    return render_template("license.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route("/")
def hello_world():
    return render_template('home.html')