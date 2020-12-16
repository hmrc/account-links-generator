FROM python:3.6.5-slim

# Change working directory to cloned repo
WORKDIR /account-links-generator

COPY . .

# Install python dependencies
RUN pip install -r requirements.txt
