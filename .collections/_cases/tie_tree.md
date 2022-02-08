---
title: "Case: Tie / Tree"
name: Tie / Tree
short_name: tie_tree
top: Tie
top_short_name: tie
bot: Tree
bot_short_name: tree

optimal: 3

recognition: Good tie/tree - color of tie and tree are swapped.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/2,5/0,1"
  description: Swap isolated corner on top with isolated edge on bottom.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/-4,-1/0,1"
  -
    alg: "-2,0/2,-1/4,1/-1,0"
    alg: "-2,0/2,-1/4,1/-1,0"
other_algs:
  -
    alg: "-2,0/2,-1/-2,-5/-1,0"
  -
    alg: "6,5/1,-2/-4,-1/0,1"
  -
    alg: "4,6/-2,1/4,1/-1,0"
    alg: "6,5/1,-2/-4,-1/0,1"
  -
    alg: "4,6/-2,1/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Tree / Tie
      short_name: tree_tie


---

