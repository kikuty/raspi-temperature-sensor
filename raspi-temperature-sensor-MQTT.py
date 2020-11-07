import RPi.GPIO as GPIO
from time import sleep
import glob
import paho.mqtt.client as mqtt

SLEEPTIME = 1
PIN = 7
MQTT_BROKER_IP = "172.19.0.3"
MQTT_TOPIC = "temperature"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

sleep(SLEEPTIME)

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def ReadTemperature():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def ShowTemperature():
    lines = ReadTemperature()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = ReadTemperature()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temperature_string = lines[1][equals_pos+2:]
        temperature = float(temperature_string) / 1000.0
        return temperature

def on_connect(client, userdata, flag, rc):
    print("Connect with result code" + str(rc))

def on_publish(client, userdata, mid):
    print("publish: {0}" .format(mid))

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(MQTT_BROKER_IP, 1883, 60)

    while True:
        print('===')
        temperature = ShowTemperature()
        client.publish(MQTT_TOPIC, temperature)
        print("Temperature:", temperature, u'\u2103')
        sleep(SLEEPTIME)

except KeyboardInterrupt:
    print("\nProgram stopped")
    GPIO.cleanup()
    
