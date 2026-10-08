FROM python:3.12-slim
WORKDIR /app
COPY expense.py .
ENV PYTHONUNBUFFERED=1
VOLUME /data
CMD ["python", "expense.py"]