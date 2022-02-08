---
title: "Case: Right Cut / Tree"
name: Right Cut / Tree
short_name: rcut_tree
top: Cut
top_short_name: cut
top_lr: Right
bot: Tree
bot_short_name: tree

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/-3,0/-2,-5/-1,0"
  description: Preserve whale on bottom and pair with bird from top to form spill/axe.
color_mirror_algs:
  -
    alg: "1,0/-1,-4/-3,0/4,1/-1,0"
  -
    alg: "-3,-4/-3,0/1,1/3,0/3,0/-1,0"
  -
    alg: "-3,-4/-3,0/-2,1/-3,0/-3,0/-1,0"
  -
    alg: "4,-3/3,0/-3,0/3,0/2,-1/0,1"
  -
    alg: "3,-4/4,1/3,0/2,-1/4,1/-1,0"
    alg: "-3,-4/-3,0/1,1/3,0/3,0/-1,0"
  -
    alg: "-3,-4/-3,0/-2,1/-3,0/-3,0/-1,0"
  -
    alg: "4,-3/3,0/-3,0/3,0/2,-1/0,1"
  -
    alg: "3,-4/4,1/3,0/2,-1/4,1/-1,0"
other_algs:
  -
    alg: "3,2/1,-2/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "3,2/1,-2/-1,-1/-3,0/-2,1/-1,0"
  -
    alg: "3,2/0,-3/1,1/-3,0/-3,0/-1,0"
  -
    alg: "-2,3/-1,2/3,0/-2,1/-3,0/-1,0"
    alg: "3,2/1,-2/-1,-1/-3,0/-2,1/-1,0"
  -
    alg: "3,2/0,-3/1,1/-3,0/-3,0/-1,0"
  -
    alg: "-2,3/-1,2/3,0/-2,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
mirrors:
  top_bot:
    -
      name: Tree / Right Cut
      short_name: tree_rcut
  lr:
    -
      name: Left Cut / Tree
      short_name: lcut_tree


---

