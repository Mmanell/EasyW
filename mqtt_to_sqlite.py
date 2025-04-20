import paho.mqtt.client as mqtt
import sqlite3
import json

# Setup SQLite
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gas_level INTEGER,
    temperature REAL,
    humidity REAL,
    leak_detected BOOLEAN,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# MQTT settings
MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_TOPIC = "wokwi-bin"

# Callback when message arrives
def on_message(client, userdata, msg):
    print("Received message:", msg.payload.decode())
    data = json.loads(msg.payload.decode())
    
    c.execute('''
    INSERT INTO sensor_data (gas_level, temperature, humidity, leak_detected)
    VALUES (?, ?, ?, ?)
    ''', (data.get('gas_level'), data.get('temperature'), data.get('humidity'), data.get('leak_detected')))
    
    conn.commit()

# Setup MQTT client
client = mqtt.Client()
client.on_message = on_message

print("Connecting to broker...")
client.connect(MQTT_BROKER)

client.subscribe(MQTT_TOPIC)
print(f"Subscribed to {MQTT_TOPIC}")

# Start loop
client.loop_forever()
