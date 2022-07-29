from time import sleep
import requests
import json

#Turn on meeting room lights

requests.put(
    'http://192.168.15.8:5000/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/toogle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/toogle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/smartbuilding/workspaces/workingroom/artifacts/lightbulb3/toogle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/smartbuilding/workspaces/workingroom/artifacts/lightbulb4/toogle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/toogle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/smartbuilding/workspaces/meetingroom/artifacts/windowblinder1/state/'
    , json={'state': 'open'}
)