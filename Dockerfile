# Use official Python image as base
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 6161 for Flask
EXPOSE 6161

# Ensure the database exists, apply migrations, and start Flask
CMD ["sh", "-c", "flask db upgrade && python -m scripts.init_db && flask run --host=0.0.0.0 --port=6161"]
