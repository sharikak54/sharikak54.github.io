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
  alg: "1,0/-1,2/0,-3/1,4/-1,0"
  description: Preserve shell on top, send tent from bottom to form good axe/spill.
other_algs:
  -
    alg: "0,5/1,-2/0,3/-1,-4/0,1"
  -
    alg: "4,-3/0,3/0,3/-4,-1/0,1"
  -
    alg: "-3,-4/0,-3/0,-3/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
mirrors:
  top_bot:
    -
      name: Hazard / Shell
      short_name: hazard_shell


---

