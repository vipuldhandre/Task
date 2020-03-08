
for Linux:

1) first create virtualenv by typing following command:
	virtualenv -p python3.6 venv_ass1

2) activate virtualenv by typing following command:
	. venv_ass1/bin/activate

3) install requirements:
	pip install -r docs/requirements.txt

4) make migrations by following command:
	python manage.py makemigrations

5) migrate by following command:
	python manage.py migrate

6) create superuser: 
	python manage.py createsuperuser

7) runserver:
	python manage.py runserver


