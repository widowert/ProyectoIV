FROM python:3

MAINTAINER Oscar Osorio <oog3996@gmail.com>

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD gunicorn app:app --logfile=- --bind 0.0.0.0:80

