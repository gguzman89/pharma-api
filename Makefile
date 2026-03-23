#vars
PYTHON = python
ENV_DEV = ENV=development
ENV_PROD = ENV=production

.PHONY: development production test install clean

install:
		pip install -r requirements.txt

dev:
		$(ENV_DEV) $(PYTHON) run.py

prod:
		$(ENV_PROD) $(PYTHON) run.py

test:
		pytest

clean:
		find . -type d -name "__pycache__" -exac rm -rf {} +
		rm -rf .pytest_cache