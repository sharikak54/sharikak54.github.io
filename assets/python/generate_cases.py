from utils import getFacesByECType, computeCase, computeCaseFileContents, SHOULD_OVERWRITE_CURRENT_FILES

OVERWRITE_CURRENT_FILES = SHOULD_OVERWRITE_CURRENT_FILES()

CASE_DIR = "../../.collections/_cases/"



'''
Generate the base case files for each case.
Run this script FIRST before importing any other new data.
'''



ct_types = getFacesByECType()

for ct_type in ct_types.keys():
  print("\n### " + ct_type)
  for top_face in ct_types[ct_type]:
    print(top_face)
    for bot_face in ct_types[ct_type]:
      print(bot_face)

      case = computeCase(top_face, bot_face)
      contents = computeCaseFileContents(case)

      if OVERWRITE_CURRENT_FILES:
        filename = CASE_DIR + case['short_name'] + ".md"
        with open(filename, 'w') as file1:
          lines = file1.write(contents)
      
      if (top_face['is_balanced'] and bot_face['is_balanced']):
        same_case = case
        same_case['name'] = "Same " + case['name']
        same_case['short_name'] = case['short_name'] + "_same"

        same_contents = computeCaseFileContents(same_case)

        if OVERWRITE_CURRENT_FILES:
          filename = CASE_DIR + same_case['short_name'] + ".md"
          with open(filename, 'w') as file1:
            lines = file1.write(same_contents)


