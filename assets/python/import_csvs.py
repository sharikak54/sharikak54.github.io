from os import listdir
from os.path import isfile, join
import csv

CASE_DIR = "../../_cases/"
CASE_SUFFIX = ".md"
filenames = [f for f in listdir(CASE_DIR) if isfile(join(CASE_DIR, f))]

cases = {}
for filename in filenames:
  short_name = filename.split(".")[0]
  with open(CASE_DIR + filename, 'r') as file1:
    lines = file1.readlines()
  for line in lines:
    if (line[0:6] == "name: "):
      case = {
        'short_name': short_name,
        'name': line[6:-1],
      }
      break
  cases[case['name']] = case



CSV_DIR = "../data/"
filenames = [f for f in listdir(CSV_DIR) if isfile(join(CSV_DIR, f))]

cases_to_update = {}
for filename in filenames:
  if (not filename[-4:] == ".tsv"):
    continue

  with open(CSV_DIR + filename, newline='') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter="	")
    for row in csvReader:
      if (not row['Full Case Name']):
        continue

      name = row['Full Case Name']
      short_name = cases[name]['short_name']

      case_filename = join(CASE_DIR, short_name + CASE_SUFFIX)
      if (not isfile(case_filename)):
        print("ERROR: file " + case_filename + " not found")
        continue

      case = {
        'optimal': row['Optimal'],
        'default_alg': row['(meta) top alg1'],
        'notes': row['Notes'],
        'name': name,
        'short_name': short_name,
        'filename': case_filename,
      }
      other_algs = row['Algs1'].split(" ")[1:]
      if (other_algs):
        case['other_algs'] = other_algs
      if (row['Algs2'] != "same alg"):
        case['mirror_algs'] = row['Algs2'].split(" ")

      cases_to_update[short_name] = case

for short_name in cases_to_update:
  case = cases_to_update[short_name]
  filename = case['filename']
  print(case)

  with open(filename, 'r') as file:
    # read a list of lines into data
    lines = file.readlines()
  
  new_lines = []
  # TODO convert to iterate by index to look backwards
  for line in lines:
    if (line == "recognition: TODO\n"):
      new_lines.append("optimal: " + case['optimal'] + "\n")
      new_lines.append("\n")
    elif (line == '  alg: "1,0/5,5/0,1"\n'):
      line = '  alg: "' + case['default_alg'] + '"\n'
    elif (line == "Description TODO\n"):
      new_lines.append("Notes: " + case['notes'] + "\n")
      new_lines.append("\n")
    new_lines.append(line)
    # print(line)

  # write everything back TODO
  with open(filename + "_test", 'w') as file:
    file.writelines(new_lines)
  
  break