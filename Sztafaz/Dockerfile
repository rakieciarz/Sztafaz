FROM python:3
RUN mkdir -r /Project/
WORKDIR /Project
COPY requirements.txt /Project/
RUN pip install -r requirements.txt
COPY . /Project/
