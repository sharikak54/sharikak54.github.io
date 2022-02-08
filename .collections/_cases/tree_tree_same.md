---
title: "Case: Same Tree / Tree"
name: Same Tree / Tree
short_name: tree_tree_same
top: Tree
top_short_name: tree
bot: Tree
bot_short_name: tree

optimal: 3

recognition: Matching trees; trees are the same color.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,-1/0,1"
  description: Solve CO into M2.
color_mirror_algs:
  -
    alg: "1,0/0,3/-1,-1/0,1"
  -
    alg: "0,-1/0,3/1,1/-1,0"
    alg: "0,-1/0,3/1,1/-1,0"
other_algs:
  -
    alg: "0,-1/-3,0/1,1/-1,0"
# RELATED CASES
parents:
  -
    name: "Eopp / Eopp"
    short_name: "eopp_eopp"
---

Two Trees that are the same color.  Be careful not to mistake this for [Tree / Tree](tree_tree).

