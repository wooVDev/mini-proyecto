FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y git

WORKDIR /app

CMD sh -c "\
    rm -rf /app/* && \
    git clone https://github.com/wooVDev/mini-proyecto.git /app && \
    pip install -r requirements.txt && \
    python manage.py migrate && \
    python manage.py runserver localhost:8000 \
"
