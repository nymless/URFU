#!/bin/bash

# Выбор переменной python для Linux, MacOS и Windows по умолчанию.
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    python_var='python3'
elif [[ "$OSTYPE" == "darwin"* ]]; then
    python_var='python3'
elif [[ "$OSTYPE" == "cygwin" ]]; then
    python_var='python'
elif [[ "$OSTYPE" == "msys" ]]; then
    python_var='python'
elif [[ "$OSTYPE" == "win32" ]]; then
    python_var='python'
else
    python_var='python3'
fi

# Необходимые для ML пайплайна переменные окружения.
export TRAIN_PATH="${PWD}/train/train.csv"
export TEST_PATH="${PWD}/test/test.csv"
export TRAIN_PREP_PATH="${PWD}/train/train_prep.csv"
export TEST_PREP_PATH="${PWD}/test/test_prep.csv"
export MODEL_PATH="${PWD}/model/model.pkl"

# Запуск ML пайплайна.
$python_var ./data_creation.py
$python_var ./model_preprocessing.py
$python_var ./model_preparation.py
$python_var ./model_testing.py
