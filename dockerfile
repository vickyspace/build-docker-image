# Use a base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the source code into the container
COPY . /app

# Specify the command to run your application
CMD [ "python", "app.py" ]
