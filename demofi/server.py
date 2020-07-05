import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from demofi.model import model

class demo_app:
    def __init__(self, m: model):    
        self.app = Flask(__name__.split('.')[0], instance_relative_config=True)
        self.app.config.update(
            DEBUG=True,
        )
        self.m = m

        self.m.save_data("fdsfs")
        self.m.get_data("dfsd")
        self.m.run_id("sdfdsf")
        self.m.run_data_no_save("dfsdfs")
        self.m.run_data("dfds")

        try:
            os.makedirs(self.app.instance_path)
        except OSError:
            pass

        CORS(self.app)

        @self.app.route('/api/<action>',  methods=['POST'])
        def actionHandler(action):
            return action

        @self.app.route('/api/urlecho/<data>',  methods=['POST'])
        def urlechoHandler(data):
            return data

        @self.app.route('/api/jsonecho',  methods=['POST'])
        def jsonechoHandler():
            data = request.json

            resp = {
                'result': data['data']
            }

            return jsonify(resp)