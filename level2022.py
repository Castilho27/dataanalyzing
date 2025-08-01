import pandas as pd
import matplotlib.pyplot as plt

arquivo_2022 = 'Pesquisa de Operações Empresariais 2022 - Finanças Empresariais.csv'

df = pd.read_csv(arquivo_2022, encoding='latin1')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Escolha a descrição que quer analisar
descricao_escolhida = 'Type of outstanding debt: bank overdrafts'

df_foco = df[df['description'] == descricao_escolhida]

# Agrupar por setor econômico e somar valores
grupo_industry = df_foco.groupby('industry')['value'].sum().sort_values(ascending=False)

# Se quiser, pegar os top 10 setores + agrupamento do resto
top_n = 10
top_industry = grupo_industry.head(top_n)
outros = grupo_industry[top_n:].sum()
top_industry['Outros'] = outros

# Gráfico de pizza
plt.figure(figsize=(8,8))
cores = plt.get_cmap('Set3').colors
plt.pie(top_industry, labels=top_industry.index, autopct='%1.1f%%', startangle=140, colors=cores)
plt.title(f'Dívida de Cheque Especial por Setor Econômico')
plt.axis('equal')
plt.tight_layout()
plt.show()

