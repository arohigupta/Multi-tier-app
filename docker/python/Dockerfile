FROM python:3.5
MAINTAINER agupta@juniper.net
COPY ./myshop /myshop
WORKDIR /myshop
RUN pip install -r requirements.pip
CMD ["python","manage.py", "runserver","0.0.0.0:8000"]
