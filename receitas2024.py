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


rotulos_amigaveis = {
    'a_0': 'Sem funcionários',
    'b_1-5': '1 a 5',
    'c_6-9': '6 a 9',
    'd_10-19': '10 a 19',
    'e_20-49': '20 a 49',
    'f_50-99': '50 a 99',
    'g_100-199': '100 a 199',
    'h_200+': '200+'
}
df_filtrado['rme_size_grp'] = df_filtrado['rme_size_grp'].map(rotulos_amigaveis)


grupo_tamanho = df_filtrado.groupby('rme_size_grp')['value'].sum().reindex(rotulos_amigaveis.values())

plt.figure(figsize=(10,6), facecolor='#F9FAFB')  # fundo off-white
bars = plt.barh(
    grupo_tamanho.index,
    grupo_tamanho.values,
    color='#55ACE7',
    edgecolor='none'
)


plt.title('Receita Total por Tamanho de Empresa\nIndústria de Manufatura - 2024', fontsize=14, color='#2D6083', weight='bold')
plt.xlabel('Receita Total (em milhões)', fontsize=12, color='#1F2937')
plt.ylabel('Tamanho da Empresa', fontsize=12, color='#1F2937')

plt.grid(axis='x', color='#D1D5DB', linestyle='--', linewidth=0.7)
plt.tick_params(axis='both', labelsize=10, colors='#1F2937')
plt.gca().set_facecolor('#F9FAFB')  # fundo do gráfico
plt.tight_layout()

for bar in bars:
    plt.text(
        bar.get_width() + max(grupo_tamanho.values) * 0.01,  # deslocamento
        bar.get_y() + bar.get_height()/2,
        f'{bar.get_width():,.0f}',
        va='center',
        fontsize=9,
        color='#1F2937'
    )

plt.show()

