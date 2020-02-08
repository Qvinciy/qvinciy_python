FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "makemigrations" ]
CMD [ "python3", "manage.py", "migrate"  ]
CMD [ "python3", "manage.py", "runserver"  ]

EXPOSE 8000
EXPOSE 5432