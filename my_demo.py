from demofi import db

def run_model(data: str) -> {}:
  return hash(data)

model_db = db.sqliteDB('./db.db', './schema.sql')