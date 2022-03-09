#Inherit from the Python Docker image
FROM python:3.7-slim

# Install the Flask package via pip
RUN pip install flask

COPY API_code.py /app/
COPY factorialcode.py /app/
WORKDIR /app/
EXPOSE 5002
# Set the command as the script name
CMD ["python", "APIcode.py"]
