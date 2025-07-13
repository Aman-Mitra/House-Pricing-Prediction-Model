# Use an official Python base image
FROM python:3.11

# Copy project files into container
COPY . /app

# Set working directory inside container
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE $PORT

# Start the Flask app
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app