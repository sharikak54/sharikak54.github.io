---
title: "Case: Right Axe / Squid"
name: Right Axe / Squid
short_name: raxe_squid
top: Axe
top_short_name: axe
top_lr: Right
bot: Squid
bot_short_name: squid

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-1,2/1,4/-1,0"
  description: Put shell on top in UL, pair tent on top with whale on bottom to form good tree/tie.
other_algs:
  -
    alg: "-5,6/3,0/-1,2/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Tree / Tie"
    short_name: "tree_tie"
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
  -
    name: "Left Bunny / Left Bunny"
    short_name: "lbunny_lbunny"
mirrors:
  top_bot:
    -
      name: Squid / Right Axe
      short_name: squid_raxe
  lr:
    -
      name: Left Axe / Squid
      short_name: laxe_squid


---

