---
title: "Case: Tree / Right Cut"
name: Tree / Right Cut
short_name: tree_rcut
top: Tree
top_short_name: tree
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/5,2/-3,0/4,1/-1,0"
  description: Preserve D-layer bird in DL, pair whale from tree with same-color bird.
color_mirror_algs:
  -
    alg: "1,0/-4,-1/0,-3/1,4/-1,0"
# RELATED CASES
parents:
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
mirrors:
  top_bot:
    -
      name: Right Cut / Tree
      short_name: rcut_tree
  lr:
    -
      name: Tree / Left Cut
      short_name: tree_lcut


---

