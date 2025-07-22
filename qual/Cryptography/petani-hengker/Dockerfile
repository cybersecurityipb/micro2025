FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends socat && \
    rm -rf /var/lib/apt/lists/*

RUN useradd --no-create-home --shell /bin/false ctf

WORKDIR /app

COPY --chown=ctf:ctf requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=ctf:ctf chal.py ecc.py flag.txt .

USER ctf

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 /app/chal.py'"]