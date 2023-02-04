from pytube import YouTube


class SongDownloader:

    def download(self, url, output_path, song_title):
        output_file_name = f"{song_title.replace('/', '-').replace('?', '').replace('|', '-').replace(': ','')}.mp3"
        youtube = YouTube(url)
        try:
            stream = youtube.streams.get_by_itag(251)
        except:
            print("error downloading stream")
            return
        if stream is None:
            return
        stream.download(output_path, output_file_name)
