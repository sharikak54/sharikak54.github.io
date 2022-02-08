---
title: "Case: Right Kite / Tree"
name: Right Kite / Tree
short_name: rkite_tree
top: Kite
top_short_name: kite
top_lr: Right
bot: Tree
bot_short_name: tree

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/-3,6/-1,0"
  description: Send tent on top to pair with shell on bottom to form axe/gem.
color_mirror_algs:
  -
    alg: "1,0/2,-1/-2,1/3,0/-1,0"
  -
    alg: "-5,6/-1,2/-2,1/6,-3/-1,0"
  -
    alg: "-5,6/5,-4/1,-2/0,3/-1,0"
    alg: "-5,6/5,-4/1,-2/0,3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
mirrors:
  top_bot:
    -
      name: Tree / Right Kite
      short_name: tree_rkite
  lr:
    -
      name: Left Kite / Tree
      short_name: lkite_tree


---

