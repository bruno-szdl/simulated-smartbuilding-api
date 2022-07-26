import string
from flask import request, jsonify, abort

class WindowBlinder:
    def __init__(self, app, room, number):

        #define atr
        self.windowblinder_state = 'waiting'

        #Set state
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/state/'
            , methods=['PUT']
            , endpoint='openwindowblinder'+str(number)
        )
        def open():
            def toggle():
                json_data = request.json
                state = json_data.get('state')
                if state == True:
                    self.windowblinder_state = True
                    return jsonify(state=True)
                elif state == False:
                    self.windowblinder_state = False
                    return jsonify(state=False)

        #Get state
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatewindowblinder'+str(number)
        )
        def getState():
            return jsonify(self.windowblinder_state)