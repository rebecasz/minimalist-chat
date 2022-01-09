# pull official base image
FROM python:3.9.6-alpine

# set work directory
#WORKDIR /usr/src/app
WORKDIR /appnew
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .
CMD ["python3","manage.py", "runserver","0.0.0.0:8000"]

