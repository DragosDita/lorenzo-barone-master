# Use a Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose any necessary ports (if applicable)
# EXPOSE <port>

# Set the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

