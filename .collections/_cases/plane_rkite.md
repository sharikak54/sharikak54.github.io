---
title: "Case: Plane / Right Kite"
name: Plane / Right Kite
short_name: plane_rkite
top: Plane
top_short_name: plane
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,-2/-3,6/-1,0"
  description: preserve D-layer shell (but not kite) in DL, swap tent on top with edge on bottom to form snoopy/gem
color_mirror_algs:
  -
    alg: "0,-1/-3,0/3,0/-2,1/-1,0"
  -
    alg: "0,-1/-3,0/4,1/-3,0/-1,0"
  -
    alg: "0,-1/-3,0/1,-2/0,3/-1,0"
other_algs:
  -
    alg: "0,-1/0,-3/3,0/-5,4/-1,0"
  -
    alg: "0,-1/0,-3/4,1/6,3/-1,0"
  -
    alg: "6,-1/0,3/-3,0/-5,-2/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Gem"
    short_name: "rsnoopy_gem"
  -
    name: "Left Snoopy / Left Spill"
    short_name: "lsnoopy_lspill"
mirrors:
  top_bot:
    -
      name: Right Kite / Plane
      short_name: rkite_plane
  lr:
    -
      name: Plane / Left Kite
      short_name: plane_lkite


---

