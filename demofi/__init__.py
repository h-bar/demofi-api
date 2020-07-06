from demofi.server import demo_app
from demofi.model import BaseModel

from flask import Flask
def create_demo(m: BaseModel) -> Flask:
    return demo_app(m).app