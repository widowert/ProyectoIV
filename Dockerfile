FROM python:3

MAINTAINER Oscar Osorio <oog3996@gmail.com>

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "app:app" ]

EXPOSE 80
