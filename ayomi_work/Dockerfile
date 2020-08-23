FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /ayomi_work

WORKDIR /ayomi_work

ADD . /ayomi_work/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]