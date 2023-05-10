FROM python:3.9.15-slim

# Change working directory to cloned repo
WORKDIR /account-links-generator

COPY requirements.txt .

# Install python dependencies
RUN pip install --index-url https://artefacts.tax.service.gov.uk/artifactory/api/pypi/pips/simple --no-cache-dir -r requirements.txt

COPY . .
