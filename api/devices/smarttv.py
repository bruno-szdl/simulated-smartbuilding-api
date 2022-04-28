import string
from flask import request, jsonify, abort

class SmartTv:
    def __init__(self, app, room, number):

        #define atr
        self.app = app
        self.room = room

        self.smarttv_state = {}
        self.smarttv_channel = {}
        self.smarttv_state['state'] = 'off'
        self.smarttv_channel['channel'] = 0

        #Turn on
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/turnOn/'
            , methods=['PUT']
            , endpoint='turnOnsmarttv'+str(number)
        )
        def turnOn():
            self.smarttv_state['state'] = 'on'
            return jsonify(self.smarttv_state)

        #Turn off
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/turnOff/'
            , methods=['PUT']
            , endpoint='turnOffsmarttv'+str(number)
        )
        def turnOff():
            self.smarttv_state['state'] = 'off'
            return jsonify(self.smarttv_state)

        #Set channel
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/channel/'
            , methods=['PUT']
            , endpoint='setColorsmarttv'+str(number)
        )
        def setColor():
            self.smarttv_channel['channel'] = request.json['channel']
            return jsonify(self.smarttv_channel)

        #Get state
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatesmarttv'+str(number)
        )
        def getState():
            return jsonify(self.smarttv_state)

        #Get channel
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/channel/'
            , methods=['GET']
            , endpoint='getColorsmarttv'+str(number)
        )
        def getChannel():
            return jsonify(self.smarttv_channel)