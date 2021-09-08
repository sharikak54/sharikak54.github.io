from os import listdir
from os.path import isfile, join

def flipLR(lr):
  return 'r' if lr == 'l' else 'l'

def flipLeftRight(LeftRight):
  return 'Right' if LeftRight == 'Left' else 'Left'


def getMirrorContents(mirrors):
  '''Get yaml from dict of mirror cases.'''

  contents = "mirrors:\n"

  for mirror_type in mirrors:
    contents += "  " + mirror_type + ":\n"
    for mirror in mirrors[mirror_type]:
      contents += "    -\n"
      contents += "      name: " + mirror['name'] + "\n"
      contents += "      short_name: " + mirror['short_name'] + "\n"

  contents += "\n"

  return contents



def getFacesByECType():
  '''Compute all faces from the ./_faces folder, sorting by edge/corner counts.'''

  FACE_DIR = "../../.collections/_faces/"

  filenames = [f for f in listdir(FACE_DIR) if isfile(join(FACE_DIR, f))]

  ct_types = {}
  for filename in filenames:
    with open(FACE_DIR + filename, 'r') as file1:
      lines = file1.readlines()
    
    name = False
    short_name = False
    nickname = False
    ct_type = False
    has_lr = False
    for line in lines:
      if (line.find("name:") == 0):
        name = line[6:].strip()
      elif (line.find("short_name:") == 0):
        short_name = line[12:].strip()
      elif (line.find("nickname:") == 0):
        nickname = line[10:].strip()
      elif (line.find("type:") == 0):
        ct_type = line[6:].strip()
      elif (line.find("has_lr:") == 0):
        has_lr = line[8:].strip()

    face = {
      'name': name,
      'short_name': short_name,
      'nickname': nickname,
      'ct_type': ct_type,
      'LR': has_lr,
      'lr': has_lr
    }

    if (face['LR']):
      lface = face.copy()
      lface['lr_short_name'] = "l" + face['short_name']
      lface['LR'] = "Left"
      lface['lr'] = "l"
      rface = face.copy()
      rface['lr_short_name'] = "r" + face['short_name']
      rface['LR'] = "Right"
      rface['lr'] = "r"
      insert = [lface, rface]
    else:
      insert = [face]

    if ct_type in ct_types.keys():
      ct_types[ct_type] += insert
    else:
      ct_types[ct_type] = insert
  
  return ct_types

