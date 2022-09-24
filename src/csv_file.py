import pandas as pd

class CSVFile:
  def __init__(self, path: str):
    self.path = path

  def read_column(self, column: str):
    try:
      data = pd.read_csv(self.path)
      row = data[column]
      return row
    except KeyError:
      return []