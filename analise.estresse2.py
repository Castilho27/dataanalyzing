import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dados = pd.read_csv("Stress_Dataset.csv")

def yes_no_to_binary(x):
    if isinstance(x, str):
        if x.strip().lower() == "yes":
            return 1
        elif x.strip().lower() == "no":
            return 0
    return x

dados = dados.applymap(yes_no_to_binary)

if "Have you been dealing with anxiety or tension recently?.1" in dados.columns:
    dados = dados.drop(columns=["Have you been dealing with anxiety or tension recently?.1"])

dados = dados.dropna(subset=["Which type of stress do you primarily experience?"])

X = dados.drop(columns=["Gender", "Age", "Which type of stress do you primarily experience?"])
y = dados["Which type of stress do you primarily experience?"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
modelo.fit(X_train, y_train)

plt.figure(figsize=(20,10))
plot_tree(modelo, feature_names=X.columns, class_names=modelo.classes_, filled=True, rounded=True, fontsize=10)
plt.title("Árvore de Decisão para Previsão do Tipo de Estresse")
plt.show()
