import wordcloud as wc
import io #para manter acentos
f = io.open("texto.txt", "r",  encoding="utf8")
texto = ""
for line in f:
    texto = texto + " " +line

#retira stopwords
stops = []
s = io.open("stopwords.txt", "r",  encoding="utf8")
for line in s:
    line = line.replace('\n', '')
    stops.append(line)

cloud = wc.WordCloud(font_path= "AdobeNaskh-Medium", stopwords=stops, width = 1594  , height = 396 ,colormap = "Pastel2",background_color = "black")
cloud.process_text(texto)
cloud.generate_from_text(texto)
cloud.to_file("nuvem.jpg")
