import json
from demofi.model import abstractModel

import nltk
class my_model(abstractModel):
  def init_model(self):
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    pass

  def run_model(self, data: {}, param: {}) -> {}:
    text = nltk.word_tokenize(data['content'])
    tagged = nltk.pos_tag(text)
    result = {
      'tokens': [],
      'labels': []
    }
    for t in tagged:
      result['tokens'].append(t[0])
      result['labels'].append(t[1])
    return result

  def destroy_model(self):
    pass