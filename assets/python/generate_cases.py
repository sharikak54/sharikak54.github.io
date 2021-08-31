from utils import flipLR, flipLeftRight, getMirrorContents, getFacesByECType

# COMMENT THIS OUT TO RUN
# WARNING: this script overwrites a ton of files,
# make sure you know what you're doing
quit()

CASE_DIR = "../../_cases/"

ct_types = getFacesByECType()

for ct_type in ct_types.keys():
  print("\n### " + ct_type)
  for top_face in ct_types[ct_type]:
    print(top_face)
    for bot_face in ct_types[ct_type]:
      print(bot_face)
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
        'type': ct_type
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

      filename = CASE_DIR + case['short_name'] + ".md"

      contents = "---\n"
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
      contents += "mirror_algs:\n"
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

      with open(filename, 'w') as file1:
        lines = file1.write(contents)


