FROM python:3.9.5-alpine3.13
RUN mkdir service
WORKDIR service
COPY requirements.txt requirements.txt
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
RUN rm requirements.txt
COPY user_server.py user_server.py
CMD ["python3", "user_server.py"]