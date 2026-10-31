from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_moons
X, y = make_moons(n_samples=100, noise=0.2)
m = DecisionTreeClassifier()
m.fit(X, y)
print("Accuracy:", m.score(X, y))
