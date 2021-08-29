def flipLR(lr):
  return 'r' if lr == 'l' else 'l'

def flipLeftRight(LeftRight):
  return 'Right' if LeftRight == 'Left' else 'Left'



def getMirrorContents(mirrors):
  contents = "mirrors:\n"

  for mirror_type in mirrors:
    contents += "  -\n"
    contents += "    type: " + mirror_type + "\n"
    contents += "    values: \n"

    for mirror in mirrors[mirror_type]:
      contents += "      -\n"
      contents += "        name: " + mirror['name'] + "\n"
      contents += "        short_name: " + mirror['short_name'] + "\n"

  contents += "\n"

  return contents
