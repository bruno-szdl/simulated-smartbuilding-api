import string
import flask
from devices.lightbulb import Lightbulb

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Lightbulb(app, room='meetingroom', number=1, color=True)
Lightbulb(app, room='meetingroom', number=2, color=True)
Lightbulb(app, room='workingroom', number=3, color=False)
Lightbulb(app, room='workingroom', number=4, color=False)
#localhost:5000/smartbuilding/rooms/meetingroom/artifacts/lightbulb1/state

app.run(host="0.0.0.0")
