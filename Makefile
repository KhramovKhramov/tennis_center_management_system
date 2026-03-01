packages?=src

style:
	ruff format $(packages)
	ruff check --fix $(packages)

mypy:
	mypy $(packages)

check: style mypy