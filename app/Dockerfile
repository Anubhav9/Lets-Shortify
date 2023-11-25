# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 1215 available to the world outside this container (if still needed)
EXPOSE 1215

# Define environment variable (if needed)
# ENV VARIABLE_NAME value

# Run pytest when the container launches
CMD ["python", "app.py"]
