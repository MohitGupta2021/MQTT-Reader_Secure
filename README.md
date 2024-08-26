## Project Description: MQTT-Reader_Secure

## Project Name: MQTT-Reader_Secure

Overview: The MQTT-Reader_Secure project is dedicated to developing a secure MQTT client that communicates with an MQTT broker through SSL/TLS encryption. This project encompasses the establishment of a Docker environment for running the Mosquitto MQTT broker and a Python application utilizing the gmqtt library for secure subscription to MQTT topics. The client ensures secure communication through authentication and encryption via certificates.

# Components:

### Mosquitto MQTT Broker:

Docker Container: The Mosquitto MQTT broker operates within a Docker container.
Configuration: Employs SSL/TLS for secure communication, managed via a Docker Compose file which includes configurations for the broker, publisher, subscriber, and Python application services.
Python MQTT Client:

### Scripts:
mqtt_subscriber_8883.py for secure connections.
mqtt_subscriber_1883.py for non-secure connections.
Library: Utilizes the gmqtt library to interface with the Mosquitto broker.
### Functionality:
Connection: Establishes a secure connection using SSL/TLS.
Subscription: Subscribes to the /events topic.
Message Handling: Asynchronously processes incoming messages and disconnections.
### Certificates:

CA Certificate: Used to validate the broker’s certificate.
Client Certificate and Key: Used for client authentication to the broker.
Certificate Generation: Generated via OpenSSL, with documentation provided in the project repository for reference. File paths are dynamically constructed relative to the script's location to ensure portability.
### Docker Setup:

## Docker Compose: Defines the configuration for the Mosquitto MQTT broker and Python client.
Network Configuration: Utilizes a bridge network driver to facilitate inter-service communication.
Port Mapping: Ensures accurate port mapping for broker communication.
Key Features:

### Secure Communication: Maintains data privacy and integrity through SSL/TLS encryption.
Asynchronous Handling: Employs asyncio for efficient MQTT message management.
Dynamic Paths: Utilizes relative file paths for certificates, enhancing deployment flexibility.

## 🚀 Getting Started

### 1. Clone the Repository

To start, clone the repository to your local machine:

```bash

git clone https://github.com/MohitGupta2021/MQTT-Reader_Secure.git

### 2.Navigate to the cloned directory:
cd MQTT-Reader_Secure

### 3.Verify the directory contents:
ls

### 4. Building the Docker Compose File
Build and start the Docker containers with Docker Compose:
docker-compose up --build

### 5. Publishing through the Docker Container
To publish data through the Docker container, execute:
docker-compose run --rm mqtt-pub

### 6. Subscribing through the Docker Container
To subscribe to data through the Docker container, use:
docker-compose run --rm mqtt-sub

### 7. Subscribing to Data through the Python Application
To subscribe to data using the Python application, run:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip list
### 8. Run the python scripts
for secure connections:
python mqtt_subscriber_8883.py
For non-secure connections:
python mqtt_subscriber_1883.py 
###  Running Mosquitto Clients with SSL
Publish:
mosquitto_pub -h localhost -p 8883 -t /events  -m "{“sensor_value”:20.2}" --cafile certs_copy/ca-root.crt --key certs_copy/mosquitto.key --cert certs_copy/mosquitto.crt -d 
Subscribe:
mosquitto_sub -h localhost -p 8883 -t /events  --cafile certs_copy/ca-root.crt --key certs_copy/mosquitto.key --cert certs_copy/mosquitto.crt -d
### Running Mosquitto Clients without SSL
Publish:
mosquitto_pub -h localhost -p 1883 -t /events  -m "{“sensor_value”:20.2}"  -d
Subsribe:
mosquitto_sub -h localhost -p 1883 -t /events -d

### Additional Information
Prerequisites: Ensure Docker and Docker Compose are installed on your system.
Documentation: For further configuration or troubleshooting, consult the repository's documentation or contact the repository maintainer.
