install:
	poetry install

test:
	poetry run pytest

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl


.PHONY: gendiff
