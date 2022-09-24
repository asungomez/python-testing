import argparse
from src.reporter import Reporter

def parse_args():
  parser = argparse.ArgumentParser(description='Example testing app')
  parser.add_argument(
    "file_name",
    metavar="I",
    nargs=1,
    help="Name of the file"
  )
  arguments = parser.parse_args()
  if not arguments.file_name:
    parser.print_help()
    exit(1)
  return arguments.file_name[0]

if __name__ == "__main__":
    file_name = parse_args()
    reporter = Reporter(file_name)
    result = reporter.generate_report()
    print(result)