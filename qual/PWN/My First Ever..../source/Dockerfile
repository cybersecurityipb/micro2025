FROM ubuntu:22.04

RUN apt update
RUN apt install -y xinetd
RUN rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf

COPY flag.txt /flag.txt
WORKDIR /home/ctf

COPY chall chall
COPY xinetd.conf /etc/xinetd.d/chall

RUN chmod +x chall

EXPOSE 8000

CMD ["/usr/sbin/xinetd", "-dontfork"]
