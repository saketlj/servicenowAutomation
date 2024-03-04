# Python Script for Creating ServiceNow Change Requests


This Python script creates a change request in ServiceNow by making an API request with JSON data. The script reads configuration data and the JSON data from YAML files and logs important events and errors.

## Dependencies

```
Python 3.x
requests library
PyYAML library
logging library
datetime library
```

### To install the dependencies, run the following command:

```bash
pip install requests pyyaml
```

## Usage

   1. Clone this repository or copy the contents of the Python script to your local environment.

   2. Create a `config.yaml` file in the same directory as the Python script, and fill in the following configuration data:

      ```yaml
      authorization_token: <your_service_now_authorization_token>
      api_url: <your_service_now_api_url>
      json_data_file: <path_to_your_json_data_file>
      ```

   3. Create a JSON data file with the required data to create the ServiceNow change request. You can use the <forwarder-node-ip> placeholder in the JSON file to specify the IP address of the forwarder node. Example JSON data:

      ```json

       {
        "short_description": "Example change request",
        "description": "This is an example change request",
        "impact": "1 - High",
        "urgency": "1 - High",
        "category": "Hardware",
        "subcategory": "Server",
        "cmdb_ci": "Server1",
        "contact_type": "Email",
        "assignment_group": "Network"
       }  
      ```
 
   4. Run the Python script using the following command:
      ```bash
      python create_cr.py
      ```

      Follow the prompt to enter the IP address of the forwarder node.

   5. The script will log important events and errors to a file named app.log in the same directory as the Python script.

   6. If the API request is successful, the script will print the ServiceNow change request details to the console and log the success event. If the API request fails, the script will print the error message to the console and log the error event.

## Contributing

     Feel free to contribute to this project by opening an issue or submitting a pull request.