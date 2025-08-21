import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\luber\OneDrive\Documentos\Estudos\Dados\construtoras.csv")
df['Vendidos'] = df['Vendidos'].map({'Sim': 1, 'Não': 0})
preco_medio = df.groupby('Construtora')['Preço'].mean().sort_values()
plt.figure(figsize=(10,6))
sns.barplot(x=preco_medio.index, y=preco_medio.values, palette="Blues_d")
plt.title("Preço médio por Construtora")
plt.ylabel("Preço médio (R$)")
plt.xlabel("Construtora")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10,6))
sns.barplot(x='Construtora', y='Número de Torres', hue='Vendidos', data=df, palette=['red','green'])
plt.title("Número de Torres e status de venda por Construtora")
plt.ylabel("Número de Torres")
plt.xlabel("Construtora")
plt.xticks(rotation=45)
plt.legend(title='Vendido', labels=['Não', 'Sim'])
plt.show()
