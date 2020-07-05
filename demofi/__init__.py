from demofi.server import demo_app
from demofi.model import model

from flask import Flask

def create_demo(m: model) -> Flask:
    demo = demo_app(m)
    return demo.app