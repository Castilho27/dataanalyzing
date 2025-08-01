import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ifood.csv', encoding='latin1')

bins = [18, 30, 40, 50, 60, 100]
labels = ['18-29', '30-39', '40-49', '50-59', '60+']
df['Faixa_Etaria'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

media_gastos = df.groupby('Faixa_Etaria')['MntTotal'].mean().reset_index()

plt.figure(figsize=(8,6))
sns.barplot(data=media_gastos, x='Faixa_Etaria', y='MntTotal', palette='Blues_d')

plt.ylabel('Gasto Médio (R$)')
plt.xlabel('Faixa Etária')
plt.title('Gasto Médio Total por Faixa Etária')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
