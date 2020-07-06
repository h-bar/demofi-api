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

        try:
            os.makedirs(self.app.instance_path)
        except OSError:
            pass

        CORS(self.app)

        @self.app.route("/api/data", methods=['POST'])
        def saveHandler():
            if 'data' not in request.json:
                return {}

            data = request.json['data']
            data_id = self.m.save_data(data)

            return {
                'id': data_id
            }

        @self.app.route("/api/data/<data_id>", methods=['GET'])
        def getHandler(data_id):
            data = self.m.get_data(data_id)

            if data == None:
                return {}
                
            return {
                'id': data_id,
                'data': data
            }

        @self.app.route("/api/data/<data_id>", methods=['DELETE'])
        def rmHandler(data_id):
            result = self.m.rm_data(data_id)
            return {
                'id': data_id,
                'result': result
            }