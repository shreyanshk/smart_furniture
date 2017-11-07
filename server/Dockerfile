FROM alpine:3.6
RUN apk update
RUN apk add --no-cache python3 py-psycopg2 &&\
    pip3 install chaperone
ADD requirements.txt /
RUN pip3 install -r /requirements.txt
ADD . /app/
WORKDIR /app
EXPOSE 5000
ENV FLASK_APP run:app
ENTRYPOINT ["/usr/bin/python3", "-m", "flask", "run", "--host=0.0.0.0"]
