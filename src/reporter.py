class Reporter:
  def __init__(self, origin: str):
    self.origin = origin

  def generate_report(self):
    return self.origin