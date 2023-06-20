# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install PyTorch
RUN pip install torch torchvision torchaudio

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory (including the code) into the container
COPY . .

# Expose the port on which the FastAPI app will run (default is 8000)
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
