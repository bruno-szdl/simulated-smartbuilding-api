import string
from flask import request, jsonify, abort

class SmartTv:
    def __init__(self, app, room, number):

        #define atr
        smarttv_state = {}
        smarttv_channel = {}
        smarttv_state['state'] = 'off'
        smarttv_channel['channel'] = 0

        #Turn on
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/turnOn/'
            , methods=['PUT']
            , endpoint='turnOnsmarttv'+str(number)
        )
        def turnOn():
            smarttv_state['state'] = 'on'
            return jsonify(smarttv_state)

        #Turn off
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/turnOff/'
            , methods=['PUT']
            , endpoint='turnOffsmarttv'+str(number)
        )
        def turnOff():
            smarttv_state['state'] = 'off'
            return jsonify(smarttv_state)

        #Set channel
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/channel/'
            , methods=['PUT']
            , endpoint='setColorsmarttv'+str(number)
        )
        def setChannel():
            smarttv_channel['channel'] = request.json['channel']
            return jsonify(smarttv_channel)

        #Get state
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatesmarttv'+str(number)
        )
        def getState():
            return jsonify(smarttv_state)

        #Get channel
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/smarttv'+str(number)+'/channel/'
            , methods=['GET']
            , endpoint='getColorsmarttv'+str(number)
        )
        def getChannel():
            return jsonify(smarttv_channel)