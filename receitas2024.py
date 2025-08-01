import pandas as pd
import matplotlib.pyplot as plt

arquivo2 = 'Pesquisa Anual de Empresas - Ano Fiscal de 2024.csv'
df2 = pd.read_csv(arquivo2)


df2['value'] = pd.to_numeric(df2['value'], errors='coerce')

filtro = (
    (df2['industry_name_ANZSIC'] == 'Manufacturing') &
    (df2['variable'] == 'Total income')
)

df_filtrado = df2.loc[filtro]

grupo_tamanho = df_filtrado.groupby('rme_size_grp')['value'].sum().sort_values()

if grupo_tamanho.empty:
    print("Nenhum dado encontrado para os critérios selecionados.")
else:
    plt.figure(figsize=(10,6))
    grupo_tamanho.plot(kind='barh', color='#4085B4')
    plt.title('Receita Total por Tamanho de Empresa\n(Indústria de Manufatura - 2024)')
    plt.xlabel('Receita Total')
    plt.ylabel('Grupo de Tamanho da Empresa')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()
