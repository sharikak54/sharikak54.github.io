---
title: "Case: Right Pinwheel / Tie"
name: Right Pinwheel / Tie
short_name: rpinwheel_tie
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Tie
bot_short_name: tie

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-1,2/0,3/-2,1/-1,0"
  description: Create a D-color shell on bottom (as part of a tree) by pairing isolated D-color corner on bottom with D-color tent on top.
color_mirror_algs:
  -
    alg: "1,0/3,0/-1,2/3,0/-2,1/-1,0"
  -
    alg: "0,-1/1,-2/0,-3/-1,-4/4,1/-1,0"
  -
    alg: "3,-4/-2,1/-1,-4/-3,0/4,1/-1,0"
  -
    alg: "4,-3/3,0/2,-1/4,1/-1,-4/0,1"
  -
    alg: "-5,6/0,3/-1,2/0,3/4,-5/-1,0"
other_algs:
  -
    alg: "0,-1/-2,1/0,-3/-4,-1/4,1/-1,0"
  -
    alg: "3,-4/1,-2/-1,-4/0,-3/4,1/-1,0"
  -
    alg: "4,-3/0,3/2,-1/1,4/-1,-4/0,1"
  -
    alg: "-5,6/3,0/-1,2/3,0/4,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Kite / Tree"
    short_name: "rkite_tree"
  -
    name: "Right Bird / Hazard"
    short_name: "rbird_hazard"
  -
    name: "Right Bird / Shell"
    short_name: "rbird_shell"
  -
    name: "Right Cut / Tree"
    short_name: "rcut_tree"
mirrors:
  top_bot:
    -
      name: Tie / Right Pinwheel
      short_name: tie_rpinwheel
  lr:
    -
      name: Left Pinwheel / Tie
      short_name: lpinwheel_tie


---

