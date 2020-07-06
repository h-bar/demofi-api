class BaseModel:
  def __init__(self, sample_data: str, sample_result: {}):
    sample_id = self.save_data(sample_data)
    sample_data = self.get_data(sample_id)

    assert(self.run(sample_data) == sample_result)

    assert(self.rm_data(sample_id))
    
  def save_data(self, data: str) -> str:
    raise NotImplementedError("Please implement save_data interface in your model class")
  
  def get_data(self, data_id: str) -> str:
    raise NotImplementedError("Please implement get_data interface in your model class")

  def rm_data(self, data_id: str) -> bool:
    raise NotImplementedError("Please implement rm_data interface in your model class")

  def run(self, data: str) -> {}:
    raise NotImplementedError("Please implement run_data interface in your model class")