import os
import shutil

from services.file_reader import FileReader

from services.scraper import Scraper, YoutubeSearchScraper
from services.song_downloader import SongDownloader


class Downloader:

    def __init__(self, file_reader: FileReader, scraper: Scraper, song_downloader: SongDownloader, download_dir: str):
        self.file_reader = file_reader
        self.scraper = scraper
        self.song_downloader = song_downloader
        self.download_dir = download_dir

    def run(self):
        artist_names = self.file_reader.read()
        for artist in artist_names:
            self.download_songs_from_artist(artist)

    def download_songs_from_artist(self, artist_name):
        output_path = f"{self.download_dir}/{artist_name.replace(' ', '_')}"

        songs = self.scraper.get_songs_from_artist(artist_name)

        if len(songs) == 0:
            return

        try:
            shutil.rmtree(output_path)
        except:
            print("output directory does not exist")
        finally:
            os.makedirs(output_path)

        for song in songs:
            print(artist_name, " - ", song.title)
            self.song_downloader.download(song.url, output_path, song.title)
