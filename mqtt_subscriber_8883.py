import asyncio  # For writing the asynchronous library
from gmqtt import Client as MQTTClient
import ssl
import os

# Define the base directory relative to the script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Constants
BROKER_HOST = 'localhost'            # Broker host; for localhost use 'localhost'
BROKER_PORT = 8883                   # Port number for the MQTT broker with TLS
TOPIC = '/events' 
              # Topic the client will subscribe to and listen for messages
CLIENT_ID = 'mqtt_reader_client'     # Unique client ID for the MQTT client 

CA_CERT = os.path.join(BASE_DIR, 'certs_copy', 'ca-root.crt')
CLIENT_CERT = os.path.join(BASE_DIR, 'certs_copy', 'mosquitto.crt')
CLIENT_KEY = os.path.join(BASE_DIR, 'certs_copy', 'mosquitto.key')

# debug to check the file path is correct or not 

# print("Client ID:", CLIENT_ID)
# print("CA Certificate Path:", CA_CERT)
# print("Client Certificate Path:", CLIENT_CERT)
# print("Client Key Path:", CLIENT_KEY)

# Callback to handle incoming messages
# This function is called when a message is received on a subscribed topic
async def on_message(client, topic, payload, qos, properties):
    print(f'Received message on {topic}: {payload.decode()}')

# Callback to handle connection
# This function is called when the client successfully connects to the broker
def on_connect(client, flags, rc, properties):
    print(f'Connected to MQTT broker at {BROKER_HOST}:{BROKER_PORT}')
    client.subscribe(TOPIC, qos=1)  # Subscribing to the topic with QoS 1
    print(f'Subscribed to topic: {TOPIC}')

# Callback to handle disconnection
# This function is called when the client disconnects from the broker
def on_disconnect(client, packet, exc=None):
    print('Disconnected from MQTT broker')

# Function to connect to the MQTT broker
# This function manages the connection to the MQTT broker asynchronously
async def connect_mqtt():
    client = MQTTClient(CLIENT_ID)
    
    # Assign the callbacks
    client.on_connect = on_connect      # Set callback for connection
    client.on_message = on_message      # Set callback for message reception
    client.on_disconnect = on_disconnect # Set callback for disconnection
    
    # Configure SSL context for client
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)  # Corrected for client connection
    ssl_context.load_verify_locations(CA_CERT)
    ssl_context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)

    # Connecting to the MQTT broker asynchronously
    await client.connect(BROKER_HOST, BROKER_PORT, ssl=ssl_context)
    
    try:
        await asyncio.Future()          # Keep the client connected indefinitely
    except asyncio.CancelledError:      # Handle cancellation of the asyncio task
        pass 
    finally:
        await client.disconnect()       # Ensure the client disconnects properly

# Ensure the following code block runs only if the script is executed directly
if __name__ == '__main__':
    loop = asyncio.get_event_loop()     # Create an event loop to execute asynchronous tasks
    try:
        loop.run_until_complete(connect_mqtt())  # Start the MQTT connection process
    except KeyboardInterrupt:
        pass
    finally:
        # Ensure the event loop is properly shut down
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()