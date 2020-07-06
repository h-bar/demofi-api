from demofi import create_demo
from demofi.model import model


class my_model(model):
  def __init__(self, sample_data: str, sample_result: {}):
    super(my_model, self).__init__(sample_data, sample_result)    
  
  def save_data(self, data: str) -> str:
    return hash(data)
  
  def get_data(self, data_id: str) -> str:
    return "dfsdfss"

  def rm_data(self, data_id: str) -> bool:
    return True
    
  def run(self, data: str) -> {}:
    data_id = self.save_data(data)
    return {
      'result': hash(data),
    }


sample_data = "dfsdfss"
sample_result = {
  'result': hash(sample_data)
}

app = create_demo(my_model(sample_data, sample_result))

if __name__ == "__main__":
  app.run()