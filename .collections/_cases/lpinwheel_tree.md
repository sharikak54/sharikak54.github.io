---
title: "Case: Left Pinwheel / Tree"
name: Left Pinwheel / Tree
short_name: lpinwheel_tree
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Tree
bot_short_name: tree

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/1,-2/-1,-4/-5,-2/-1,0"
  description: Pair tent on top with shell on bottom to form spill/gem.
color_mirror_algs:
  -
    alg: "0,-1/3,0/1,-2/-1,-4/1,4/-1,0"
  -
    alg: "0,5/0,3/1,-2/-4,-1/-5,-2/-1,0"
  -
    alg: "1,0/2,-1/0,-3/4,1/-4,-1/0,1"
  -
    alg: "-3,-4/0,3/-2,1/-1,2/0,3/0,1"
    alg: "0,5/0,3/1,-2/-4,-1/-5,-2/-1,0"
  -
    alg: "1,0/2,-1/0,-3/4,1/-4,-1/0,1"
  -
    alg: "-3,-4/0,3/-2,1/-1,2/0,3/0,1"
other_algs:
  -
    alg: "0,5/0,3/1,-2/-4,-1/1,4/-1,0"
  -
    alg: "1,0/2,-1/0,-3/4,1/2,5/0,1"
  -
    alg: "-3,2/3,0/-2,1/2,-1/0,3/0,1"
    alg: "1,0/2,-1/0,-3/4,1/2,5/0,1"
  -
    alg: "-3,2/3,0/-2,1/2,-1/0,3/0,1"

# RELATED CASES
parents:
  -
    name: "Right Spill / Gem"
    short_name: "rspill_gem"
  -
    name: "Squid / Right Spill"
    short_name: "squid_rspill"
  -
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
  -
    name: "Squid / Right Spill"
    short_name: "squid_rspill"
  -
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
mirrors:
  top_bot:
    -
      name: Tree / Left Pinwheel
      short_name: tree_lpinwheel
  lr:
    -
      name: Right Pinwheel / Tree
      short_name: rpinwheel_tree


---

