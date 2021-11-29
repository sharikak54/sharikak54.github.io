---
title: "Case: Left Kite / Plane"
name: Left Kite / Plane
short_name: lkite_plane
top: Kite
top_short_name: kite
top_lr: Left
bot: Plane
bot_short_name: plane

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/2,-1/3,6/0,1"
  description: Send tent on top to pair with shell on bottom to form snoopy/gem.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/2,-1/-3,0/0,1"
other_algs:
  -
    alg: "6,5/1,-2/2,-1/6,3/0,1"
  -
    alg: "6,5/-5,4/-1,2/0,-3/0,1"
  -
    alg: "6,5/-5,4/-3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Gem"
    short_name: "lsnoopy_gem"
  -
    name: "Right Spill / Right Snoopy"
    short_name: "rspill_rsnoopy"
mirrors:
  top_bot:
    -
      name: Plane / Left Kite
      short_name: plane_lkite
  lr:
    -
      name: Right Kite / Plane
      short_name: rkite_plane


---

