# API de Prueba


docker compose build

docker compose up -d

docker compose exec web python manage.py migrate

docker compose exec web python manage.py createsuperuser
