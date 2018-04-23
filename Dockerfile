FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
EXPOSE 8005
ENTRYPOINT ["python", "app.py"]