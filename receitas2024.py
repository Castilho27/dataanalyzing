import pandas as pd
import matplotlib.pyplot as plt

arquivo1 = 'Pesquisa Anual de Empresas 2024 - Ano Fiscal - Provisório.csv'
arquivo2 = 'Pesquisa Anual de Empresas - Ano Fiscal de 2024.csv'

df1 = pd.read_csv(arquivo1)
df2 = pd.read_csv(arquivo2)

print("Arquivo 1 info:")
print(df1.info())
print("\nArquivo 2 info:")
print(df2.info())

df1['Value'] = pd.to_numeric(df1['Value'], errors='coerce')
df2['value'] = pd.to_numeric(df2['value'], errors='coerce')

print("\nEstatísticas Arquivo 1 - Value:")
print(df1['Value'].describe())

print("\nEstatísticas Arquivo 2 - value:")
print(df2['value'].describe())

filtro = (df2['industry_name_ANZSIC'] == 'Manufacturing') & (df2['variable'] == 'Revenue')

df_filtrado = df2.loc[filtro]

serie_temporal = df_filtrado.groupby('year')['value'].sum()

plt.figure(figsize=(10,6))
plt.plot(serie_temporal.index, serie_temporal.values, marker='o')
plt.title('Evolução da Receita na Indústria de Manufatura (2024)')
plt.xlabel('Ano')
plt.ylabel('Receita')
plt.grid(True)
plt.show()
