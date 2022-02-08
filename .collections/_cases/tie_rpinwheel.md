---
title: "Case: Tie / Right Pinwheel"
name: Tie / Right Pinwheel
short_name: tie_rpinwheel
top: Tie
top_short_name: tie
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/2,-1/1,-2/3,0/-1,0"
  description: Create a shell on top (as part of a tree) with the isolated corner on top and a tent on bottom.
color_mirror_algs:
  -
    alg: "1,0/0,3/2,-1/-2,1/3,0/-1,0"
  -
    alg: "0,-1/-2,1/-3,0/-4,-1/1,4/-1,0"
  -
    alg: "-2,3/0,3/-1,2/1,4/-4,-1/0,1"
  -
    alg: "-3,2/1,-2/-4,-1/0,-3/1,4/-1,0"
  -
    alg: "-5,6/3,0/2,-1/1,-2/-3,6/-1,0"
    alg: "0,-1/-2,1/-3,0/-4,-1/1,4/-1,0"
  -
    alg: "-2,3/0,3/-1,2/1,4/-4,-1/0,1"
  -
    alg: "-3,2/1,-2/-4,-1/0,-3/1,4/-1,0"
  -
    alg: "-5,6/3,0/2,-1/1,-2/-3,6/-1,0"
other_algs:
  -
    alg: "0,-1/1,-2/-3,0/-1,-4/1,4/-1,0"
  -
    alg: "-2,3/3,0/-1,2/4,1/-4,-1/0,1"
  -
    alg: "-3,2/-2,1/-4,-1/-3,0/1,4/-1,0"
  -
    alg: "-5,6/0,3/2,-1/-2,1/-3,6/-1,0"
    alg: "-2,3/3,0/-1,2/4,1/-4,-1/0,1"
  -
    alg: "-3,2/-2,1/-4,-1/-3,0/1,4/-1,0"
  -
    alg: "-5,6/0,3/2,-1/-2,1/-3,6/-1,0"

# RELATED CASES
parents:
  -
    name: "Tree / Right Kite"
    short_name: "tree_rkite"
  -
    name: "Hazard / Right Bird"
    short_name: "hazard_rbird"
  -
    name: "Shell / Right Bird"
    short_name: "shell_rbird"
  -
    name: "Tree / Right Cut"
    short_name: "tree_rcut"
  -
    name: "Hazard / Right Bird"
    short_name: "hazard_rbird"
  -
    name: "Shell / Right Bird"
    short_name: "shell_rbird"
  -
    name: "Tree / Right Cut"
    short_name: "tree_rcut"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Tie
      short_name: rpinwheel_tie
  lr:
    -
      name: Tie / Left Pinwheel
      short_name: tie_lpinwheel


---

