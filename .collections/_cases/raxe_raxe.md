---
title: "Case: Right Axe / Right Axe"
name: Right Axe / Right Axe
short_name: raxe_raxe
top: Axe
top_short_name: axe
top_lr: Right
bot: Axe
bot_short_name: axe
bot_lr: Right

optimal: 5

recognition: Matching axes; tents can connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-4,-1/-2,1/-3,0/-1,0"
  description: Put shells on left, pair tent on bottom with isolated edge on top.
other_algs:
  -
    alg: "1,0/3,0/-4,-1/-3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Gem / Gem"
    short_name: "gem_gem"
mirrors:
  lr:
    -
      name: Left Axe / Left Axe
      short_name: laxe_laxe
  pseudo:
    -
      name: Left Axe / Right Axe
      short_name: laxe_raxe
    -
      name: Right Axe / Left Axe
      short_name: raxe_laxe


---

