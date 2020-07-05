import os
from flask import Flask, request, jsonify
from flask_cors import CORS

def create_demo():
    app = Flask("demopy", instance_relative_config=True)
    app.config.update(
        DEBUG=True,
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/api/<action>',  methods=['POST'])
    def actionHandler(action):
        return action

    @app.route('/api/urlecho/<data>',  methods=['POST'])
    def urlechoHandler(data):
        return data

    @app.route('/api/jsonecho',  methods=['POST'])
    def jsonechoHandler():
        data = request.json

        resp = {
            'result': data['data']
        }

        return jsonify(resp) 
    
    CORS(app)
    return app

if __name__ == "__main__":
    app = create_demo()
    app.run(host='0.0.0.0')