FROM tiangolo/uwsgi-nginx:python3.8

RUN pip3.8 install pipenv

ENV PROJECT_DIR /usr/src/flaskyieldapi

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

CMD ["pipenv", "run", "python", "wsgi.py"]
