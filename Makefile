TAIL=100

packages?=src

define set-default-container
	ifndef c
	c = backend
	else ifeq (${c},all)
	override c=
	endif
endef

set-container:
	$(eval $(call set-default-container))

build:
	docker compose build
full-build:
	docker compose build --no-cache
up:
	docker compose up -d
stop:
	docker compose stop
down:
	docker compose down
logs: set-container
	docker compose logs --tail=$(TAIL) -f $(c)
exec: set-container
	docker compose exec $(c) /bin/bash

style:
	ruff format $(packages)
	ruff check --fix $(packages)

mypy:
	mypy $(packages)

check: style mypy

create-migration: set-container
	docker compose exec $(c) /bin/bash -c 'alembic revision --autogenerate -m $(name)'

migrations: set-container
	docker compose exec $(c) /bin/bash -c 'alembic upgrade head'