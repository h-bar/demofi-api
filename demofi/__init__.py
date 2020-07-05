from demofi.server import demo_app
from demofi.model import model

from flask import Flask
def create_demo(m: model) -> Flask:
    return demo_app(m).app