# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Set unbuffered output for python
# 1. Prevents Python from writing pyc files to disc
# 2. Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Install dependencies
RUN apt update \
    && apt install -y libpq-dev gcc \
    && apt install -y netcat-traditional \
    && pip install --upgrade pip \
    && pip install psycopg2

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entrypoint.sh file into the container and make it executable
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the app directory into the container
COPY /app .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
