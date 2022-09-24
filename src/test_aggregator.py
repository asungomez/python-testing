from aggregator import Aggregator
import pandas as pd

def test_empty_data(mocker):
  aggregator = Aggregator([])
  mocker.patch("aggregator.pd.Series.value_counts", return_value="success")
  result = aggregator.aggregate()
  assert result == {}

def test_non_empty_data(mocker):
  aggregator = Aggregator(pd.Series(['a','b','a','b','c']))
  mocker.patch("aggregator.pd.Series.value_counts", return_value="success")
  result = aggregator.aggregate()
  assert result == "success"