# flask-yield-api

The aim of this project is to implement a flask restful API as an exercise.

## Install with pipenv

``` shell
pipenv install --deploy --ignore-pipfile
```

## Run with pipenv


``` shell
pipenv run python wsgi.py
```


## Install with docker

``` shell
docker-compose build
docker-compose up -d
```

## Start docker container


``` shell
docker run -p 5000:5000 --name FlaslYieldAPI flask-yield-api_web
```
