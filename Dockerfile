FROM python:3.9.2

RUN pip3 install pipenv

ENV PROJECT_DIR /usr/src/flaskyieldapi

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

# CMD ["./run_app_prod.sh"]
CMD ["pipenv", "run", "python", "wsgi.py"]
