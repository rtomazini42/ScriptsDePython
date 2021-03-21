import io #para manter acentos
import wordcloud as wc

#with open('stopwords.txt', 'r') as f:
#    stops = f.readlines()
stops = []
s = io.open("stopwords.txt", "r",  encoding="utf8")
for line in s:
    line = line.replace('\n', '')
    stops.append(line)
#print(stops)
cloud = wc.WordCloud(stopwords=stops)
txt = ""
f = io.open("texto.txt", "r",  encoding="utf8")
for line in f:
    txt = txt + " " +line
f.close()

cloud.process_text(txt)
cloud.generate_from_text(txt)
cloud.to_file("hell.jpg")
