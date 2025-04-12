FROM python:3.12.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install Python packages
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files to the working directory
COPY mapping /app/mapping
COPY log_utils.py /app/
COPY main.py /app/
COPY metrics_2_usage_convertor.py /app/
COPY version /app/

# Run the application
CMD ["python3", "main.py"]
