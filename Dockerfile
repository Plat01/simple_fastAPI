FROM python:3.10-slim
LABEL authors="plat01"

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN sudo chmod +x ./docker-scripts/wait-for-db.sh

# Create a user to run the app
#ARG USER_NAME=defaultusername
#RUN addgroup --system $USER_NAME && adduser --system --group $USER_NAME
#USER $USER_NAME

CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
