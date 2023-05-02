FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    git \
    && pip install pytest coverage

COPY uno.py tests_uno.py random_game.py /images/ /uno/

WORKDIR /uno

CMD ["python", "random_game.py"]
