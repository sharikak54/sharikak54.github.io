---
title: "Case: Left Kite / Tree"
name: Left Kite / Tree
short_name: lkite_tree
top: Kite
top_short_name: kite
top_lr: Left
bot: Tree
bot_short_name: tree

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/2,-1/3,6/0,1"
  description: Send tent on top to pair with shell on bottom to form axe/gem.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/2,-1/-3,0/0,1"
  -
    alg: "6,5/1,-2/2,-1/6,3/0,1"
  -
    alg: "6,5/-5,4/-1,2/0,-3/0,1"
  -
    alg: "6,5/-5,4/-3,0/2,-1/0,1"
    alg: "6,5/-5,4/-1,2/0,-3/0,1"
  -
    alg: "6,5/-5,4/-3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
mirrors:
  top_bot:
    -
      name: Tree / Left Kite
      short_name: tree_lkite
  lr:
    -
      name: Right Kite / Tree
      short_name: rkite_tree


---

