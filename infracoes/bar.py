import seaborn as sns
import pandas as pd

dados = pd.read_csv('C:/Users/Tomazini/Desktop/bar_race/infracoes2020completo.csv', sep=';')
dados.head()
infracoes = dados.descricaoinfracao.unique()

infracoes = dados["descricaoinfracao"].value_counts().to_frame().reset_index()

infracoes.head(10)

import matplotlib.pyplot as plt
g = sns.barplot(y ="index",x="descricaoinfracao", data = infracoes.head(10))
g.figure.savefig('a.jpg', figsize='large')


help(g.figure)
