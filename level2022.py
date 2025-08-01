import pandas as pd
import matplotlib.pyplot as plt

arquivo_2022 = 'Pesquisa de Operações Empresariais 2022 - Finanças Empresariais.csv'

df = pd.read_csv(arquivo_2022, encoding='latin1')

# Garantir que 'value' seja numérico
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Filtrar só um tipo específico de description
filtro = df['description'] == 'Type of outstanding debt: bank overdrafts'
df_filtrado = df.loc[filtro]

# Criar a coluna combinada Industry + Size
df_filtrado['combinado'] = df_filtrado['industry'].astype(str) + ' | ' + df_filtrado['size'].astype(str)

# Agrupar e somar valores
grupo = df_filtrado.groupby('combinado')['value'].sum().sort_values(ascending=False)

# Pegar os top 10 e somar o resto como "Outros"
top_n = 10
top_grupo = grupo.head(top_n)
outros = grupo[top_n:].sum()
top_grupo['Outros'] = outros

# Gráfico de pizza
plt.figure(figsize=(10,10))
cores = plt.get_cmap('Set3').colors
plt.pie(top_grupo, labels=top_grupo.index, autopct='%1.1f%%', startangle=140, colors=cores)
plt.title('Distribuição de "Bank Overdrafts" por Setor e Porte')
plt.axis('equal')
plt.tight_layout()
plt.show()

