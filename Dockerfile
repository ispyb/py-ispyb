FROM frolvlad/alpine-python3
MAINTAINER Ivars Karpics <ivars.karpics@embl-hamburg.de>

ENV API_SERVER_HOME=/opt/www
WORKDIR "$API_SERVER_HOME"
COPY "./requirements.txt" "./"
COPY "./app/requirements.txt" "./app/"
COPY "./config.py" "./"
COPY "./tasks" "./tasks"
COPY "./ispyb_core_config_example.yml" "./ispyb_core_config.yml"

ARG INCLUDE_POSTGRESQL=false
ARG INCLUDE_UWSGI=false
ARG INCLUDE_MYSQL=true

RUN apk add --no-cache --virtual=.build_dependencies musl-dev gcc python3-dev libffi-dev linux-headers
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev
RUN cd /opt/www
RUN pip install --upgrade pip
RUN pip install -r tasks/requirements.txt

RUN invoke app.dependencies.install && \
    ( \
        if [ "$INCLUDE_POSTGRESQL" = 'true' ]; then \
            apk add --no-cache libpq && \
            apk add --no-cache --virtual=.build_dependencies postgresql-dev && \
            pip install psycopg2 ; \
        fi \
    ) && \
    ( if [ "$INCLUDE_UWSGI" = 'true' ]; then pip install uwsgi ; fi ) && \
    rm -rf ~/.cache/pip && \
    apk del .build_dependencies

COPY "./" "./"

RUN chown -R nobody "."

USER nobody
CMD ["invoke", "app.run", "--no-install-dependencies", "--host", "0.0.0.0" ]
