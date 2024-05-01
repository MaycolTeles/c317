# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src/app

# Set unbuffered output for python
# 1. Prevents Python from writing pyc files to disc
# 2. Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the app directory into the container
COPY /app .

# Copy pyproject.toml
COPY pyproject.toml .

# Set the command to run the App
CMD poetry run flet run -d -r --web --port 3000 main.py
