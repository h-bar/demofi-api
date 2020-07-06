from demofi.app import demo_app
from demofi.db import dummyDB

def run_model(data: str) -> {}:
  return hash(data)

db = dummyDB()
# demo = demo_app(run_model)
demo = demo_app(run_model, db)
app = demo.app

if __name__ == "__main__":
  app.run()