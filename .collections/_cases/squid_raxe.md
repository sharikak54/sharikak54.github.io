---
title: "Case: Squid / Right Axe"
name: Squid / Right Axe
short_name: squid_raxe
top: Squid
top_short_name: squid
bot: Axe
bot_short_name: axe
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/2,-1/4,1/-1,0"
  description: Put shell on bottom in DL, pair tent on bottom with whale on top to form good tie/tree.

# RELATED CASES
parents:
  -
    name: "Tie / Tree"
    short_name: "tie_tree"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Left Bunny / Left Bunny"
    short_name: "lbunny_lbunny"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Left Bunny / Left Bunny"
    short_name: "lbunny_lbunny"
mirrors:
  top_bot:
    -
      name: Right Axe / Squid
      short_name: raxe_squid
  lr:
    -
      name: Squid / Left Axe
      short_name: squid_laxe


---

