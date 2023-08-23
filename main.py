import json
import paho.mqtt.client as mqtt
from datetime import datetime
import time
import datetime
import os
import random
from colorama import Fore
from colorama import Back
from colorama import Style
from termcolor import colored, cprint
import sys
import re


# MQTT server details
mqtt_broker = "ec2-18-184-11-58.eu-central-1.compute.amazonaws.com"
mqtt_port = 1883
mqtt_username = "test-client-5"
mqtt_password = "eXxgXc3JtXzi&VxVqd^5"


# there are two ways to specify the device_id:
#  1. define the device_id here
#  2. use a command line parameter (the first command line parameter will be interpreted as the device_id)
device_id = "351358817705806"


# firmware download details for the "older" firmware. Note: sha needs to be updated if firmware checks that
# AXO real hardware
update_command_1 = {"url": "http://dev-switch-fota.s3.eu-central-1.amazonaws.com/downloads/app_update_axo_01.bin",
                 "fw_version": "0.1", "size": 348902, "sha1": "a82221d8c331b612089d9a5c983023c0aebb2e36"}

# firmware download details for the "newer" firmware. Note: sha needs to be updated if firmware checks that
update_command_2 = {"url": "http://dev-switch-fota.s3.eu-central-1.amazonaws.com/downloads/app_update_axo_02.bin",
                 "fw_version": "0.2", "size": 348902,
                 "sha1": "ff5473aa0301719799627d12f799410de24f909f"}

log_file = "ota_test.log"

# Topics
root_topic = '/device/' + device_id
metrics_update_topic = root_topic + '/metrics/update'
event_topic = root_topic + '/event'
cmd_accepted_topic = root_topic + '/command/accepted'
publish_cmd_topic = root_topic + '/command'
ota_accepted_topic = root_topic + '/ota/update/accepted'
ota_rejected_topic = root_topic + '/ota/update/rejected'
update_accepted_topic = root_topic + '/update/accepted'
ota_update_topic = root_topic + '/ota/update/'
cmd_received_topic = root_topic + '/command'
cmd_rejected_topic = root_topic + '/command/rejected'

