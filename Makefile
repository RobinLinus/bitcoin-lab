.PHONY: test validate index serve smoke compose-up compose-down

test:
	python3 -m unittest discover -s tests -v

validate:
	python3 -m lab.cli validate

index:
	python3 -m lab.cli index

serve:
	python3 -m lab.cli serve

smoke:
	python3 scripts/smoke_test.py

compose-up:
	docker compose up --build

compose-down:
	docker compose down

