FROM python:3.10.9

RUN apt-get update && apt-get install -y \
    libldap2-dev \
    libsasl2-dev \
    libmariadb-dev \
    build-essential

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY ./pyispyb /app/pyispyb/
COPY ./config/docker.env /app/config/docker.env
COPY ./uvicorn.sh /app/uvicorn.sh

ENV ISPYB_ENVIRONMENT="docker"


EXPOSE 80

CMD ["gunicorn",\
    "pyispyb.app.main:app",\
    "--workers", "5",\
    "--worker-class", "uvicorn.workers.UvicornWorker",\
    "--bind", "0.0.0.0:80"\
    ]
