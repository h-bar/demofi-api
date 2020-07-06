class abstractDB:
  def __init__(self):
    pass

  def save_data(self, data: str) -> str:
    raise NotImplementedError("Please implement save_data interface in your model class")
  
  def get_data(self, data_id: str) -> str:
    raise NotImplementedError("Please implement get_data interface in your model class")

  def rm_data(self, data_id: str) -> bool:
    raise NotImplementedError("Please implement rm_data interface in your model class")

  def add_truth(self, data_id: str, truth: {}) -> bool:
    raise NotImplementedError("Please implement add_truth interface in your model class")
  

class dummyDB(abstractDB):
  def __init__(self):
    super(dummyDB, self).__init__()
  
  def save_data(self, data: str) -> str:
    self.get_data(data)
    return hash(data)
  
  def get_data(self, data_id: str) -> str:
    return "dfsdfss"

  def rm_data(self, data_id: str) -> bool:
    return True

  def add_truth(self, data_id: str, truth: {}) -> bool:
    return True