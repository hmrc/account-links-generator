FROM python:3.9.1-slim

# Change working directory to cloned repo
WORKDIR /account-links-generator

COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
