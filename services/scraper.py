from dataclasses import dataclass

from playwright.sync_api import Page


@dataclass
class Song:
    title: str
    artist: str
    url: str


class Scraper:
    def __init__(self, page: Page):
        self.page = page


class YoutubeSearchScraper(Scraper):

    def __init__(self, page: Page):
        super().__init__(page)
        self.playlist_link_selector = "#lists #items ytd-watch-card-compact-video-renderer .yt-simple-endpoint"

    def get_songs_from_artist(self, artist_name: str):
        self.page.goto(
            f"https://www.youtube.com/results?search_query=" + artist_name.replace(" ", "+"))
        self.page.wait_for_selector(
            self.playlist_link_selector, timeout=12000)

        try:
            playlist_links = self.page.query_selector_all(
                self.playlist_link_selector)

            if len(playlist_links) == 0:
                raise Exception("Playlist element could not be found")

            songs = self.get_songs_from_playlist(playlist_links)
            return songs
        except:
            print("playlist could not be found")

        return []

    def get_songs_from_playlist(self, playlist_links):
        songs: list[Song] = []
        artist_name_element = self.page.query_selector(
            "#secondary #channel-name .ytd-channel-name #text")

        if not artist_name_element:
            raise Exception("Artist playlist could not be found")

        for link_element in playlist_links:
            song_title_element = link_element.query_selector(".title")

            if not song_title_element:
                continue

            song_title = song_title_element.inner_text()
            song_url = link_element.get_attribute("href")

            if song_title_element and artist_name_element and song_url:
                songs.append(
                    Song(song_title, artist_name_element.inner_html(), f"http://www.youtube.com/watch?v={song_url}"))
        return songs
