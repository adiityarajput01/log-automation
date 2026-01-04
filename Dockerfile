#dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install boto3

CMD ["python","log_uploader.py"]
