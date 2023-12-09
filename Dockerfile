FROM python:3.10-slim

# Set the working directory to /app

# RUN apt-get update && apt-get install -y tesseract-ocr
RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils

WORKDIR /app
# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app/
# RUN apt-get install -y sox ffmpeg libcairo2 libcairo2-dev texlive-full pkg-config python3-dev
RUN pip install --trusted-host pypi.python.org -r requirements2.txt
# Make port 8000 available to the world outside this container
EXPOSE 8000
# Run websocket server when the container launches
CMD ["python", "/app/app.py"]
