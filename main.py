from demofi.app import demo_app
from my_demo import my_model
from demofi import db

model_db = db.sqliteDB('./db.db', './schema.sql')
app = demo_app(my_model(), model_db).app

if __name__ == "__main__":
  app.run()