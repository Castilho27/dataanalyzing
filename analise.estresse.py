import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("Stress_Dataset.csv")

mapa_genero = {0: "Feminino", 1: "Masculino"}
dados["Gender"] = dados["Gender"].map(mapa_genero)

plt.figure(figsize=(6,4))
sns.countplot(data=dados, x="Gender", palette="pastel")
plt.title("Distribuição por Gênero")
plt.xlabel("")
plt.ylabel("Quantidade")
plt.show()

