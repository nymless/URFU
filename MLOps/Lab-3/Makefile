# Подготовка виртуального окружения
.PHONY: venv
venv:
	python3 -m venv ./.venv

# Установка указанных пакетов (когда отсутствует файл `requirements.txt`)
.PHONY: direct_deps
direct_deps: venv
	(. ./.venv/bin/activate; pip install scikit-learn streamlit)

# Установка пакетов указанных в `requirements.txt`
.PHONY: deps
deps: venv
	(. ./.venv/bin/activate; pip install -r requirements.txt)

# Удаление виртуального окружения
.PHONY: del_venv
del_venv:
	rm -R ./.venv

# Удаление всех пакетов из виртуального окружения`
.PHONY: del_deps
del_deps:
	(. ./.venv/bin/activate; pip freeze | xargs pip uninstall -y)

# Сохранение зависимостей в файл `requirements.txt`
.PHONY: freeze
freeze:
	(. ./.venv/bin/activate; pip freeze > requirements.txt)

# Запуск приложения
.PHONY: run
run:
	(export SCALER_PATH="./model/iris_scaler.pkl"; \
	export MODEL_PATH="./model/iris_model.pkl"; \
	. ./.venv/bin/activate; python3 src/train_model.py; \
	streamlit run src/app.py --server.port 8081)

# Контейнеризация Docker
.PHONY: docker
docker:
	docker compose up -d --build
