FROM ubuntu:24.04

EXPOSE 10001

RUN apt-get update && apt-get upgrade -y && apt-get update --fix-missing
RUN apt-get install -y python3 python3-venv python3-dev python3-pip

WORKDIR /hehe
COPY server.py .
COPY secret.py .

# securing the flag
RUN chmod 755 /hehe
RUN chmod 744 /hehe/secret.py

# securing the environment
RUN chmod 700 /tmp /dev/shm
RUN chmod 755 /usr/bin/env /usr/bin/python3 /bin/dash /bin/bash /bin/sh /bin/cat /usr/bin/groups /usr/bin/id /bin/ls

# add a less-privileged user
RUN useradd -ms /bin/bash ctfuser
USER ctfuser

# create a Python virtual environment & install dependencies
RUN python3 -m venv /home/ctfuser/venv
RUN /home/ctfuser/venv/bin/pip install --upgrade pip
RUN /home/ctfuser/venv/bin/pip install --no-cache-dir flask==3.1.1 openfhe==1.2.3.0.24.4

# env variables for Flask
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=10001

CMD ["/home/ctfuser/venv/bin/flask", "run"]
