FROM python:3.10 AS builder
COPY challenge/requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools wheel
RUN pip install --user -r requirements.txt

FROM python:3.10-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY --from=builder /root/.local /root/.local

COPY challenge /app/challenge
ADD manage.py /app
ADD pyproject.toml /app

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
