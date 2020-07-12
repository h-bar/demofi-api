# Demofi [Under early development]

Demofi is a template to build and deploy a quick demo for your Machine Learning model. This repository only includes code for an API server. For a web app demo using this API server. Please see [demofi-web](https://github.com/h-bar/demofi-web).

## Usage

Modify my_demo.py to fit you model into  `run_model`. Upon each request, `run_model` is called with a python objects containning data and model parameters sent along with the request as parameter. The returned value is sent back as response in JSON format.

## Endpoint

- ```JSON
  POST /api/run
  reqest => 
  {
    "data": {},
    "param": {}
  }
  response =>
  {
    "id": "",
    "result": {}
  }
  Run the model with data and parameter. The data will be saved to database. Data id and model result are returned as response.

- ```JSON
  POST /api/run/<data_id>
  reqest => 
  {
    "data": {},
    "param": {}
  }
  response =>
  {
    "id": "",
    "result": {}
  }
  Run the model with data saved in data base specified by the data_id, and parameter. Data id and model result are returned as response.

- ```JSON
  POST /api/run_no_save
  reqest => 
  {
    "data": {},
    "param": {}
  }
  response =>
  {
    "id": null,
    "result": {}
  }
  Run the model with data and parameter. The data will not be saved to database. Only model result is returned as response.

- ```JSON
  POST /api/data
  reqest => 
  {
    "data": {}
  }
  response =>
  {
    "id": null
  }
  Save data to database. Data id is returned as the response


- ```JSON
  GET /api/data/<data_id>
  reqest => 
  {}
  response =>
  {
    "id":  "",
    "data": {}
  }
  Retrive data from database. Data id and data are returned as the response
 
- ```JSON
  POST /api/truth/<data_id>
  reqest => 
  {
    "truth": {}
  }
  response =>
  {
    "id":  "",
    "result": {}
  }
  Upload a truth for a data saved in database. Data id and the insertion result are returned as the response

- ```JSON
  GET /api/data/<data_id>
  reqest => 
  {}
  response =>
  {
    "id":  "",
    "result": {}
  }
  Retrive truth of a data saved in database. Data id and truth are returned as the response
