# Лабораторная работа №4

## Описание

Выполненная работа заключается в использовании системы версионирования данных dvc.

## Отчёт о функциональности

1. Проведён разведывательный анализ данных в `notebooks/data_analysis.ipynb`, в котором предложены решения для пропущенных данных, а так же проведён отбор важных признаков для предсказания.

2. Модуль `data_fetch.py` загружает данные, и сохраняет в csv файл. Далее эти сырые данные добавлены в dvc и загружены на gdrive. Hash git коммита - `02d0710`.

3. Модуль `data_fillnan.py` обрабатывает пропуски согласно разведывательному анализу. Потом сохраняет данные в новый отдельный csv файл. Далее эти данные добавлены в dvc и загружены на gdrive. Hash git коммита - `e8d80c8`.

4. Модуль `data_features.py` обрабатывает признаки согласно разведывательному анализу. Потом обновляет ранее созданные csv файл. Далее эти обработанные данные добавлены в dvc и загружены на gdrive. Hash git коммита - `ae01c56`.

## Изображения

![Screenshot 2024-05-08 233635](https://github.com/nymless/URFU/assets/86611399/e5f3fbb7-8bc8-4b2d-9c86-70d5c7780874)
![Screenshot 2024-05-10 174742](https://github.com/nymless/URFU/assets/86611399/a0951ded-c332-43cc-96ee-a03e9fb28fb3)
