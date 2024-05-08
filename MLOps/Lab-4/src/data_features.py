import pandas as pd


# Загрузим данные в DataFrame
df = pd.read_csv("data/titanic_train_prep.csv")

# Реализуем тот отбор параметром, который предложен в разведывательном
# анализе данных notebooks/data_analysis.ipynb

# Удалим признак Ticket
df.drop("Ticket", inplace=True, axis=1)

# Сохраним артефакт
df.to_csv("data/titanic_train_prep.csv", index=False)
