import RPi.GPIO as GPIO
from time import sleep
import glob

SLEEPTIME = 1
PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

sleep(SLEEPTIME)

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def ReadTemprature():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def ShowTemprature():
    lines = ReadTemprature()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = ReadTemprature()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temprature_string = lines[1][equals_pos+2:]
        temprature = float(temprature_string) / 1000.0
        return temprature

try:
    while True:
        print('===')
        print("Temperature:", ShowTemprature(), u'\u2103')
        sleep(SLEEPTIME)
 
except KeyboardInterrupt:
    print("Program stopped")
    GPIO.cleanup()

