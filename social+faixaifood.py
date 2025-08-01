import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ifood.csv', encoding='latin1')
df['value'] = pd.to_numeric(df['MntTotal'], errors='coerce')

bins = [18, 30, 45, 60, 100]
labels = ['18-29', '30-44', '45-59', '60+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

mean_by_age = df.groupby('AgeGroup')['MntTotal'].mean()

def estado_civil(row):
    if row['marital_Married'] == 1:
        return 'Casado(a)'
    elif row['marital_Single'] == 1:
        return 'Solteiro(a)'
    else:
        return 'Outro'

df['EstadoCivil'] = df.apply(estado_civil, axis=1)
mean_by_civil = df.groupby('EstadoCivil')['MntTotal'].mean()

fig, ax1 = plt.subplots(figsize=(10,6))

bars = ax1.bar(mean_by_age.index.astype(str), mean_by_age.values, color='#55ACE7', alpha=0.7)
ax1.set_xlabel('Faixa Etária')
ax1.set_ylabel('Gasto Médio (R$)')
ax1.set_title('Gasto Médio Total: Faixa Etária e Estado Civil')

ax2 = ax1.twinx()

ax2.plot(mean_by_civil.index, mean_by_civil.values, color='#E64A19', marker='o', linewidth=3, label='Estado Civil')

ax2.set_ylabel('Gasto Médio (R$) por Estado Civil')

ax2.legend(loc='upper right')

plt.show()
