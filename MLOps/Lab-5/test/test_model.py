import pickle

import pandas as pd
from sklearn.metrics import r2_score


def test_model():
    x_new = pd.read_csv("data/x_new.csv")
    y_new = pd.read_csv("data/y_new.csv")
    model = pickle.load(open("model/model.pkl", "rb"))
    
    with open("model/score.txt", "r") as f:
        score = float(f.read())

    y_pred = model.predict(x_new)
    r2 = r2_score(y_new, y_pred)
    
    score = 0.95 * score
    assert r2 >= score
