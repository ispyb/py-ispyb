FROM frolvlad/alpine-python3

ENV API_SERVER_HOME=/opt/www
WORKDIR "$API_SERVER_HOME"
COPY "./requirements.txt" "./"
COPY "./app/requirements.txt" "./app/"
COPY "./config-template.py" "./config.py"

ARG INCLUDE_POSTGRESQL=false
ARG INCLUDE_UWSGI=false
RUN apk add --no-cache --virtual=.build_dependencies musl-dev gcc python3-dev libffi-dev linux-headers && \
    cd /opt/www && \
    pip install -r requirements.txt && \
    invoke app.dependencies.install && \
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
USER nobody
CMD [ "invoke", "app.run", "--no-install-dependencies", "--host", "0.0.0.0" ]
