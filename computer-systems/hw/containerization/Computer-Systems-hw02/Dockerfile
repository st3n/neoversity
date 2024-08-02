# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
