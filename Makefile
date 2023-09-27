run:
	python manage.py runserver

mig:
	python manage.py makemigrations
	python manage.py migrate

user:
	python manage.py createsuperuser

django:
	pip install django

drf:
	pip install djangorestframework

proj:
	django-admin startproject config .

app:
	django-admin startapp default