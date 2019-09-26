import json
import os
import re
import unicodedata

output_file = open("data.txt", "wb")

for root, dirs, files in os.walk("./output/", topdown=False):
    for name in files:
        with open("./output/" + name) as json_data:
            data_dict = json.load(json_data)
            for song in data_dict['songs']:
                lyrics = song['lyrics']

                #We remove anything between []
                matches = re.findall('([^[\]]+)(?:$|\[)', lyrics)
                lyrics = ""
                for string in matches :
                    lyrics+=string
                
                #normalize lirics to ASCII
                lyrics = unicodedata.normalize('NFKD', lyrics).encode('ASCII', 'ignore')

                #write on output file
                output_file.write(lyrics)

output_file.close()
