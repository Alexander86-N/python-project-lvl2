install:
	poetry install

gendiff:
	poetry run gendif -h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
