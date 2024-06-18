---
title: "Case: Left Axe / Squid"
name: Left Axe / Squid
short_name: laxe_squid
top: Axe
top_short_name: axe
top_lr: Left
bot: Squid
bot_short_name: squid

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,-2/-1,-4/0,1"
  description: Put shell on top in UL, pair tent on top with whale on bottom to form good tree/tie.
other_algs:
  -
    alg: "6,5/-3,0/1,-2/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Tree / Tie"
    short_name: "tree_tie"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
  -
    name: "Right Bunny / Right Bunny"
    short_name: "rbunny_rbunny"
mirrors:
  top_bot:
    -
      name: Squid / Left Axe
      short_name: squid_laxe
  lr:
    -
      name: Right Axe / Squid
      short_name: raxe_squid


---

