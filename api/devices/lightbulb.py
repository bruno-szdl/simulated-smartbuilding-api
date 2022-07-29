import string
from flask import request, jsonify, abort

class Lightbulb:
    def __init__(self, app, room, number, color):

        #define atr
        self.lightbulb_state = bool(False)

        if color:
            self.lightbulb_color = 'white'

        #toggle
        @app.route(
            '/smartbuilding/workspaces/'+room+'/artifacts/lightbulb'+str(number)+'/toggle/'
            , methods=['PUT']
            , endpoint='toggleLightbulb'+str(number)
        )
        def toggle():
            json_data = request.json
            state = json_data.get('state')
            if state == True:
                self.lightbulb_state = True
                return jsonify(state=True)
            elif state == False:
                self.lightbulb_state = False
                return jsonify(state=False)

        #Set color
        @app.route(
            '/smartbuilding/workspaces/'+room+'/artifacts/lightbulb'+str(number)+'/color/'
            , methods=['PUT']
            , endpoint='setColorLightbulb'+str(number)
        )
        def setColor():
            if color:
                self.lightbulb_color = request.json['color']
                return jsonify(color=self.lightbulb_color)
            else:
                return

        #Get state
        @app.route(
            '/smartbuilding/workspaces/'+room+'/artifacts/lightbulb'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStateLightbulb'+str(number)
        )
        def getState():
            return jsonify(state=self.lightbulb_state)

        #Get color
        @app.route(
            '/smartbuilding/workspaces/'+room+'/artifacts/lightbulb'+str(number)+'/color/'
            , methods=['GET']
            , endpoint='getColorLightbulb'+str(number)
        )
        def getColor():
            return jsonify(color=self.lightbulb_color)