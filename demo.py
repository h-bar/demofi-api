from demofi.app import demo_app
from demofi.db import dummyDB, sqliteDB

def run_model(data: str) -> {}:
  return hash(data)

# db = dummyDB()
db = sqliteDB('./db.db', './schema.sql')

# demo = demo_app(run_model)
demo = demo_app(run_model, db)

app = demo.app

if __name__ == "__main__":
  app.run()