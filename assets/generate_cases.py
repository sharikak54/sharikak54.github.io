from os import listdir
from os.path import isfile, join

DIR = "../_faces/"
filenames = [f for f in listdir(DIR) if isfile(join(DIR, f))]

obl_types = {}
for filename in filenames:
  file1 = open(DIR + filename, 'r')
  lines = file1.readlines()
  
  for line in lines:
    if (line.find("short_name:") == 0):
      short_name = line[12:].strip()
    elif (line.find("type:") == 0):
      obl_type = line[6:].strip()
  
  if obl_type in obl_types.keys():
    obl_types[obl_type] += [short_name]
  else:
    obl_types[obl_type] = [short_name]

for obl_type in obl_types.keys():
  print("\n### " + obl_type)
  for face1 in obl_types[obl_type]:
    for face2 in obl_types[obl_type]:
      print(face1 + "_" + face2)


