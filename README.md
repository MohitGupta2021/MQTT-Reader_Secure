Project Description: MQTT-Reader_Secure

Project Name: MQTT-Reader_Secure

Overview: The MQTT-Reader_Secure project is dedicated to developing a secure MQTT client that communicates with an MQTT broker through SSL/TLS encryption. This project encompasses the establishment of a Docker environment for running the Mosquitto MQTT broker and a Python application utilizing the gmqtt library for secure subscription to MQTT topics. The client ensures secure communication through authentication and encryption via certificates.

Components:

Mosquitto MQTT Broker:

Docker Container: The Mosquitto MQTT broker operates within a Docker container.
Configuration: Employs SSL/TLS for secure communication, managed via a Docker Compose file which includes configurations for the broker, publisher, subscriber, and Python application services.
Python MQTT Client:

Scripts:
mqtt_subscriber_8883.py for secure connections.
mqtt_subscriber_1883.py for non-secure connections.
Library: Utilizes the gmqtt library to interface with the Mosquitto broker.
Functionality:
Connection: Establishes a secure connection using SSL/TLS.
Subscription: Subscribes to the /events topic.
Message Handling: Asynchronously processes incoming messages and disconnections.
Certificates:

CA Certificate: Used to validate the broker’s certificate.
Client Certificate and Key: Used for client authentication to the broker.
Certificate Generation: Generated via OpenSSL, with documentation provided in the project repository for reference. File paths are dynamically constructed relative to the script's location to ensure portability.
Docker Setup:

Docker Compose: Defines the configuration for the Mosquitto MQTT broker and Python client.
Network Configuration: Utilizes a bridge network driver to facilitate inter-service communication.
Port Mapping: Ensures accurate port mapping for broker communication.
Key Features:

Secure Communication: Maintains data privacy and integrity through SSL/TLS encryption.
Asynchronous Handling: Employs asyncio for efficient MQTT message management.
Dynamic Paths: Utilizes relative file paths for certificates, enhancing deployment flexibility.
Usage:

Setup:

Generate SSL/TLS certificates and place them in the designated directory.
Use Docker Compose to initiate the Mosquitto broker and associated services.
Execute the mqtt_subscriber_8883.py script to connect to the broker and begin message reception.
Configuration:

Modify the mqtt_subscriber_8883.py script to adjust certificate paths as required.
Update the Docker Compose file to configure MQTT broker settings as needed.
Conclusion: The MQTT-Reader_Secure project offers a secure and efficient solution for MQTT communication, leveraging Docker for streamlined deployment and Python for flexible message handling. The integration of SSL/TLS ensures secure data transmission, while dynamic certificate paths enhance adaptability across different environments.
