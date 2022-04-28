import string
from flask import request, jsonify, abort

class WindowBlinder:
    def __init__(self, app, room, number):

        #define atr
        self.app = app
        self.room = room

        self.windowblinder_state = {}
        self.windowblinder_state['state'] = 'closed'

        #Open
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/open/'
            , methods=['PUT']
            , endpoint='openwindowblinder'+str(number)
        )
        def open():
            self.windowblinder_state['state'] = 'open'
            return jsonify(self.windowblinder_state)

        #Close
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/close/'
            , methods=['PUT']
            , endpoint='closewindowblinder'+str(number)
        )
        def close():
            self.windowblinder_state['state'] = 'closed'
            return jsonify(self.windowblinder_state)

        #Get state
        @self.app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatewindowblinder'+str(number)
        )
        def getState():
            return jsonify(self.windowblinder_state)