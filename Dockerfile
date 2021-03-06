FROM python:latest

RUN mkdir /code
COPY ./requirements.txt /code/
WORKDIR /code

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /code/

ENV GUNICORN_CMD_ARGS "--bind=0.0.0.0:8000 --workers=2 --thread=4 --worker-class=gthread --forwarded-allow-ips='*' --access-logfile -"

CMD ["gunicorn","app:app"]

EXPOSE 8000
