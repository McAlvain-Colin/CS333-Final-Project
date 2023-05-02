FROM python:3.9-slim-buster


RUN apt-get update && \
    apt-get install -y \
    build-essential \
    git

COPY . /uno

WORKDIR /uno

CMD ["python", "uno/random_game.py"]