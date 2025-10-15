FROM python:3.8-slim-buster

WORKDIR /app
COPY . /app
RUN pip install -r requiremets.txt
CMD ["python", "app.py"]    
EXPOSE 8080 
