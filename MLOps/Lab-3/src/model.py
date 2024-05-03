import os
import pickle

from Iris import Iris
from sklearn.preprocessing import StandardScaler


def load_model():
    scaler_path = os.environ["SCALER_PATH"]
    model_path = os.environ["MODEL_PATH"]
    scaler = pickle.load(open(scaler_path, "rb"))
    model = pickle.load(open(model_path, "rb"))

    def predict_iris(iris: Iris):
        iris_tuple = iris.get_params()
        iris_ndarray = scaler.transform([iris_tuple])

        iris_label = model.predict(iris_ndarray)[0]
        iris_class = Iris.CLASSES[iris_label]
        
        return iris_class

    return predict_iris
