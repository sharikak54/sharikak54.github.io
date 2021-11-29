---
title: "Case: Plane / Left Kite"
name: Plane / Left Kite
short_name: plane_lkite
top: Plane
top_short_name: plane
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-1,2/3,6/0,1"
  description: preserve D-layer shell (but not kite) in DL, swap tent on top with edge on bottom to form snoopy/gem
color_mirror_algs:
  -
    alg: "1,0/3,0/-3,0/2,-1/0,1"
  -
    alg: "1,0/3,0/-1,2/0,-3/0,1"
  -
    alg: "-5,0/-3,0/3,0/-4,-1/0,1"
other_algs:
  -
    alg: "1,0/0,3/-3,0/5,-4/0,1"
  -
    alg: "-5,0/0,-3/3,0/5,2/0,1"

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Gem"
    short_name: "lsnoopy_gem"
  -
    name: "Right Snoopy / Right Spill"
    short_name: "rsnoopy_rspill"
mirrors:
  top_bot:
    -
      name: Left Kite / Plane
      short_name: lkite_plane
  lr:
    -
      name: Plane / Right Kite
      short_name: plane_rkite


---

