import json
from demofi.model import abstractModel
class my_model(abstractModel):
  def init_model(self):
    pass

  def run_model(self, data: {}, param: {}) -> {}:
    return {'str': json.dumps(data)}

  def destroy_model(self):
    pass