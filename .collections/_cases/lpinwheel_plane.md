---
title: "Case: Left Pinwheel / Plane"
name: Left Pinwheel / Plane
short_name: lpinwheel_plane
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Plane
bot_short_name: plane

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
other_algs:
  -
    alg: "0,5/0,3/1,-2/-4,-1/1,4/-1,0"
  -
    alg: "1,0/2,-1/0,-3/4,1/2,5/0,1"
  -
    alg: "-3,2/3,0/-2,1/2,-1/0,3/0,1"

# RELATED CASES
parents:
  -
    name: "Right Spill / Gem"
    short_name: "rspill_gem"
  -
    name: "Angel / Right Spill"
    short_name: "angel_rspill"
  -
    name: "Moth / Left Kite"
    short_name: "moth_lkite"
  -
    name: "Moth / Left Zero"
    short_name: "moth_lzero"
mirrors:
  top_bot:
    -
      name: Plane / Left Pinwheel
      short_name: plane_lpinwheel
  lr:
    -
      name: Right Pinwheel / Plane
      short_name: rpinwheel_plane


---

