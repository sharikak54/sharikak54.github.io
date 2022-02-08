---
title: "Case: Right Axe / Left Axe"
name: Right Axe / Left Axe
short_name: raxe_laxe
top: Axe
top_short_name: axe
top_lr: Right
bot: Axe
bot_short_name: axe
bot_lr: Left

optimal: 5

recognition: Mirrored axes; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-2,1/-1,-1/-3,0/0,1"
  description: Swap isolated edge on top with tent on bottom, forming opposite trees.
other_algs:
  -
    alg: "1,0/-4,-1/-2,1/-1,-1/-3,0/0,1"
  -
    alg: "3,-1/4,1/2,-1/4,1/-4,-1/0,1"
    description: Put shells on left, pair tent on bottom with edge from tent on top to form gem/spill.

# RELATED CASES
parents:
  -
    name: "Tree / Tree"
    short_name: "tree_tree"
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Tie / Right Kite"
    short_name: "tie_rkite"
  -
    name: "Squid / Left Spill"
    short_name: "squid_lspill"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Tie / Right Kite"
    short_name: "tie_rkite"
  -
    name: "Squid / Left Spill"
    short_name: "squid_lspill"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
mirrors:
  lr:
    -
      name: Left Axe / Right Axe
      short_name: laxe_raxe
  pseudo:
    -
      name: Left Axe / Left Axe
      short_name: laxe_laxe
    -
      name: Right Axe / Right Axe
      short_name: raxe_raxe


---

