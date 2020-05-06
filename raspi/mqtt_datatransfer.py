import paho.mqtt.publish as publish
import serial

serial = serial.Serial('COM13',9600 , timeout = 2)

response = serial.readline()
publish.single("Sensor/DHT22", payload=response,
                 qos=0, hostname="192.168.43.59", port=1883)