import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("Stress_Dataset.csv")

plt.figure(figsize=(6,4))
sns.countplot(data=dados, x="Gender", palette="pastel")
plt.title("Distribuição por Gênero")
plt.xlabel("")
plt.ylabel("Quantidade")
plt.show()

