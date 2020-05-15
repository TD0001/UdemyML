import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import  load_iris
iris_db = load_iris()
print(iris_db)
x = iris_db.data
y = iris_db.target

print(y)