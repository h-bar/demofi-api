import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from demofi.db import *


class demo_app:
    def __init__(self, r: callable, db : abstractDB = None):    
        self.app = Flask(__name__.split('.')[0], instance_relative_config=True)
        self.run = r
        self.db = db

        try:
            os.makedirs(self.app.instance_path)
        except OSError:
            pass

        CORS(self.app)

        if self.db == None:
            @self.app.route("/api/run", methods=['POST'])
            @self.app.route("/api/run_no_save", methods=['POST'])
            def runHandler():
                if 'data' not in request.json:
                    return {}
                
                data = request.json['data']
                result = self.run(data)

                return {
                    'id': '',
                    'result': result
                }

        else:
            @self.app.route("/api/data", methods=['POST'])
            def saveHandler():
                if 'data' not in request.json:
                    return {}

                data = request.json['data']
                data_id = self.db.save_data(data)

                return {
                    'id': data_id
                }

            @self.app.route("/api/data/<data_id>", methods=['GET'])
            def getHandler(data_id):
                data = self.db.get_data(data_id)

                if data == None:
                    return {}

                return {
                    'id': data_id,
                    'data': data
                }

            @self.app.route("/api/data/<data_id>", methods=['DELETE'])
            def rmHandler(data_id):
                result = self.db.rm_data(data_id)
                return {
                    'id': data_id,
                    'result': result
                }
            

            @self.app.route("/api/run", methods=['POST'])
            def runHandler():
                if 'data' not in request.json:
                    return {}
                
                data = request.json['data']
                data_id = self.db.save_data(data)
                result = self.run(data)

                return {
                    'id': data_id,
                    'result': result
                }

            @self.app.route("/api/run_no_save", methods=['POST'])
            def runNoSaveHandler():
                if 'data' not in request.json:
                    return {}
                
                data = request.json['data']
                result = self.run(data)

                return {
                    'id': '',
                    'result': result
                }

            @self.app.route("/api/run/<data_id>", methods=['POST'])
            def runIDHandler(data_id):
                data = self.db.get_data(data_id)

                if data == None:
                    return {}
                
                result = self.run(data)
                return {
                    'id': data_id,
                    'result': result
                }

            @self.app.route("/api/truth/<data_id>", methods=['POST'])
            def addTruthHandler(data_id):
                if 'truth' not in request.json:
                    return {}
                
                truth = request.json['truth']
                result = self.db.add_truth(data_id, truth)

                return {
                    'id': data_id,
                    'result': result
                }

            @self.app.route("/api/truth/<data_id>", methods=['GET'])
            def getTruthHandler(data_id):
                result = self.db.get_truth(data_id)

                return {
                    'id': data_id,
                    'result': result
                }