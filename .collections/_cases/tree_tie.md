---
title: "Case: Tree / Tie"
name: Tree / Tie
short_name: tree_tie
top: Tree
top_short_name: tree
bot: Tie
bot_short_name: tie

optimal: 3

recognition: Good tree/tie - color of tree and tie are swapped.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/-5,-2/-1,0"
  description: Swap isolated edge on top with isolated corner on bottom.
color_mirror_algs:
  -
    alg: "1,0/-1,2/1,4/-1,0"
  -
    alg: "0,2/1,-2/-1,-4/0,1"
    alg: "0,2/1,-2/-1,-4/0,1"
other_algs:
  -
    alg: "0,2/1,-2/5,2/0,1"
  -
    alg: "-5,6/2,-1/1,4/-1,0"
  -
    alg: "6,-4/-2,1/-1,-4/0,1"
    alg: "-5,6/2,-1/1,4/-1,0"
  -
    alg: "6,-4/-2,1/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Tie / Tree
      short_name: tie_tree


---

