from src.aggregator import Aggregator
from src.csv_file import CSVFile


class Reporter:
  def __init__(
    self, 
    input_file: str, 
    output_file: str,
    column: str
    ):
    self.input_file = input_file
    self.output_file = output_file
    self.column = column

  def generate_report(self):
    input_csv = CSVFile(self.input_file)
    data = input_csv.read_column(self.column)
    aggregator = Aggregator(data)
    aggregation = aggregator.aggregate()
    # output_csv = CSVFile(self.output_file)
    # output_csv.write(self.output_file, aggregation)