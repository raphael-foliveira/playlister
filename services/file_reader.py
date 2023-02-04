

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, "r") as file:
            artist_names = [
                artist.replace("\n", "") for artist in file.readlines()
            ]
        return artist_names
