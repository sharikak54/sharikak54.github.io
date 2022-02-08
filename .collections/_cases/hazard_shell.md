---
title: "Case: Hazard / Shell"
name: Hazard / Shell
short_name: hazard_shell
top: Hazard
top_short_name: hazard
bot: Shell
bot_short_name: shell

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/3,0/2,5/0,1"
  description: Preserve shell on bottom, send tent from top to form good spill/axe.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/3,0/-4,-1/0,1"
  -
    alg: "-5,0/2,-1/-3,0/4,1/-1,0"
    alg: "-5,0/2,-1/-3,0/4,1/-1,0"
other_algs:
  -
    alg: "-5,0/2,-1/-3,0/-2,-5/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
mirrors:
  top_bot:
    -
      name: Shell / Hazard
      short_name: shell_hazard


---

