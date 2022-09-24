from reporter import Reporter

def test_returns_the_file():
  reporter = Reporter("something")
  assert reporter.generate_report() == "something"