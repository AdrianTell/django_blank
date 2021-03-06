FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /calendar_api

WORKDIR /calendar_api

ADD . /calendar_api/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]