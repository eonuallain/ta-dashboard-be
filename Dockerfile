FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=ta

WORKDIR /app
COPY requirements.txt .

RUN apk update 
RUN apk add libpq-dev gcc musl-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN ls -l
COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
