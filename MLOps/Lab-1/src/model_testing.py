import os
import pickle

import pandas as pd
from sklearn.metrics import r2_score


def load_model(model_path):
    """Loading a model from the pickle file."""

    model = pickle.load(open(model_path, "rb"))

    print("The model has been loaded.")

    return model


def test_model(model, test_prep_path):
    """Model testing by R2 score (coefficient of determination)."""

    test_df = pd.read_csv(test_prep_path)

    X_test = test_df.drop(columns=["Daily_Temperature"])
    y_test = test_df["Daily_Temperature"]

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)

    print("The model has been tested.")

    return r2


# Читаем пути из переменных окружения.
test_prep_path = os.environ["TEST_PREP_PATH"]
model_path = os.environ["MODEL_PATH"]

model = load_model(model_path)
r2 = test_model(model, test_prep_path)

print("=====================================")
print("Model R2 score is:", r2)
print("ML pipeline execution is complete.")
