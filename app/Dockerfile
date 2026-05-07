FROM 10.6.0.190:80/proxy/python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]