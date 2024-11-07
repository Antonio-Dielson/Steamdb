import pandas as pd
dfsteam = pd.read_csv('steam_dados.csv')
'''

Analise de qualidade dos dados

'''
print(dfsteam.head(20))
print(dfsteam.info())

'''

Transformações: remoção de colunas nulas e textos desnecessários na coluna Name,
renomeação de coluna e salvar o DataFrame em formato csv com as alterações.

'''
dfsteam.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Ends', 'Started'], inplace=True)
dfsteam['Name']= dfsteam['Name'].str.split('\n').str[0]
dfsteam.rename(columns={'%':'Discount_rate'}, inplace=True)

dfsteam.to_csv('silver_steam.csv', index=False)
df = pd.read_csv('silver_steam.csv')
print(df.head(10))