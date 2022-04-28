import string
from flask import request, jsonify, abort

class WindowBlinder:
    def __init__(self, app, room, number):

        #define atr
        windowblinder_state = {}
        windowblinder_state['state'] = 'waiting'

        #Open
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/open/'
            , methods=['PUT']
            , endpoint='openwindowblinder'+str(number)
        )
        def open():
            windowblinder_state['state'] = 'open'
            return jsonify(windowblinder_state)

        #Close
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/close/'
            , methods=['PUT']
            , endpoint='closewindowblinder'+str(number)
        )
        def close():
            windowblinder_state['state'] = 'closed'
            return jsonify(windowblinder_state)

        #Get state
        @app.route(
            '/smartbuilding/rooms/'+room+'/artifacts/windowblinder'+str(number)+'/state/'
            , methods=['GET']
            , endpoint='getStatewindowblinder'+str(number)
        )
        def getState():
            return jsonify(windowblinder_state)