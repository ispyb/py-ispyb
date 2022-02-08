FROM python:3.8.10

RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
COPY ./pyispyb/requirements.txt ./pyispyb/requirements.txt
COPY ./tests/requirements.txt ./tests/requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY ./pyispyb /app/pyispyb/
COPY ./app.py /app/app.py

EXPOSE 80

RUN mkdir -p /var/log/pyispyb/

CMD ["gunicorn",\
    "-b", "0.0.0.0:80",\
    "--access-logfile", "/var/log/pyispyb/gunicorn-access.log",\
    "--error-logfile", "/var/log/pyispyb/gunicorn-error.log",\
    "app:app"\
    ]
