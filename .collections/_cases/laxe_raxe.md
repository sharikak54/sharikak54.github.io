---
title: "Case: Left Axe / Right Axe"
name: Left Axe / Right Axe
short_name: laxe_raxe
top: Axe
top_short_name: axe
top_lr: Left
bot: Axe
bot_short_name: axe
bot_lr: Right

optimal: 5

recognition: Mirrored axes; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/-1,-1/-3,0/0,1"
  description: Swap isolated edge on top with tent on bottom, forming opposite trees.
other_algs:
  -
    alg: "0,-1/3,0/-2,1/-1,-1/-3,0/0,1"
  -
    alg: "-2,0/-4,-1/-2,1/-4,-1/4,1/-1,0"
    description: Put shells on left, pair tent on bottom with edge from tent on top to form gem/spill.

# RELATED CASES
parents:
  -
    name: "Tree / Tree"
    short_name: "tree_tree"
  -
    name: "Gem / Right Spill"
    short_name: "gem_rspill"
  -
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Squid / Right Spill"
    short_name: "squid_rspill"
  -
    name: "Tie / Right Cut"
    short_name: "tie_rcut"
  -
    name: "Gem / Right Spill"
    short_name: "gem_rspill"
  -
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Squid / Right Spill"
    short_name: "squid_rspill"
  -
    name: "Tie / Right Cut"
    short_name: "tie_rcut"
mirrors:
  lr:
    -
      name: Right Axe / Left Axe
      short_name: raxe_laxe
  pseudo:
    -
      name: Right Axe / Right Axe
      short_name: raxe_raxe
    -
      name: Left Axe / Left Axe
      short_name: laxe_laxe


---

