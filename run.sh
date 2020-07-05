#! /usr/bin/bash

if [ $1 == "dev" ]; then
  FLASK_ENV=development python3 ./demo.py
else
  gunicorn -w 4 -b 0.0.0.0:5000 demo:app
fi