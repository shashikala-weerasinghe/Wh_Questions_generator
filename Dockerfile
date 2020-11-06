FROM python:3.7-alpine

RUN apk add --update \
    build-base \
    openjdk8-jre \
    bash \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /app

COPY api .

COPY requirements.txt requirements.txt

RUN apk add --update supervisor dos2unix

RUN dos2unix QuestionGeneration/runSSTServer.sh \
    && dos2unix QuestionGeneration/runStanfordParserServer.sh

RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf ~/.cache/pip

RUN spacy download en

COPY supervisord.conf supervisord.conf

CMD ["supervisord", "-c", "supervisord.conf"]

