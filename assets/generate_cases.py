from os import listdir
from os.path import isfile, join

DIR = "../_faces/"
filenames = [f for f in listdir(DIR) if isfile(join(DIR, f))]

obl_types = {}
for filename in filenames:
  file1 = open(DIR + filename, 'r')
  lines = file1.readlines()
  
  name = False
  short_name = False
  nickname = False
  obl_type = False
  has_lr = False
  for line in lines:
    if (line.find("name:") == 0):
      name = line[6:].strip()
    elif (line.find("short_name:") == 0):
      short_name = line[12:].strip()
    elif (line.find("nickname:") == 0):
      nickname = line[10:].strip()
    elif (line.find("type:") == 0):
      obl_type = line[6:].strip()
    elif (line.find("has_lr:") == 0):
      has_lr = line[8:].strip()

  face = {
    'name': name,
    'short_name': short_name,
    'nickname': nickname,
    'obl_type': obl_type,
    'lr': has_lr
  }

  if (face['lr']):
    lface = face.copy()
    lface['short_name'] = "l" + face['short_name']
    lface['lr'] = "Left"
    rface = face.copy()
    rface['short_name'] = "r" + face['short_name']
    rface['lr'] = "Right"
    insert = [lface, rface]
  else:
    insert = [face]

  if obl_type in obl_types.keys():
    obl_types[obl_type] += insert
  else:
    obl_types[obl_type] = insert

for obl_type in obl_types.keys():
  print("\n### " + obl_type)
  for top_face in obl_types[obl_type]:
    for bot_face in obl_types[obl_type]:
      case = {
        'name': top_face['short_name'] + "_" + bot_face['short_name'],
        'top': top_face['name'],
        'bot': bot_face['name']
      }
      if (top_face['lr']):
        case['top_lr'] = top_face['lr']
      if (bot_face['lr']):
        case['bot_lr'] = bot_face['lr']
      print(case)


