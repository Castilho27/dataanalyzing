import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

df = pd.read_csv('ifood.csv', encoding='latin1')

bins = [18, 30, 40, 50, 60, 100]
labels = ['18-29', '30-39', '40-49', '50-59', '60+']
df['Faixa_Etaria'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

media_gastos = df.groupby('Faixa_Etaria')['MntTotal'].mean().reset_index()

plt.figure(figsize=(10,6))
sns.set_style('whitegrid')
palette = sns.color_palette('coolwarm', len(labels))
barplot = sns.barplot(data=media_gastos, x='Faixa_Etaria', y='MntTotal', palette=palette)

barplot.yaxis.set_major_formatter(mtick.StrMethodFormatter('R$ {x:,.0f}'))

for p in barplot.patches:
    height = p.get_height()
    barplot.annotate(f'R$ {height:,.0f}', 
                     (p.get_x() + p.get_width() / 2, height), 
                     ha='center', va='bottom',
                     fontsize=11,
                     fontweight='bold',
                     color='black',
                     xytext=(0,5),
                     textcoords='offset points')

plt.title('Gasto Médio Total por Faixa Etária', fontsize=16, fontweight='bold')
plt.xlabel('Faixa Etária', fontsize=14)
plt.ylabel('Gasto Médio (R$)', fontsize=14)
plt.ylim(0, media_gastos['MntTotal'].max() * 1.15)
plt.tight_layout()
plt.show()

