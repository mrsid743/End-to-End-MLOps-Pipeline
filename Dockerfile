# Update to 3.12 to satisfy numpy==2.5.1
FROM python:3.12-slim

# The rest stays exactly the same
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/src/

# ... your existing lines ...
COPY src/ /app/src/

# EXPOSE port 8000 so Kubernetes can route to it
EXPOSE 8000

# The critical missing piece: Start the server!
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]