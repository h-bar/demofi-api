import os
from flask import Flask

def create_app():
    app = Flask("demopy", instance_relative_config=True)
    app.config.update(
        DEBUG=True,
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/api/<action>')
    def actionHandler(action):
        return action

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')