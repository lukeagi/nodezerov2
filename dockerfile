FROM python:3.11-slim
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "-m", "pytest"]
