FROM ubuntu:20.04

WORKDIR /
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

COPY . .
RUN pip3 install psutil

ENTRYPOINT ["python3", "copy_workload.py"]