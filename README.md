# Demo of Celery with Django showing progress
In this project I have tried to demonstrate use of celery with Django framework including showing progress of the request. I have used django-celery-results
and celery-progress packages for achieving the result.

## Setup
I have provided a requirements .txt file which include all the dependencies of the project. You can setup a virtual environment of use the global python context to install these packages. To use it, type

    pip install -r requirements.txt

After all the packages are installed, just run migrations and run server commands in django to run the project.

For generating migrations: 

    python manage.py makemigrations

For migration: 

    python manage.py migrate

Run Django server: 

    python manage.py runserver
