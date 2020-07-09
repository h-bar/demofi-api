#! /usr/bin/bash

if [ $1 == "dev" ]; then
  FLASK_ENV=development python3 ./main.py
else
  gunicorn -w 4 -b 0.0.0.0:5000 main:app
fi