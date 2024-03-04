import requests
import yaml
import logging
import datetime

logging.basicConfig(filename='log/app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# Read configuration from YAML file
with open('config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Get forwarder IP address from user input
forwarder_ip = input("Enter forwarder node IP address: ")
purpose = input("Enter CR Title (Purpose): ")
#planned_start = input("Enter Planned start day for CR: ")
#planned_end = input("Enter Planned end day for CR: ")
logging.info("User entered forwarder IP address: %s", forwarder_ip)
logging.info("User entered forwarder IP address: %s", purpose)
#logging.info("User entered forwarder IP address: %s", planned_start)
#logging.info("User entered forwarder IP address: %s", planned_end)

'''
# Convert datetime strings to datetime objects
planned_start = datetime.datetime.fromisoformat(planned_start)
planned_end = datetime.datetime.fromisoformat(planned_end)
planned_start = planned_start.replace('Z', '+00:00')
planned_end = planned_end.replace('Z', '+00:00')

# Convert datetime objects to strings
planned_start_str = planned_start.isoformat()
planned_end_str = planned_end.isoformat()
'''

# Construct headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': config['authorization_token'],
}


# Construct JSON data from YAML file
try:
    with open('config/' + config['json_data_file'], 'r') as f:
        yaml_data = f.read()
        # Replace <forwarder-node-ip> with user input
        yaml_data = yaml_data.replace('<forwarder-node-ip>', forwarder_ip)
        yaml_data = yaml_data.replace('Create Hypersocket NICs for the s32 L1BM partitions on the s01 forwarder in WDC07', purpose)
        # Replace planned_start and planned_end with user input
        #yaml_data = yaml_data.replace('planned_start', planned_start_str)
        #yaml_data = yaml_data.replace('planned_end', planned_end_str)
        # Load YAML data into a Python object
        json_data = yaml.safe_load(yaml_data)
except FileNotFoundError:
    logging.error("JSON data file '%s' not found.", config['json_data_file'])
    print(f"JSON data file '{config['json_data_file']}' not found.")
    exit(1)
except Exception as e:
    logging.error("Error reading JSON data file: %s", str(e))
    print(f"Error reading JSON data file: {str(e)}")
    exit(1)

# Make API request
response = requests.post(config['api_url'], headers=headers, json=json_data)

if response.status_code == 201:
    response_json = response.json()
    print(response_json) # Add this line to print the response JSON
    cr_url = response_json['href']
    cr_number = cr_url.split('/')[-1]  # extract the last part of the URL, which should be the CR number    
    logging.info(f"CR {cr_number} is created successfully")
    print(f"CR {cr_number} is created successfully")
else:
    logging.error("Error creating change request: %s", response.text)
    print("Error creating change request: " + response.text)

