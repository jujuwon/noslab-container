FROM ubuntu:20.04

WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY . .
RUN pip3 install tensorflow
RUN pip3 install psutil

CMD ["python3", "dp.py"]


