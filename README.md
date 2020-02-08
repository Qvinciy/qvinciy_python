# qvinciy_python

#### DATABASES

    /qvinciy/settings.py

    https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#### create admin

    python3 manage.py createsuperuser

#### START

    docker-compose up

##### OR

    docker-compose up -d --build
    
##### OR

    pip3 install -r requirements.txt

    python3 -m django --version

    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser

    python3 manage.py runserver

    
#### STOP

    docker-compose down