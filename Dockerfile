# Use an official Python runtime as a parent image
FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
EXPOSE 4000
CMD python ./app/app.py