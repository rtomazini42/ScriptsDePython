import io #para manter acentos
import wordcloud as wc
import numpy as np
from PIL import Image
from os import path

#with open('stopwords.txt', 'r') as f:
#    stops = f.readlines()

my_mask = np.array(Image.open(path.join("mask.png")))
stops = []
s = io.open("stopwords.txt", "r",  encoding="utf8")
for line in s:
    line = line.replace('\n', '')
    stops.append(line)
#print(stops)
txt = ""
f = io.open("texto.txt", "r",  encoding="utf8")
for line in f:
    txt = txt + " " +line
f.close()
cloud = wc.WordCloud(font_path= "AdobeNaskh-Medium", stopwords=stops, width = 1920, height = 1080, mask = my_mask, contour_width=1, contour_color='white', colormap = "Pastel1")
cloud.process_text(txt)
cloud.generate_from_text(txt)
cloud.to_file("promon.jpg")
