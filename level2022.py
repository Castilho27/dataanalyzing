import pandas as pd
import matplotlib.pyplot as plt

arquivo_2022 = 'Pesquisa de Operações Empresariais 2022 - Finanças Empresariais.csv'

df = pd.read_csv(arquivo_2022, encoding='latin1')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

descricao_escolhida = 'Type of outstanding debt: bank overdrafts'
df_foco = df[df['description'] == descricao_escolhida]

grupo_industry = df_foco.groupby('industry')['value'].sum().sort_values(ascending=False)

top_n = 10
top_industry = grupo_industry.head(top_n)
outros = grupo_industry[top_n:].sum()
top_industry['Outros'] = outros

plt.figure(figsize=(10,10))
cores = plt.get_cmap('Set3').colors

def func(pct, allvals):
    absolute = int(pct/100.*sum(allvals))
    return f'{pct:.1f}%\n({absolute:,})' if pct > 3 else ''  

wedges, texts, autotexts = plt.pie(
    top_industry,
    labels=None,  
    autopct=lambda pct: func(pct, top_industry),
    startangle=140,
    colors=cores,
    pctdistance=0.75,
    labeldistance=1.1,
    wedgeprops=dict(width=0.4, edgecolor='w')
)

plt.title(f'Dívida de Cheque Especial por Setor Econômico')
plt.axis('equal')

plt.legend(wedges, top_industry.index, title="Setores", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()


