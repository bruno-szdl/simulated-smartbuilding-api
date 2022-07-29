from time import sleep
import requests
import json

#Turn on meeting room lights

requests.put(
    'http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb1/toggle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/lightbulb2/toggle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb3/toggle/'
    , json={'state': True}
)
requests.put(
    'http://192.168.15.8:5000/environments/smartbuilding/workspaces/workingroom/artifacts/lightbulb4/toggle/'
    , json={'state': True}
)
# requests.put(
#     'http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/smarttv1/toggle/'
#     , json={'state': True}
# )
# requests.put(
#     'http://192.168.15.8:5000/environments/smartbuilding/workspaces/meetingroom/artifacts/windowblinder1/state/'
#     , json={'state': 'open'}
# )