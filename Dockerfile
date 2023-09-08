# Use a Python base image
FROM python:3.10

# Set a working directory
WORKDIR /app

# Install requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Set the default command to run start.sh
CMD ["./start.sh"]