import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
df=pd.read_csv("listings.csv")


df.dropna(subset=['summary'], axis=0, inplace = True) #remoção de linhas
summary = df['summary']
all_summary = " ".join(s for s in summary)
stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "você", "de", "ao", "os"])
wordcloud = WordCloud(stopwords=stopwords,
                      background_color='black', width=1600,
                      height=800).generate(all_summary)


fig, ax = plt.subplots(figsize=(16,8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file('nuvem.png',);
