from time import sleep
import requests

#Turn on meeting room lights
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb1/switchOn/")
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb2/switchOn/")
sleep(2)

#Turn on working room lights
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/workingroom/artifacts/lightbulb3/switchOn/")
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/workingroom/artifacts/lightbulb4/switchOn/")
sleep(2)

#Turn meeting room lights red
requests.put(
    "http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb1/color/"
    , json = {"color": "white"}
)
requests.put(
    "http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb2/color/"
    , json = {"color": "white"}
)
sleep(2)

#Turn off working room lights
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/workingroom/artifacts/lightbulb3/switchOff/")
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/workingroom/artifacts/lightbulb4/switchOff/")
sleep(2)

#Turn off meeting room lights
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb1/switchOff/")
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb2/switchOff/")