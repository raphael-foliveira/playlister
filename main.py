from playwright.sync_api import sync_playwright
from services.downloader import Downloader
from services.file_reader import FileReader
from services.scraper import YoutubeSearchScraper
from services.song_downloader import SongDownloader


def main():
    file_reader = FileReader("./sample.txt")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        downloader = Downloader(
            file_reader,
            YoutubeSearchScraper(page),
            SongDownloader(),
            "./songs/"
        )
        downloader.run()


if __name__ == "__main__":
    main()
