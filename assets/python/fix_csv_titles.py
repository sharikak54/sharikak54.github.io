from os import listdir
from os.path import isfile, join
from utils import SHOULD_OVERWRITE_CURRENT_FILES



'''
Fix the csv title rows to differentiate first and second images/algs/etc.
Must run this whenever a new .tsv is downloaded from the spreadsheet.
'''

OVERWRITE_CURRENT_FILES = SHOULD_OVERWRITE_CURRENT_FILES()



CSV_DIR = "../data/"
filenames = [f for f in listdir(CSV_DIR) if isfile(join(CSV_DIR, f))]

for filename in filenames:
  if (not filename[-4:] == ".tsv"):
    continue

  print(filename)
  contents = ""
  with open(CSV_DIR + filename, newline='') as csvfile:
    lines = csvfile.readlines()

    # previous "Image	Optimal	(meta) top alg	Algs	Image	(meta) top alg	Algs	Notes	Recognition Notes	Best Alg Notes	Full Case Name	Parents"
    lines[0] = "Image1	Optimal1	(meta) top alg1	Algs1	Image2	(meta) top alg2	Algs2	Notes	Recognition Notes	Best Alg Notes	Full Case Name	Parents\n"
    contents = "".join(lines)

  if OVERWRITE_CURRENT_FILES:
    with open(CSV_DIR + filename, 'w') as csvfile:
      lines = csvfile.write(contents)
  else:
    print("\n ### contents:")
    print(contents)

