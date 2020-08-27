FROM frolvlad/alpine-python3

ENV API_SERVER_HOME=/opt/www
WORKDIR "$API_SERVER_HOME"
COPY "./requirements.txt" "./"
COPY "./app/requirements.txt" "./app/"
COPY "./ispyb_core_config.py" "./ispyb_core_config.py"
COPY "./ispyb_ssx_config.py" "./ispyb_ssx_config.py"

ARG INCLUDE_POSTGRESQL=false
ARG INCLUDE_UWSGI=false
RUN apk add --no-cache --virtual=.build_dependencies musl-dev gcc python3-dev libffi-dev linux-headers && \
    cd /opt/www && \
    pip install -r requirements.txt && \
    rm -rf ~/.cache/pip && \
    apk del .build_dependencies

COPY "./" "./"
USER nobody
CMD [ "app.run", "--no-install-dependencies", "--host", "0.0.0.0" ]
