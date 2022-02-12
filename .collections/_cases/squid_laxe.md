---
title: "Case: Squid / Left Axe"
name: Squid / Left Axe
short_name: squid_laxe
top: Squid
top_short_name: squid
bot: Axe
bot_short_name: axe
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-2,1/-4,-1/0,1"
  description: Put shell on bottom in DL, pair tent on bottom with whale on top to form good tie/tree.

# RELATED CASES
parents:
  -
    name: "Tie / Tree"
    short_name: "tie_tree"
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
  -
    name: "Right Bunny / Right Bunny"
    short_name: "rbunny_rbunny"
mirrors:
  top_bot:
    -
      name: Left Axe / Squid
      short_name: laxe_squid
  lr:
    -
      name: Squid / Right Axe
      short_name: squid_raxe


---

