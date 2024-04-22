# Use an official Python runtime as the base image
FROM python:3.12-slim

# Install dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

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

# Expose port
EXPOSE 8000

# Run migrations and start the server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
