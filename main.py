import argparse
from src.reporter import Reporter

def parse_args():
  parser = argparse.ArgumentParser(description='Example testing app')
  parser.add_argument(
    "input_file",
    metavar="I",
    nargs=1,
    help="Name of the input file"
  )
  parser.add_argument(
    "output_file",
    metavar="O",
    nargs=1,
    help="Name of the output file"
  )
  parser.add_argument(
    "column",
    metavar="C",
    nargs=1,
    help="Column to aggregate"
  )
  arguments = parser.parse_args()
  if not arguments.input_file or not arguments.output_file or not arguments.column:
    parser.print_help()
    exit(1)
    
  return arguments.input_file[0], arguments.output_file[0], arguments.column[0]

if __name__ == "__main__":
    input_file, output_file, column = parse_args()
    reporter = Reporter(input_file, output_file, column)
    reporter.generate_report()