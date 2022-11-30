FROM python:3.9

# Path: DockerFile
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]

