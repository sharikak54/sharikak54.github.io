---
title: "Case: Right Pinwheel / Tree"
name: Right Pinwheel / Tree
short_name: rpinwheel_tree
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Tree
bot_short_name: tree

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,2/1,4/5,2/0,1"
  description: Pair tent on top with shell on bottom to form spill/gem.
color_mirror_algs:
  -
    alg: "1,0/-3,0/-1,2/1,4/-1,-4/0,1"
  -
    alg: "1,6/0,-3/-1,2/4,1/5,2/0,1"
  -
    alg: "0,-1/-2,1/0,3/-4,-1/4,1/-1,0"
  -
    alg: "-2,3/0,-3/2,-1/1,-2/0,-3/-1,0"
    alg: "1,6/0,-3/-1,2/4,1/5,2/0,1"
  -
    alg: "0,-1/-2,1/0,3/-4,-1/4,1/-1,0"
  -
    alg: "-2,3/0,-3/2,-1/1,-2/0,-3/-1,0"
other_algs:
  -
    alg: "1,6/0,-3/-1,2/4,1/-1,-4/0,1"
  -
    alg: "0,-1/-2,1/0,3/-4,-1/-2,-5/-1,0"
  -
    alg: "-2,-3/-3,0/2,-1/-2,1/0,-3/-1,0"
    alg: "0,-1/-2,1/0,3/-4,-1/-2,-5/-1,0"
  -
    alg: "-2,-3/-3,0/2,-1/-2,1/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Spill / Gem"
    short_name: "lspill_gem"
  -
    name: "Squid / Left Spill"
    short_name: "squid_lspill"
  -
    name: "Tie / Right Kite"
    short_name: "tie_rkite"
  -
    name: "Tie / Right Cut"
    short_name: "tie_rcut"
  -
    name: "Squid / Left Spill"
    short_name: "squid_lspill"
  -
    name: "Tie / Right Kite"
    short_name: "tie_rkite"
  -
    name: "Tie / Right Cut"
    short_name: "tie_rcut"
mirrors:
  top_bot:
    -
      name: Tree / Right Pinwheel
      short_name: tree_rpinwheel
  lr:
    -
      name: Left Pinwheel / Tree
      short_name: lpinwheel_tree


---

