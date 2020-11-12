# raspi-temperature-sensor

<p>
    <a href="https://github.com/kikuty/raspi-temperature-sensor/commits/master">
    <img src="https://img.shields.io/github/last-commit/kikuty/raspi-temperature-sensor.svg?style=flat-square&logo=github&logoColor=white">
    <a href="https://github.com/kikuty/raspi-temperature-sensor/issues">
    <img src="https://img.shields.io/github/issues-raw/kikuty/raspi-temperature-sensor.svg?style=flat-square&logo=github&logoColor=white">
    <a href="https://github.com/kikuty/raspi-temperature-sensorpulls">
    <img src="https://img.shields.io/github/issues-pr-raw/kikuty/raspi-temperature-sensor.svg?style=flat-square&logo=github&logoColor=white">
    <a href="https://github.com/kikuty/raspi-temperature-sensorpulls">
    <img src="https://img.shields.io/github/license/kikuty/raspi-temperature-sensor.svg?style=flat-square&logo=github&logoColor=white">
</p>

<p>
  <a href="#about">About</a> | 
  <a href="#tested-sensor">Tested sensor</a> | 
  <a href="#pin-assingment">PIN assingment</a> | 
  <a href="#tested-environment">Tested environment</a> | 
  <a href="#usage">Usage</a> | 
  <a href="#license">License</a> | 
  <a href="#author">Author</a> 
</p>

***
## About
A temperature monitor to work with DS18B20, 1-Wire sensor on the Raspberry Pi, featuring MQTT for distributing data.

## Tested sensor  
DS18B20 (Temperature sensor)  

## PIN assingment  
* Signal -> Pin7 (as specified in the "PIN" variable in the code)  
* +V -> 3.3V (e.g. Pin1)  
* GND -> GND  (e.g. Pin39)

Also see [Raspberry Pi GPIO Usage](https://www.raspberrypi.org/documentation/usage/gpio/),
or check the Pin status using the `gpio readall` command.

## Tested environment  
* Raspberry Pi 4 model B  
* Raspberry Pi OS (32-bit) with desktop and recommended software(verrion August 2020)  
* Python 3.7.3  

## Circuit diagram example
![Circuit diagram](https://github.com/kikuty/raspi-temperature-sensor/blob/main/DS18B20.jpg)

## Usage  
Clone and run this code, you'll need [paho-mqtt](https://pypi.org/project/paho-mqtt/) installed on your Raspberry Pi.

```
$  sudo pip3 install paho-mqtt
```

After the code clone & paho-mqtt instalarion, from your command line:
1. Just show the temperature on your command line
```
$ sudo python3 raspi-temperature-sensor-noMQTT.py
```  
output
```
===
Temperature: 19.687 ℃
===
Temperature: 19.687 ℃
===
```
2. Show the temperature on your command line and send it to MQTT Broker
Please change the variables, `MQTT_BROKER_IP` and `MQTT_TOPIC` in the code before running
```
$ sudo python3 raspi-temperature-sensor-MQTT.py
``` 
output
```
===
publish: 1
Temperature: 19.625 ℃
===
publish: 2
Temperature: 19.625 ℃
===
```

Ctrl+C to Stop.  

## License  
This project is published under [MIT license](https://en.wikipedia.org/wiki/MIT_License).  

## Author  
Yoshinao Kikuchi  
