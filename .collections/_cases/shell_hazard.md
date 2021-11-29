---
title: "Case: Shell / Hazard"
name: Shell / Hazard
short_name: shell_hazard
top: Shell
top_short_name: shell
bot: Hazard
bot_short_name: hazard

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/0,-3/-5,-2/-1,0"
  description: preserve shell on top, send tent from bottom to form good snoopy/spill
color_mirror_algs:
  -
    alg: "1,0/-1,2/0,-3/1,4/-1,0"
  -
    alg: "0,5/1,-2/0,3/-1,-4/0,1"
other_algs:
  -
    alg: "0,5/1,-2/0,3/5,2/0,1"

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Left Spill"
    short_name: "lsnoopy_lspill"
  -
    name: "Right Snoopy / Right Spill"
    short_name: "rsnoopy_rspill"
  -
    name: "Same Moth / Moth"
    short_name: "moth_moth_same"
mirrors:
  top_bot:
    -
      name: Hazard / Shell
      short_name: hazard_shell


---

