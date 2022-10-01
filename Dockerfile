from python:3.7


WORKDIR /usr/src/app

COPY src .

RUN pip install --no-cache-dir -r requirements.txt \
    apt-get update && apt-get install -y \
    imagemagick libmagickwand-dev --no-install-recommends