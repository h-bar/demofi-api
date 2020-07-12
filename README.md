# Demofi [Under early development]

Demofi is a template to build and deploy a quick demo for your Machine Learning model. This repository only includes code for an APU server. For a web app demo using this API server. Please see [demofi-web](https://github.com/h-bar/demofi-web).

## Usage

Modify my_demo.py to fit you model into  `run_model`. Upon each request, `run_model` will be called with a python object containning data sent along with the request as parameter. The returned value will be sent back as response in JSON format.

## Endpoint

- `POST /api/run`
  run the model with posted data. `data` field in request body with be used as parameter to call `run_model` as well as be saved to database. An `id` to the saved data and `result` will be sent along with response.

- `POST /api/<data_id>`
  run the model with data saved in data base. `data` field in request body with be used as parameter to call `run_model` as well as be saved to database. An `id` to the saved data and `result` will be sent along with response.
  
- `POST /api/run_no_save`
- `POST /api/data`
- `GET /api/data/<data_id>`
- `POST /api/truth`
- `POST /api/truth/<data_id>`
