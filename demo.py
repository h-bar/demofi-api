from demofi import create_demo
from demofi.model import model


class my_model(model):
  def __init__(self):
    super(model).__init__()    
  
  def save_data(self, data: str) -> str:
    return hash(data)
  
  def get_data(self, id: str) -> str:
    return id

  def run_data(self, data: str) -> {}:
    id = self.save_data(data)
    return {
      'id': id
    }

  def run_id(self, id: str) -> {}:
    data = self.get_data(id)
    return {
      'id': id
    }
  
  def run_data_no_save(self, data: str) -> {}:
    return {}


demo = create_demo(my_model())
demo.run(host='0.0.0.0')


