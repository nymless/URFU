import pandas as pd


# Загрузим данные в DataFrame
df = pd.read_csv("data/titanic_train.csv")

# Реализуем ту работу с пропусками, которая была предложена в разведывательном
# анализе данных notebooks/data_analysis.ipynb

# Пропуски в Cabin
mask_3 = df["Pclass"] == 3
mask_2 = df["Pclass"] == 2
mask_1 = df["Pclass"] == 1

df[mask_3] = df[mask_3].fillna({"Cabin": "NoCabin"})
df[mask_2] = df[mask_2].fillna({"Cabin": "NoCabin"})
df[mask_1] = df[mask_1].fillna({"Cabin": "UnknownCabin"})

# Пропуски в Age
mask_male = df["Sex"] == "male"
mask_female = df["Sex"] == "female"

male_age = df[mask_male]["Age"].median()
female_age = df[mask_female]["Age"].median()

df[mask_male] = df[mask_male].fillna({"Age": male_age})
df[mask_female] = df[mask_female].fillna({"Age": female_age})

# Пропуски в Embarked
df["Embarked"] = df["Embarked"].fillna("S")

# Сохраним артефакт
df.to_csv("data/titanic_train_prep.csv", index=False)
