FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD flask run -h 0.0.0.0 -p $PORT
