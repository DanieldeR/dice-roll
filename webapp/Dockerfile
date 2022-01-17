FROM python:3.9-slim-buster

ENV AM_I_IN_DOCKER="yes"

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
