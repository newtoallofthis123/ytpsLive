from youtube_search import YoutubeSearch
from youtubesearchpython import CustomSearch, VideoSortOrder, ChannelsSearch, Search, Video, ChannelSearch, StreamURLFetcher
from youtubesearchpython.internal.constants import ResultMode
from pytube import YouTube

def normal_results(search_term):
    results = YoutubeSearch(search_term, max_results=60).to_dict()
    return results

def video_info_results(video_url):
    video_info = Video.getInfo(video_url)
    video_results = { "title": video_info["title"], "url": video_info["link"], "view_count": video_info["viewCount"]["text"], "channel": video_info["channel"]["name"], "channel_link": video_info["channel"]["link"], "description": video_info["description"] }
    return video_results

def video_stream_fetcher(video_url):
    yt = YouTube(video_url)
    url = yt.streams[1].url
    return url

def audio_stream_fetcher(video_url):
    yt = YouTube(video_url)
    url = yt.streams[0].url
    return url