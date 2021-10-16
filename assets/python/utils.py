from os import listdir
from os.path import isfile, join

def flipLR(lr):
  return 'r' if lr == 'l' else 'l'

def flipLeftRight(LeftRight):
  return 'Right' if LeftRight == 'Left' else 'Left'



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
    is_balanced = False
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
        has_lr = (line[8:].strip()) == "true"
      elif (line.find("is_balanced:") == 0):
        is_balanced = (line[13:].strip()) == "true"

    face = {
      'name': name,
      'short_name': short_name,
      'nickname': nickname,
      'ct_type': ct_type,
      'LR': has_lr,
      'lr': has_lr,
      'is_balanced': is_balanced
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


def computeCase(top_face, bot_face):
  '''Compute case data given a top and bottom face.'''

  ct_type = top_face['ct_type']

  top_name = top_face['name']
  bot_name = bot_face['name']
  top_short_name = top_face['short_name']
  bot_short_name = bot_face['short_name']

  case = {
    'top': top_face['name'],
    'top_short_name': top_short_name,
    'top_lr': False,
    'bot': bot_face['name'],
    'bot_short_name': bot_short_name,
    'bot_lr': False,
    'type': ct_type,
    'is_balanced': False
  }

  # LR stuff
  if (top_face['LR']):
    case['top_lr'] = top_face['LR']
    top_name = top_face['LR'] + " " + top_face['name']
    top_short_name = top_face['lr'] + top_face['short_name']
  if (bot_face['LR']):
    case['bot_lr'] = bot_face['LR']
    bot_name = bot_face['LR'] + " " + bot_face['name']
    bot_short_name = bot_face['lr'] + bot_face['short_name']

  case['name'] = top_name + " / " + bot_name
  case['short_name'] = top_short_name + "_" + bot_short_name

  # "Same" cases
  if top_face['is_balanced'] and bot_face['is_balanced']:
    case['is_balanced'] = True

  # Calculate mirrors
  case['mirrors'] = {}
  (has_top_bot_mirror, has_lr_mirror) = (False, False)
  if (case['top_short_name'] != case['bot_short_name']):
    has_top_bot_mirror = True
    case['mirrors']['top_bot'] = [{
      "name": bot_name + " / " + top_name,
      "short_name": bot_short_name + "_" + top_short_name,
    }]

  if (top_face['LR'] or bot_face['LR']):
    has_lr_mirror = True
    lr_mirror_top_name = ((flipLeftRight(top_face['LR']) + " ") if top_face['LR'] else "") + top_face['name']
    lr_mirror_bot_name = ((flipLeftRight(bot_face['LR']) + " ") if bot_face['LR'] else "") + bot_face['name']
    lr_mirror_top_short_name = ((flipLR(top_face['lr'])) if top_face['LR'] else "") + top_face['short_name']
    lr_mirror_bot_short_name = ((flipLR(bot_face['lr'])) if bot_face['LR'] else "") + bot_face['short_name']
    case['mirrors']['lr'] = [{
      "name": lr_mirror_top_name + " / " + lr_mirror_bot_name,
      "short_name": lr_mirror_top_short_name + "_" + lr_mirror_bot_short_name,
    }]

    if (top_face['LR'] and bot_face['LR']):
      has_pmirror = True
      case['mirrors']['pseudo'] = [
        {
          "name": lr_mirror_top_name + " / " + bot_name,
          "short_name": lr_mirror_top_short_name + "_" + bot_short_name,
        },
        {
          "name": top_name + " / " + lr_mirror_bot_name,
          "short_name": top_short_name + "_" + lr_mirror_bot_short_name,
        },
      ]
  
  return case


def getMirrorContents(mirrors):
  '''Helper to get yaml from dict of mirror cases.'''

  contents = "mirrors:\n"

  for mirror_type in mirrors:
    contents += "  " + mirror_type + ":\n"
    for mirror in mirrors[mirror_type]:
      contents += "    -\n"
      contents += "      name: " + mirror['name'] + "\n"
      contents += "      short_name: " + mirror['short_name'] + "\n"

  contents += "\n"

  return contents

def computeCaseFileContents(case):
  '''What to write to case file as defaults.'''

  contents = "---\n"
  contents += "title: \"Case: {}\"\n".format(case['name'])
  contents += "name: {}\n".format(case['name'])
  contents += "short_name: {}\n".format(case['short_name'])
  contents += "top: {}\n".format(case['top'])
  contents += "top_short_name: {}\n".format(case['top_short_name'])
  if case['top_lr']:
    contents += "top_lr: {}\n".format(case['top_lr'])
  contents += "bot: {}\n".format(case['bot'])
  contents += "bot_short_name: {}\n".format(case['bot_short_name'])
  if case['bot_lr']:
    contents += "bot_lr: {}\n".format(case['bot_lr'])
  contents += "\n"

  contents += "recognition: TODO\n"
  contents += "\n"

  contents += "# ALGORITHMS\n"
  contents += "default_alg:\n"
  contents += "  alg: \"1,0/5,5/0,1\"\n"
  contents += "  description: TODO\n"
  contents += "color_mirror_algs:\n"
  contents += "  -\n"
  contents += "    alg: \"0,0/\"\n"
  contents += "    description: TODO\n"
  contents += "other_algs:\n"
  contents += "  -\n"
  contents += "    alg: \"0,0/\"\n"
  contents += "    description: TODO\n"
  contents += "\n"

  contents += "# RELATED CASES\n"
  contents += "parents:\n"
  contents += "  -\n"
  contents += "    name: TODO\n"
  contents += "    short_name: TODO\n"

  if case['mirrors'].keys():
    contents += getMirrorContents(case['mirrors'])
    contents += "\n"

  contents += "---\n"
  contents += "\n"
  contents += "Description TODO\n\n"
  if case['is_balanced'] and case['name'][:5] == "Same ":
    if case['top_short_name'] == case['bot_short_name']:
      contents += "Two " + case['top'] + "s that are the same color.  "
    else:
      contents += "A " + case['top'] + " and a " + case['bot'] + " that are the same color.  "
    contents += "Be careful not to mistake this for ["+ case['name'][5:] + "]"
    contents += "(" + case['short_name'][:len(case['short_name']) - 5] + ")."
    contents += "\n\n"

  return contents