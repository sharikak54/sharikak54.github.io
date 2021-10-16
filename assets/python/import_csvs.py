from os import listdir
from os.path import isfile, join
import csv

'''
Run this directly after running ./generate_cases.py.
'''

# CHANGE THIS TO TRUE TO RUN
# WARNING: this option overwrites a ton of files,
# make sure you know what you're doing!
OVERWRITE_CURRENT_FILES = False

CASE_DIR = "../../.collections/_cases/"
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
        case['color_mirror_algs'] = row['Algs2'].split(" ")

      cases_to_update[short_name] = case

for short_name in cases_to_update:
  case = cases_to_update[short_name]
  filename = case['filename']
  print(case)

  # Read old lines
  with open(filename, 'r') as file:
    # read a list of lines into data
    lines = file.readlines()
  
  # Generate lines in edited file

  found_optimal_line = False
  found_description_line = False

  new_lines = []
  i = 0
  while (i < len(lines)):
    line = lines[i]
    if (line[0:8] == "optimal:"):
      found_optimal_line = True
      line = "optimal: " + case['optimal'] + "\n"
    elif ((not found_optimal_line) and line == "recognition: TODO\n"):
      new_lines.append("optimal: " + case['optimal'] + "\n")
      new_lines.append("\n")
    elif (line == "Description TODO\n"):
      new_lines.append("Notes: " + case['notes'] + "\n")
      new_lines.append("\n")
    elif (i > 0):
      # Checking previous line(s)
      if (lines[i-1] == "default_alg:\n"):
        line = '  alg: "' + case['default_alg'] + '"\n'
      elif (lines[i-1] == "color_mirror_algs:\n"):
        if ('color_mirror_algs' in case.keys()):
          for mirror_alg in case['color_mirror_algs']:
            new_lines.append('  -\n')
            new_lines.append('    alg: "' + mirror_alg + '"\n')
            new_lines.append('    description: TODO\n')
        else:
          new_lines.pop()
        i += 3
        continue
      elif (lines[i-1] == "other_algs:\n"):
        if ('other_algs' in case.keys()):
          for other_alg in case['other_algs']:
            new_lines.append('  -\n')
            new_lines.append('    alg: "' + other_alg + '"\n')
            new_lines.append('    description: TODO\n')
        else:
          new_lines.pop()
        i += 3
        continue

    new_lines.append(line)
    i += 1

  if OVERWRITE_CURRENT_FILES:
    # Write everything back in
    with open(filename, 'w') as file:
      file.writelines(new_lines)
