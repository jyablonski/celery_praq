.PHONY: up
up:
	@docker-compose -f docker/docker-compose.yml up

.PHONY: down
down:
	@docker-compose -f docker/docker-compose.yml down