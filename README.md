# qvinciy_python

### DATABASES

    /qvinciy/settings.py

    https://docs.djangoproject.com/en/1.10/ref/settings/#databases
    
##### if start 127.0.0.1
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'qvinciy',
        'USER': 'qvinciy',
        'PASSWORD': 'qvinciy',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

##### if start docker-compose

    https://docs.docker.com/install
    https://docs.docker.com/compose/install/
    
``` 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'qvinciy',
        'USER': 'qvinciy',
        'PASSWORD': 'qvinciy',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

### create admin

    python3 manage.py createsuperuser

### START
    git clone https://github.com/Qvinciy/qvinciy_python
    cd qvinciy_python
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

    
### STOP

    docker-compose down