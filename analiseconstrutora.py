import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

df = pd.read_csv("construtoras.csv")

df['Vendidos'] = df['Vendidos'].map({'Sim': 1, 'Não': 0})

X = df[['Número de Torres', 'Vendidos', 'Preço']]
y = df['Construtora']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"Acurácia da árvore de decisão: {accuracy*100:.2f}%")

import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
tree.plot_tree(clf, feature_names=X.columns, class_names=df['Construtora'].unique(), filled=True)
plt.show()

exemplo = pd.DataFrame({
    'Número de Torres': [4],
    'Vendidos': [0],
    'Preço': [500000]
})
predicao = clf.predict(exemplo)
print(f"Construtora recomendada: {predicao[0]}")
