install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

clean:
	rm -r dist

package-update: clean build publish package-install

lint:
	poetry run flake8 brain_games
