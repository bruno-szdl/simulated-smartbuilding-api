import string
from flask import request, jsonify, abort

class Lightbulb:
    def __init__(self, app, room, number, color):

        #define atr
        self.app = app
        self.room = room
        self.color = color

        self.lightbulb_state = {}
        self.lightbulb_state['state'] = 'off'

        if self.color:
            self.lightbulb_color = {}
            self.lightbulb_color['color'] = 'white'

        #Switch on
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/switchOn/'
            , methods=['PUT']
            , endpoint='switchOnLightbulb'+str(number)
        )
        def switchOn():
            self.lightbulb_state['state'] = 'on'
            return jsonify(self.lightbulb_state)

        #Switch off
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/switchOff/'
            , methods=['PUT']
            , endpoint='switchOffLightbulb'+str(number)
        )
        def switchOff():
            self.lightbulb_state['state'] = 'off'
            return jsonify(self.lightbulb_state)

        #Set color
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/color/'
            , methods=['PUT']
            , endpoint='setColorLightbulb'+str(number)
        )
        def setColor():
            if self.color:
                self.lightbulb_color['color'] = request.json['color']
                return jsonify(self.lightbulb_color)
            else:
                return

        #Get state
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStateLightbulb'+str(number)
        )
        def getState():
            return jsonify(self.lightbulb_state)

        #Get color
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/color/'
            , methods=['GET']
            , endpoint='getColorLightbulb'+str(number)
        )
        def getColor():
            return jsonify(self.lightbulb_color)