import string
from flask import request, jsonify, abort

class SmartTv:
    def __init__(self, app, room, number):

        #define atr
        self.smarttv_state = bool(False)
        self.smarttv_channel = 0

        #Set state
        @app.route(
            '/environments/smartbuilding/workspaces/'+room+'/artifacts/smarttv'+str(number)+'/toggle/'
            , methods=['PUT']
            , endpoint='toggleSmartTv'+str(number)
        )
        def setState():
            json_data = request.json
            state = json_data.get('state')
            if state == True:
                self.smarttv_state = True
                return jsonify(state=True)
            elif state == False:
                self.smarttv_state = False
                return jsonify(state=False)

        #Set channel
        @app.route(
            '/environments/smartbuilding/workspaces/'+room+'/artifacts/smarttv'+str(number)+'/channel/'
            , methods=['PUT']
            , endpoint='setColorsmarttv'+str(number)
        )
        def setChannel():
            self.smarttv_channel = request.json['channel']
            return jsonify(channel=self.smarttv_channel)

        #Get state
        @app.route(
            '/environments/smartbuilding/workspaces/'+room+'/artifacts/smarttv'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatesmarttv'+str(number)
        )
        def getState():
            return jsonify(state=self.smarttv_state)

        #Get channel
        @app.route(
            '/environments/smartbuilding/workspaces/'+room+'/artifacts/smarttv'+str(number)+'/channel/'
            , methods=['GET']
            , endpoint='getColorsmarttv'+str(number)
        )
        def getChannel():
            return jsonify(channel=self.smarttv_channel)