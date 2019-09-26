import lyricsgenius as genius
import sys
from threading import Thread

class LyricsRipper(Thread):

    def __init__(self, artist_name):
        Thread.__init__(self)
        self.artist_name = artist_name

    def run(self):
        api = genius.Genius('RkxM70rkXh_rRNHT3GsYZc80wyfiX-X2sCXmQxGuST2nyrP3dF6zRk9UYR2cSEHb')
        try:
            artist = api.search_artist(self.artist_name)
        except :
            print(self.artist_name + "has stopped")        

        artist.save_lyrics('json', "./output/" + self.artist_name, 1)

artist_list = [
    'Dinos Punchliovic',
    'Espiiem',
    'IAM'
]

thread_list = []

for name in artist_list:
    thread_list.append(LyricsRipper(name))

for thread in thread_list:
    thread.start()
