---
title: "Case: Left Pinwheel / Tie"
name: Left Pinwheel / Tie
short_name: lpinwheel_tie
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Tie
bot_short_name: tie

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,-2/0,-3/2,-1/0,1"
  description: Create a D-color shell on bottom (as part of a tree) by pairing isolated D-color corner on bottom with D-color tent on top.
color_mirror_algs:
  -
    alg: "0,-1/-3,0/1,-2/-3,0/2,-1/0,1"
  -
    alg: "1,0/-1,2/0,3/1,4/-4,-1/0,1"
  -
    alg: "-2,3/2,-1/1,4/3,0/-4,-1/0,1"
  -
    alg: "-3,2/-3,0/-2,1/-4,-1/1,4/-1,0"
  -
    alg: "6,5/0,-3/1,-2/0,-3/-4,5/0,1"
other_algs:
  -
    alg: "1,0/2,-1/0,3/4,1/-4,-1/0,1"
  -
    alg: "-2,3/-1,2/1,4/0,3/-4,-1/0,1"
  -
    alg: "-3,2/0,-3/-2,1/-1,-4/1,4/-1,0"
  -
    alg: "6,5/-3,0/1,-2/-3,0/-4,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Kite / Tree"
    short_name: "lkite_tree"
  -
    name: "Left Bird / Hazard"
    short_name: "lbird_hazard"
  -
    name: "Left Bird / Shell"
    short_name: "lbird_shell"
  -
    name: "Left Cut / Tree"
    short_name: "lcut_tree"
mirrors:
  top_bot:
    -
      name: Tie / Left Pinwheel
      short_name: tie_lpinwheel
  lr:
    -
      name: Right Pinwheel / Tie
      short_name: rpinwheel_tie


---

