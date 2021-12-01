from os import listdir
from os.path import isfile, join
import urllib.request
from utils import SHOULD_OVERWRITE_CURRENT_FILES



'''
TODO
Hit cubicle to generate case images based on current best algs for each case.
'''



OVERWRITE_CURRENT_FILES = SHOULD_OVERWRITE_CURRENT_FILES()

CASE_DIR = "../../.collections/_cases/"
CASE_SUFFIX = ".md"

CUBICLE_BASE = "https://cubiclealgdbimagegen.azurewebsites.net/generator?&stage=obl&puzzle=sq1&type=png&scheme=FFD900-FF0000-00FF00-FFFFFF-FF00FF-0000FF&case=1,-1/-3,-3/1,-4/4,-2/2,-4/2,0/-2,4/1,-5/-3,0/-3,-3/5,4/6,0/6,0/"
LOCAL_BASE = "../images/cases/"



filenames = [f for f in listdir(CASE_DIR) if isfile(join(CASE_DIR, f))]

for filename in filenames:
  short_name = filename.split(".")[0]
  with open(CASE_DIR + filename, 'r') as file1:
    lines = file1.readlines()

  case = {}
  for i in range(len(lines)):
    line = lines[i]
    if (line[0:6] == "name: "):
      case['short_name'] = short_name
      case['name'] = line[6:-1]
    elif (i > 0 and lines[i-1] == "default_alg:\n"):
      case['default_alg'] = line[8:-2]

  remote_filename = CUBICLE_BASE + case['default_alg']
  local_filename = LOCAL_BASE + case['short_name'] + ".png"
  if OVERWRITE_CURRENT_FILES:
    print("Retrieving " + case['name'] + "...")
    urllib.request.urlretrieve(remote_filename, local_filename)
  else:
    print(remote_filename)
    print(local_filename)
