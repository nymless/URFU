import os

import numpy as np
import pandas as pd


def create_data(data_size, noise_power):
    """Creating a dataset of five features and a target feature
    that is some function of the original features."""

    # Генерация исходных признаков, распределённых по различным законам.
    features = [
        np.random.normal(1, 2, data_size),
        np.random.lognormal(0, 0.4, data_size),
        np.random.exponential(2, data_size),
        np.random.binomial(10, 0.5, data_size),
        np.random.geometric(0.5, data_size),
    ]

    # Генерация целевого признака, как некоторой функции от исходных признаков.
    target = (
        1.5 * features[0]
        + 2 * np.exp(features[1])
        + 3.2 * np.log(features[2])
        + 0.2 * features[3] ** 2
        + 1.9 * np.sqrt(features[4])
    )

    # Добавление шумов исходным признакам.
    for index, feature in enumerate(features):
        noises = np.random.randn(data_size) * noise_power
        features[index] = feature + noises

    # Создание датасета из всех признаков.
    features.append(target)
    data = np.stack(features, axis=1)

    print("The data has been created.")

    return data


def create_directories(train_path, test_path):
    """Creating directories to save datasets."""

    # Создание директории train
    train_dir = os.path.dirname(train_path)
    if not os.path.isdir(train_dir):
        os.mkdir(train_dir)

    # Создание директории test
    test_dir = os.path.dirname(test_path)
    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)

    print("Directories have been created.")


def save_data(data, columns, train_path, test_path):
    """Saving datasets in CSV files."""

    # Создание Pandas DataFrame для работы с данными
    df = pd.DataFrame(data, columns=columns)

    # Разделение на тренировочные данные 80% и тестовые 20%
    split_index = int(len(df) * 0.8)
    train = df[:split_index]
    test = df[split_index:]

    # Сохранение train.csv
    train.to_csv(train_path, index=False)

    # Сохранение test.csv
    test.to_csv(test_path, index=False)

    print("The datasets have been saved.")


# Наименование признаков и целевого признака - "Дневная температура".
columns = [
    "Feature_1",
    "Feature_2",
    "Feature_3",
    "Feature_4",
    "Feature_5",
    "Daily_Temperature",
]

# Размер данных и сила шума.
data_size = 10000
noise_power = 0.05

train_path = os.environ["TRAIN_PATH"]
test_path = os.environ["TEST_PATH"]

data = create_data(data_size, noise_power)
create_directories(train_path, test_path)
save_data(data, columns, train_path, test_path)
