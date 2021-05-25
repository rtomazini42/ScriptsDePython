import bar_chart_race as bcr
import pandas as pd

dados = pd.read_csv('covid5.csv')
#print(dados.head)
dados.dropna(subset=["total_deaths"],inplace = True) #Remover vazios com dropna
dados.dropna(subset=["date"],inplace = True)
dados.fillna(0)
print(dados)
covid_bcr=pd.DataFrame(dados.groupby(["location","date"]).sum()["total_deaths"]).unstack().T.droplevel(level=0)
#covid_bcr.columns
covid_bcr=covid_bcr.drop(columns=["World","Asia","Africa","North America","South America", "European Union", "Europe"])
covid_bcr.fillna(0) #colocar 0 onde faltar o dado
print(covid_bcr)

print(covid_bcr.head)
bcr.bar_chart_race(df =covid_bcr,figsize=(1920/96, 1080/96),n_bars=12,period_length=300,bar_label_size=22,tick_label_size=22,title='COVID-19 Deaths by Country',
period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                  's': f'Total deaths: {v.nlargest(6).sum():,.0f}',
                                  'ha': 'right', 'size': 32, 'family': 'Courier New'},
period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center','size': 26},
 filename='covid19_final.mp4')
print("done")
