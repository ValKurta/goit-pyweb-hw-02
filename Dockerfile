# Use the official Python image as the base image
FROM python:3.11

# Install Poetry
RUN pip install poetry

# Install bash
RUN apt-get update && apt-get install -y bash

# Install necessary libraries for working with Poetry
RUN apt-get update && apt-get install -y build-essential

# Install git
RUN apt-get update && apt-get install -y git

# Install dependencies for psycopg2-binary
RUN apt-get update && apt-get install -y libpq-dev

# Install curl
RUN apt-get update && apt-get install -y curl

# Set the working directory
WORKDIR /app

# Copy project files to the working directory
COPY . /app

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# cd /app/contact_manager by default
WORKDIR /app/contact_manager

# default command
CMD ["poetry", "run", "python", "main.py"]