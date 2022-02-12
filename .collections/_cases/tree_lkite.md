---
title: "Case: Tree / Left Kite"
name: Tree / Left Kite
short_name: tree_lkite
top: Tree
top_short_name: tree
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-3,0/2,-1/0,1"
  description: Preserve D-layer shell (but not kite) in DL, swap tent on top with edge on bottom to form axe/gem.
other_algs:
  -
    alg: "1,0/3,0/-1,2/0,-3/0,1"
  -
    alg: "-5,0/-3,0/3,0/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
mirrors:
  top_bot:
    -
      name: Left Kite / Tree
      short_name: lkite_tree
  lr:
    -
      name: Tree / Right Kite
      short_name: tree_rkite


---

