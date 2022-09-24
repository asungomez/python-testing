import pandas as pd

class Aggregator:
  def __init__(self, data):
    self.data= data

  def aggregate(self):
    try:
      return self.data.value_counts()
    except AttributeError:
      return {}

