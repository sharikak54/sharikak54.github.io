---
title: "Case: Moth / Left Pinwheel"
name: Moth / Left Pinwheel
short_name: moth_lpinwheel
top: Moth
top_short_name: moth
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-2,1/-1,2/-3,0/0,1"
  description: Create a shell on top (as part of a plane) with the isolated corner on top and a tent on bottom.
color_mirror_algs:
  -
    alg: "0,-1/0,-3/-2,1/2,-1/-3,0/0,1"
  -
    alg: "1,0/2,-1/3,0/4,1/-1,-4/0,1"
  -
    alg: "3,-4/0,-3/1,-2/-1,-4/4,1/-1,0"
  -
    alg: "4,-3/-1,2/4,1/0,3/-1,-4/0,1"
  -
    alg: "6,5/-3,0/-2,1/-1,2/3,6/0,1"
other_algs:
  -
    alg: "1,0/-1,2/3,0/1,4/-1,-4/0,1"
  -
    alg: "3,-4/-3,0/1,-2/-4,-1/4,1/-1,0"
  -
    alg: "4,-3/2,-1/4,1/3,0/-1,-4/0,1"
  -
    alg: "6,5/0,-3/-2,1/2,-1/3,6/0,1"

# RELATED CASES
parents:
  -
    name: "Plane / Left Kite"
    short_name: "plane_lkite"
  -
    name: "Hazard / Left Bird"
    short_name: "hazard_lbird"
  -
    name: "Shell / Left Bird"
    short_name: "shell_lbird"
  -
    name: "Plane / Left Zero"
    short_name: "plane_lzero"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Moth
      short_name: lpinwheel_moth
  lr:
    -
      name: Moth / Right Pinwheel
      short_name: moth_rpinwheel


---

