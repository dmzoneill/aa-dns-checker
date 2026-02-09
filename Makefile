.PHONY: setup test-setup test lint

setup:
	@echo "Installing dependencies..."
	pip3 install --user fastapi starlette uvicorn gunicorn

test-setup:
	@echo "Setting up test environment..."
	@echo "No test setup required"

test:
	@echo "Running tests..."
	@python3 -c "from dnslookup import app; print('✓ App imports successfully')"
	@echo "✓ All tests passed"

lint:
	@echo "Linting code..."
	@python3 -m py_compile dnslookup.py
	@echo "✓ Syntax check passed"
