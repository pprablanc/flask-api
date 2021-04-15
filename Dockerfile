FROM python:3.8

RUN pip3 install pipenv

ENV PROJECT_DIR /usr/src/flaskyieldapi
ENV FLASK_APP=./launch_app.py

WORKDIR ${PROJECT_DIR}

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["./run_app.sh"]
