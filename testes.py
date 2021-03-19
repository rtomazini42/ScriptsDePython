import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

games = pd.read_csv("Games.csv")
print(games.columns[0:-1])
games.shape
#sns.set(rc={'figure.figsize':(50,50)})
#print(games.count())
print(games.Game.describe())

sns.catplot(y = "Game", data = games, kind="count",size = 20,palette="dark:salmon", order = games['Game'].value_counts().iloc[:10].index)
plt.savefig('Game.png')
sns.catplot(y = "Series", data = games, kind="count",size = 20,palette="dark:salmon", order = games['Series'].value_counts().iloc[:10].index)
plt.savefig('Series.png')
sns.catplot(y = "Country", data = games, kind="count",size = 20,palette="dark:salmon", order = games['Country'].value_counts().iloc[:10].index)
plt.savefig('Country.png')
sns.catplot(y = "Ban Category", data = games, kind="count",size = 20,palette="dark:salmon", order = games['Ban Category'].value_counts().iloc[:10].index)
plt.savefig('Ban Category.png')
sns.catplot(y = "Developer", data = games, kind="count",size = 20,palette="dark:salmon", order = games['Developer'].value_counts().iloc[:10].index)
plt.savefig('Developer.png')
