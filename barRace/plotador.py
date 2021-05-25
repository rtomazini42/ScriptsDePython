import bar_chart_race as bcr
import pandas as pd

dados = pd.read_csv('PROMONcomplete.csv')
#dados.fillna(0)
#dados.dropna(subset=["Abertas no Prazo"],inplace = True)
df = dados.set_index('data')

df=df.drop(columns=["total", "Abertas no Prazo","Abertas em Atraso","Encerradas","total de tudo"])
print(df.head())

#dados=pd.DataFrame(dados.groupby(["data","data"]).sum()["total"]).unstack().T.droplevel(level=0)

bcr.bar_chart_race(df =df,figsize=(1920/96, 1080/96),n_bars=3,period_length=1000,bar_label_size=22,tick_label_size=22,title='Promon',
period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                  's': f'Total: {v.nlargest(6).sum():,.0f}',
                                  'ha': 'right', 'size': 32, 'family': 'Courier New'},
period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center','size': 26},
 filename='promon.mp4')
