---
title: "Case: Tree / Right Kite"
name: Tree / Right Kite
short_name: tree_rkite
top: Tree
top_short_name: tree
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/3,0/-2,1/-1,0"
  description: Preserve D-layer shell (but not kite) in DL, swap tent on top with edge on bottom to form axe/gem.
other_algs:
  -
    alg: "0,-1/-3,0/4,1/-3,0/-1,0"
  -
    alg: "0,-1/-3,0/1,-2/0,3/-1,0"
  -
    alg: "6,-1/3,0/-3,0/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
mirrors:
  top_bot:
    -
      name: Right Kite / Tree
      short_name: rkite_tree
  lr:
    -
      name: Tree / Left Kite
      short_name: tree_lkite


---

