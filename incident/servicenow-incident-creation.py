import requests
import yaml
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the log level to INFO

# Load the config and payload files
with open("incident-config.yaml", "r") as f:
    config = yaml.safe_load(f)

with open("incident-payload-data.yaml", "r") as f:
    payload = yaml.safe_load(f)

# Set the headers and URL for the POST request
headers = {
    "Content-Type": "application/json",
    "Authorization": config["token"]
}

url = config["url"]

# Send the POST request and handle any exceptions
try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    json_response = response.json()  # Parse the JSON response

    logging.info("Incident created successfully with response code: %s", response.status_code)
    logging.info("Response: %s", json_response)  # Log the response JSON
    incident_number = json_response.get('incidentId')  # Assuming the incident number is present in the response

    if incident_number:
        logging.info("Incident number: %s", incident_number)  # Log the incident number
    else:
        logging.warning("Incident number not found in the response.")

except requests.exceptions.HTTPError as err:
    logging.error("Error creating incident: %s", err)