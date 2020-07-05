class model:
  def __init__(self):
    pass

  def save_data(self, data: str) -> str:
    raise NotImplementedError("Please implement save_data interface in your model class")
  
  def get_data(self, id: str) -> str:
    raise NotImplementedError("Please implement get_data interface in your model class")

  def run_data(self, data: str) -> {}:
    raise NotImplementedError("Please implement run_data interface in your model class")

  def run_id(self, id: str) -> {}:
    raise NotImplementedError("Please implement run_id interface in your model class")
  
  def run_data_no_save(self, data: str) -> {}:
    raise NotImplementedError("Please implement run_data_no_save interface in your model class")