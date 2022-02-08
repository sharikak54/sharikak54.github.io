---
title: "Case: Left Axe / Left Axe"
name: Left Axe / Left Axe
short_name: laxe_laxe
top: Axe
top_short_name: axe
top_lr: Left
bot: Axe
bot_short_name: axe
bot_lr: Left

optimal: 5

recognition: Matching axes; tents can connect to form kites.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/4,1/3,0/2,-1/0,1"
  description: Put shells on left, pair tent on bottom with isolated edge on top.

# RELATED CASES
parents:
  -
    name: "Gem / Gem"
    short_name: "gem_gem"
mirrors:
  lr:
    -
      name: Right Axe / Right Axe
      short_name: raxe_raxe
  pseudo:
    -
      name: Right Axe / Left Axe
      short_name: raxe_laxe
    -
      name: Left Axe / Right Axe
      short_name: laxe_raxe


---

