FROM python:3.9-slim

WORKDIR /app
COPY . /app 

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip3 install -r requirements.txt 

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_store/health 

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]