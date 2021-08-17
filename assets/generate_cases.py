from os import listdir
from os.path import isfile, join

FACE_DIR = "../_faces/"
CASE_DIR = "../_cases/"

filenames = [f for f in listdir(FACE_DIR) if isfile(join(FACE_DIR, f))]

obl_types = {}
for filename in filenames:
  with open(FACE_DIR + filename, 'r') as file1:
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
  # print("\n### " + obl_type)
  for top_face in obl_types[obl_type]:
    for bot_face in obl_types[obl_type]:
      top_face_name = top_face['name']
      bot_face_name = bot_face['name']
      case = {
        'short_name': top_face['short_name'] + "_" + bot_face['short_name'],
        'top': top_face['name'],
        'top_lr': False,
        'bot': bot_face['name'],
        'bot_lr': False,
        'type': obl_type
      }

      # LR stuff
      if (top_face['lr']):
        case['top_lr'] = top_face['lr']
        top_face_name = top_face['lr'] + " " + top_face['name']
      if (bot_face['lr']):
        case['bot_lr'] = bot_face['lr']
        bot_face_name = bot_face['lr'] + " " + bot_face['name']
      case['name'] = top_face_name + " / " + bot_face_name

      print(case)
      filename = CASE_DIR + case['short_name'] + ".md"

      contents = "---\n"
      contents += "name: {}\n".format(case['name'])
      contents += "top: {}\n".format(case['top'])
      if case['top_lr']:
        contents += "top_lr: {}\n".format(case['top_lr'])
      contents += "bot: {}\n".format(case['bot'])
      if case['bot_lr']:
        contents += "bot_lr: {}\n".format(case['bot_lr'])
      contents += "\n"
      contents += "default_alg:\n"
      contents += "  alg: \"0,0/\"\n"
      contents += "  description: TODO\n"
      contents += "other_algs:\n"
      contents += "  -\n"
      contents += "    alg: \"0,0/\"\n"
      contents += "    description: TODO\n"
      contents += "---\n"
      contents += "\n"
      contents += "Description TODO\n\n"
      with open(FACE_DIR + filename, 'w') as file1:
        lines = file1.write(contents)


