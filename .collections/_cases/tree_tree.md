---
title: "Case: Tree / Tree"
name: Tree / Tree
short_name: tree_tree
top: Tree
top_short_name: tree
bot: Tree
bot_short_name: tree

optimal: 4

recognition: Opposite trees; trees are of different colors.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/-1,-1/3,6/0,1"
  description: Hold D-layer shell in DL, and hold same-color corners in UL ("anti-CO") to go to good cut/kite; I prefer misaligning D-layer.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/-1,-1/-3,0/0,1"
  -
    alg: "1,0/2,-1/1,1/3,0/-1,0"
  -
    alg: "-5,6/-1,2/1,1/0,3/-1,0"
    alg: "1,0/2,-1/1,1/3,0/-1,0"
  -
    alg: "-5,6/-1,2/1,1/0,3/-1,0"
other_algs:
  -
    alg: "1,0/2,-1/1,1/-3,6/-1,0"
  -
    alg: "-5,6/-1,2/1,1/6,-3/-1,0"
    alg: "-5,6/-1,2/1,1/6,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Cut / Right Kite"
    short_name: "lcut_rkite"
  -
    name: "Right Cut / Left Kite"
    short_name: "rcut_lkite"
  -
    name: "Right Cut / Left Kite"
    short_name: "rcut_lkite"
---

