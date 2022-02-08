---
title: "Case: Tree / Left Cut"
name: Tree / Left Cut
short_name: tree_lcut
top: Tree
top_short_name: tree
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-5,-2/3,0/-4,-1/0,1"
  description: Preserve D-layer bird in DL, pair whale from tree with same-color bird.
color_mirror_algs:
  -
    alg: "0,-1/4,1/0,3/-1,-4/0,1"
# RELATED CASES
parents:
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
mirrors:
  top_bot:
    -
      name: Left Cut / Tree
      short_name: lcut_tree
  lr:
    -
      name: Tree / Right Cut
      short_name: tree_rcut


---

