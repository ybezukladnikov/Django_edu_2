FROM python:3.9.16-alpine3.18
#FROM python:3

#Инструкция WORKDIR задаёт рабочую папку приложения.
#Все инструкции в Dockerfile будут выполняться относительно неё.
#
#Устанавливать рабочую папку — хороший тон. Она позволяет явно
#указать место, где будет происходить вся работа. Добавим её в нашу конфигурацию:
WORKDIR /app/

COPY Pipfile  /app
COPY Pipfile.lock /app

# PYTHONUNBUFFERED отвечает за отключение буферизации вывода (output).
#То есть непустое значение данной переменной среды гарантирует,
#что мы можем видеть выходные данные нашего приложения в
#режиме реального времени.
ENV PYTHONUNBUFFERED 1

#PYTHONDONTWRITEBYTECODE означает,
#что Python не будет пытаться создавать файлы .pyc
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install pipenv \
    && pipenv requirements > requirements.txt \
    && pip install -r requirements.txt

COPY . /app

#EXPOSE 8000
#WORKDIR /app/coolsite
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
