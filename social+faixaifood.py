import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ifood.csv', encoding='latin1')
df['MntTotal'] = pd.to_numeric(df['MntTotal'], errors='coerce')

bins = [18, 30, 45, 60, 100]
labels = ['18-29', '30-44', '45-59', '60+']
df['FaixaEtaria'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

def estado_civil(row):
    if row['marital_Married'] == 1:
        return 'Casado(a)'
    elif row['marital_Single'] == 1:
        return 'Solteiro(a)'
    else:
        return 'Outro'

df['EstadoCivil'] = df.apply(estado_civil, axis=1)

media = df.groupby(['FaixaEtaria', 'EstadoCivil'])['MntTotal'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.barplot(data=media, x='FaixaEtaria', y='MntTotal', hue='EstadoCivil', palette='Set2')

plt.title('Gasto Médio Total por Faixa Etária e Estado Civil')
plt.xlabel('Faixa Etária')
plt.ylabel('Gasto Médio (R$)')
plt.legend(title='Estado Civil')
plt.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.show()

