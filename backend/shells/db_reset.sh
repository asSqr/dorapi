#!/bin/bash

docker-compose down && docker volume rm dorapi_django_data_volume_v2 && docker-compose up -d && docker-compose exec backend python manage.py makemigrations && docker-compose exec backend python manage.py makemigrations dorapi && docker-compose exec backend python manage.py migrate && docker-compose exec backend /bin/bash -c "python ./manage.py shell < ./data/seed_entity.py"
