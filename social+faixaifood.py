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

plt.figure(figsize=(12,7))
sns.set_style('whitegrid')
sns.set_palette('pastel')
sns.set_context('notebook', font_scale=1.2)

barplot = sns.barplot(
    data=media, 
    x='FaixaEtaria', 
    y='MntTotal', 
    hue='EstadoCivil', 
    dodge=True, 
    edgecolor='gray'
)

for container in barplot.containers:
    barplot.bar_label(container, fmt='R$ %.0f', label_type='edge', padding=2)

plt.title('💰 Gasto Médio Total por Faixa Etária e Estado Civil', fontsize=16, weight='bold', pad=20)
plt.xlabel('Faixa Etária', labelpad=10)
plt.ylabel('Gasto Médio (R$)', labelpad=10)
plt.legend(title='Estado Civil', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
