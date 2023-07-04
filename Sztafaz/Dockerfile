FROM python:3
RUN mkdir -p /project/
WORKDIR /project
COPY requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/
