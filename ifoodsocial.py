import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

arquivo = 'ifood.csv'
df = pd.read_csv(arquivo, encoding='latin1')

def extrair_estado_civil(row):
    if row['marital_Divorced'] == 1:
        return 'Divorciado'
    elif row['marital_Married'] == 1:
        return 'Casado'
    elif row['marital_Single'] == 1:
        return 'Solteiro'
    elif row['marital_Together'] == 1:
        return 'Juntado'
    elif row['marital_Widow'] == 1:
        return 'Viúvo'
    else:
        return 'Desconhecido'

df['estado_civil'] = df.apply(extrair_estado_civil, axis=1)

plt.figure(figsize=(10,6))
sns.boxplot(x='estado_civil', y='MntTotal', data=df, palette='Set3')
plt.title('Distribuição dos Gastos Totais por Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Gastos Totais')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
