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
