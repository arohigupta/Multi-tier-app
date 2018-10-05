FROM python:3.5
MAINTAINER agupta@juniper.net
COPY ./myshop /myshop
WORKDIR /myshop
RUN pip install -r requirements.pip
CMD ["celery", "-A", "myshop", "worker","-l","info"]
