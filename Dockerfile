FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install python3 python3-pip python-dev build-essential -y
COPY . /tmp
WORKDIR /tmp
RUN pip3 install --default-timeout=20 --no-cache-dir -r requirements.txt
ENV PORT 8080
CMD ["flask", "run", "--host", "0.0.0.0", "-p", "8080"]