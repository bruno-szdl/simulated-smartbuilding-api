import string
from flask import request, jsonify, abort

class WindowBlinder:
    def __init__(self, app, room, number):

        #define atr
        self.windowblinder_state = 'waiting'

        #Set state
        @app.route(
            '/environments/smartbuilding/workspaces/'+room+'/artifacts/windowblinder'+str(number)+'/state/'
            , methods=['PUT']
            , endpoint='openwindowblinder'+str(number)
        )
        def setState():
            json_data = request.json
            state = json_data.get('state')
            if state == 'open':
                self.windowblinder_state = 'open'
                return jsonify(state='open')
            elif state == 'closed':
                self.windowblinder_state = 'closed'
                return jsonify(state='closed')

        #Get state
        @app.route(
            '/environments/smartbuilding/workspaces/'+room+'/artifacts/windowblinder'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatewindowblinder'+str(number)
        )
        def getState():
            return jsonify(state=self.windowblinder_state)