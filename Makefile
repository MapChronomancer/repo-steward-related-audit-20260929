.PHONY: install test lint clean run

install:
	pip install -e . pytest

test:
	pytest -q

lint:
	python -m compileall -q src

run:
	python -m repo_steward_related_audit_20260929

clean:
	rm -rf build dist *.egg-info __pycache__
