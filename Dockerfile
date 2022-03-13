FROM python:3.8.10
WORKDIR /home/mddn41/isp-first
COPY . .
ENTRYPOINT [ "python", "./entry.py" ]
