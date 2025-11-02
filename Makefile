TAIL=100

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
	docker compose -f docker-compose.yaml build
full-build:
	docker compose -f docker-compose.yaml build --no-cache
up:
	docker compose -f docker-compose.yaml up -d
stop:
	docker compose -f docker-compose.yaml stop
down:
	docker compose -f docker-compose.yaml down
logs: set-container
	docker compose -f docker-compose.yaml logs --tail=$(TAIL) -f $(c)
exec: set-container
	docker compose -f docker-compose.yaml exec $(c) /bin/bash
shell: set-container
	docker compose -f docker-compose.yaml exec $(c) /bin/bash -c 'python /app/src/manage.py shell'
migrate: set-container
	docker compose -f docker-compose.yaml exec $(c) /bin/bash -c 'python /app/src/manage.py migrate'
migrations: set-container
	docker compose -f docker-compose.yaml exec $(c) /bin/bash -c 'python /app/src/manage.py makemigrations'
tests: set-container
	docker compose -f docker-compose.yaml exec $(c) /bin/bash -c 'cd /app && pytest -vvs'

