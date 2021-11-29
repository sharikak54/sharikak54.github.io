---
title: "Case: Right Pinwheel / Plane"
name: Right Pinwheel / Plane
short_name: rpinwheel_plane
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Plane
bot_short_name: plane

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,2/1,4/5,2/0,1"
  description: pair tent on top with shell on bottom to form spill/gem
color_mirror_algs:
  -
    alg: "1,0/-3,0/-1,2/1,4/-1,-4/0,1"
  -
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

# RELATED CASES
parents:
  -
    name: "Left Spill / Gem"
    short_name: "lspill_gem"
  -
    name: "Angel / Left Spill"
    short_name: "angel_lspill"
  -
    name: "Moth / Right Kite"
    short_name: "moth_rkite"
  -
    name: "Moth / Right Zero"
    short_name: "moth_rzero"
mirrors:
  top_bot:
    -
      name: Plane / Right Pinwheel
      short_name: plane_rpinwheel
  lr:
    -
      name: Left Pinwheel / Plane
      short_name: lpinwheel_plane


---

