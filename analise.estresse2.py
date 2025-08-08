import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dados = pd.read_csv("Stress_Dataset.csv")

def yes_no_to_binary(valor):
    if isinstance(valor, str):
        valor_limpo = valor.strip().lower()
        if valor_limpo == "yes":
            return 1
        elif valor_limpo == "no":
            return 0
    return valor

dados = dados.applymap(yes_no_to_binary)

coluna_remover = "Have you been dealing with anxiety or tension recently?.1"
if coluna_remover in dados.columns:
    dados = dados.drop(columns=[coluna_remover])

coluna_alvo = "Which type of stress do you primarily experience?"
dados = dados.dropna(subset=[coluna_alvo])


colunas_excluir = ["Gender", "Age", coluna_alvo]
X = dados.drop(columns=colunas_excluir)
y = dados[coluna_alvo]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
modelo.fit(X_train, y_train)


plt.figure(figsize=(20, 10))
plot_tree(
    modelo, 
    feature_names=X.columns, 
    class_names=modelo.classes_, 
    filled=True, 
    rounded=True, 
    fontsize=10
)
plt.title("Árvore de Decisão para Previsão do Tipo de Estresse")
plt.show()
