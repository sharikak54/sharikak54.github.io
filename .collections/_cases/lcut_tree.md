---
title: "Case: Left Cut / Tree"
name: Left Cut / Tree
short_name: lcut_tree
top: Cut
top_short_name: cut
top_lr: Left
bot: Tree
bot_short_name: tree

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/3,0/-4,-1/0,1"
  description: Preserve whale on bottom and pair with bird from top to form spill/axe.
color_mirror_algs:
  -
    alg: "0,-1/1,4/3,0/2,5/0,1"
  -
    alg: "-2,-3/0,3/-1,-1/3,0/3,0/0,1"
  -
    alg: "-2,-3/0,3/2,-1/-3,0/-3,0/0,1"
  -
    alg: "-2,-3/-1,2/1,1/3,0/2,-1/0,1"
  -
    alg: "3,-4/1,-2/-3,0/3,0/2,-1/0,1"
other_algs:
  -
    alg: "6,5/4,1/3,0/-1,-4/0,1"
  -
    alg: "4,3/3,0/-1,-1/-3,0/-3,0/0,1"
  -
    alg: "-3,2/-3,0/3,0/-3,0/-2,1/-1,0"
  -
    alg: "-2,3/-4,-1/-3,0/-2,1/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
mirrors:
  top_bot:
    -
      name: Tree / Left Cut
      short_name: tree_lcut
  lr:
    -
      name: Right Cut / Tree
      short_name: rcut_tree


---

