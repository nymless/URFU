import pandas as pd
from catboost.datasets import titanic

titanic_train, titanic_test = titanic()
titanic_train.to_csv("./data/titanic_train.csv", index=False)
