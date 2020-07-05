class model:
  def __init__(self, sample_data: str, sample_result: {}):
    sample_id = self.save_data(sample_data)
    sample_data = self.get_data(sample_id)

    assert(self.run_data(sample_data) == sample_result)
    assert(self.run_id(sample_id) == sample_result)
    assert(self.run_data_no_save(sample_data) == sample_result)

    assert(self.rm_data(sample_id))
    
  def save_data(self, data: str) -> str:
    raise NotImplementedError("Please implement save_data interface in your model class")
  
  def get_data(self, data_id: str) -> str:
    raise NotImplementedError("Please implement get_data interface in your model class")

  def rm_data(self, data_id: str) -> bool:
    raise NotImplementedError("Please implement rm_data interface in your model class")

  def run_data(self, data: str) -> {}:
    raise NotImplementedError("Please implement run_data interface in your model class")

  def run_id(self, data_id: str) -> {}:
    raise NotImplementedError("Please implement run_id interface in your model class")
  
  def run_data_no_save(self, data: str) -> {}:
    raise NotImplementedError("Please implement run_data_no_save interface in your model class")