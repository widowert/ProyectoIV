FROM python:3-alpine

MAINTAINER Oscar Osorio <oog3996@gmail.com>

WORKDIR /usr/src/app

COPY /src /test /data /app.py /requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD gunicorn app:app --bind 0.0.0.0:80

