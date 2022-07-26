from time import sleep
import requests
import json

#Turn on meeting room lights

requests.put(
    'http://192.168.15.8:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb1/toggle/'
    , json={'state': True}
)