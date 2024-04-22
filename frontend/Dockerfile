# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the app directory into the container
COPY /app .

# Copy pyproject.toml
COPY pyproject.toml .

# Expose port
EXPOSE 3000

# Set the command to run the App
CMD poetry run flet run -d -r --web --port 3000 main.py
