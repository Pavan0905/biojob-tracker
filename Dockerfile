FROM python:3.12

# Set working directory
WORKDIR /app

# Install system packages including FastQC
RUN apt-get update && \
    apt-get install -y default-jre fastqc && \
    apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose Django port
EXPOSE 8000

# Start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]