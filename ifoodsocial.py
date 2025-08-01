import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ifood.csv', encoding='latin1')

def estado_civil(row):
    if row['marital_Divorced'] == 1:
        return 'Divorciado'
    elif row['marital_Married'] == 1:
        return 'Casado'
    elif row['marital_Single'] == 1:
        return 'Solteiro'
    elif row['marital_Together'] == 1:
        return 'Namorando/Juntos'
    elif row['marital_Widow'] == 1:
        return 'Viúvo'
    else:
        return 'Desconhecido'

df['estado_civil'] = df.apply(estado_civil, axis=1)

plt.figure(figsize=(10,6))
sns.boxplot(x='estado_civil', y='MntTotal', data=df, palette='pastel')

plt.title('Gastos Totais por Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Gastos Totais (R$)')

plt.xticks(rotation=30)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

formatter = plt.FuncFormatter(lambda x, _: f'R$ {x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.show()
