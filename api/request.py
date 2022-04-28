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

#Close Window blinder
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/windowblinder1/close/")
sleep(2)

#Turn on TV
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/smarttv1/turnOn/")
sleep(2)

#Change TV Channel
requests.put(
    "http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/smarttv1/channel/"
    , json = {"channel": 0}
)
sleep(1)
requests.put(
    "http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/smarttv1/channel/"
    , json = {"channel": 1}
)
sleep(1)
requests.put(
    "http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/smarttv1/channel/"
    , json = {"channel": 2}
)
sleep(1)

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

#Turn off TV
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/smarttv1/turnOff/")
sleep(2)

#Open Window blinder
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/windowblinder1/open/")
sleep(2)

#Turn off meeting room lights
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb1/switchOff/")
requests.put("http://127.0.0.1:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb2/switchOff/")