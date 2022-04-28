import string
import flask
from devices.lightbulb import Lightbulb
from devices.smarttv import SmartTv
from devices.windowblinder import WindowBlinder

smartbuilding_app = flask.Flask(__name__)
smartbuilding_app.config["DEBUG"] = True

#Init lightbulbs
Lightbulb(app=smartbuilding_app, room='meetingroom', number=1, color=True)
Lightbulb(app=smartbuilding_app, room='meetingroom', number=2, color=True)
Lightbulb(app=smartbuilding_app, room='workingroom', number=3, color=False)
Lightbulb(app=smartbuilding_app, room='workingroom', number=4, color=False)

#Init smart tv
SmartTv(app=smartbuilding_app, room='meetingroom', number=1)

#Init window blinder
WindowBlinder(app=smartbuilding_app, room='meetingroom', number=1)

smartbuilding_app.run(host="0.0.0.0")
