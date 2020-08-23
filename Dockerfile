FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /AyomiWork

WORKDIR /AyomiWork

ADD . /AyomiWork/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]