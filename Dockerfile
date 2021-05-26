FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install python3 python3-pip python-dev build-essential -y
COPY . /tmp
WORKDIR /tmp
RUN tar -xzf CRF++-0.58.tar.gz
RUN cd CRF++-0.58 && ./configure && make && make install && ldconfig
RUN LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib && export LD_LIBRARY_PATH
RUN pip3 install --default-timeout=20 --no-cache-dir -r requirements.txt
ENV PORT 8080
CMD ["flask", "run", "--host", "0.0.0.0", "-p", "8080"]