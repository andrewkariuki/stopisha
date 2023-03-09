.EXPORT_ALL_VARIABLES:
.PHONY: install-poetry create-missing-files publish requirements docs develop clean

setup: install-poetry install create-missing-files

current: install create-missing-files

create-missing-files:
	@echo "Create missing directories and files..."
	mkdir -p volumes/logs
	mkdir -p volumes/data

install-poetry:
	@echo "Installing poetry..."
	python -m pip install --upgrade pip
	pip install poetry

install:
	@echo "Installing dependencies..."
	poetry install --no-root --sync
	
publish:
	@echo "Versioning and publishing package..."
	poetry run semantic-release version
	git add .
	git commit -m "chore(release): release stopisha"
	git push --follow-tags

requirements:
	@echo "Generating requirements.txt..."
	poetry export --without-hashes --format=requirements.txt > requirements.txt

docs:
	@echo "Generating documentation..."
	poetry run sphinx-build -b html docs/source/ docs/build/html

develop:
	@echo "Initializing development environment..."
	docker-compose up -d --build

clean:
	@echo "Setting up pre-commit..."
	if exist .\\.git\\hooks ( rmdir .\\.git\\hooks /q /s )
	if exist .\\.venv\\ ( rmdir .\\.venv /q /s )
	if exist poetry.lock ( del poetry.lock /q /s )