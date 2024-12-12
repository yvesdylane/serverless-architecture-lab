# Use an official Python 3.12 image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY app.py .

# Expose the port the app will run on (default Flask port)
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
