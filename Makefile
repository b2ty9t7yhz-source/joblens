run:
	python -m uvicorn app.main:app --reload

test:
	python -m pytest -q

docker-build:
	docker build -t internship-application-tracker .

docker-run:
	docker run -p 8000:8000 internship-application-tracker

docker-compose-up:
	docker compose up --build

docker-compose-down:
	docker compose down
