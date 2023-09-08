FROM python:3.10

WORKDIR /app

COPY ./src /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["uvicorn", "main.app", "-host", "0.0.0.0", "--port", "8000"]