import string
from flask import request, jsonify, abort

class Lightbulb:
    def __init__(self, app, room, number, color):

        #define atr
        lightbulb_state = {}
        lightbulb_state['state'] = 'off'

        if color:
            lightbulb_color = {}
            lightbulb_color['color'] = 'white'

        #Switch on
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/switchOn/'
            , methods=['PUT']
            , endpoint='switchOnLightbulb'+str(number)
        )
        def switchOn():
            lightbulb_state['state'] = 'on'
            return jsonify(lightbulb_state)

        #Switch off
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/switchOff/'
            , methods=['PUT']
            , endpoint='switchOffLightbulb'+str(number)
        )
        def switchOff():
            lightbulb_state['state'] = 'off'
            return jsonify(lightbulb_state)

        #Set color
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/color/'
            , methods=['PUT']
            , endpoint='setColorLightbulb'+str(number)
        )
        def setColor():
            if color:
                lightbulb_color['color'] = request.json['color']
                return jsonify(lightbulb_color)
            else:
                return

        #Get state
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStateLightbulb'+str(number)
        )
        def getState():
            return jsonify(lightbulb_state)

        #Get color
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/lightbulb'+str(number)+'/color/'
            , methods=['GET']
            , endpoint='getColorLightbulb'+str(number)
        )
        def getColor():
            return jsonify(lightbulb_color)