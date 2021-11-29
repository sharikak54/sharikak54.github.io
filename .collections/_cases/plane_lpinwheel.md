---
title: "Case: Plane / Left Pinwheel"
name: Plane / Left Pinwheel
short_name: plane_lpinwheel
top: Plane
top_short_name: plane
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,3/-2,1/-4,-1/-2,-5/-1,0"
  description: pair shell on top with a tent on bottom to form gem/spill
color_mirror_algs:
  -
    alg: "0,-1/0,3/-2,1/-4,-1/4,1/-1,0"
  -
    alg: "6,-1/3,0/-2,1/-1,-4/-2,-5/-1,0"
  -
    alg: "1,0/-1,2/-3,0/1,4/-1,-4/0,1"
  -
    alg: "-3,2/3,0/1,-2/3,0/2,-1/0,1"
other_algs:
  -
    alg: "6,-1/3,0/-2,1/-1,-4/4,1/-1,0"
  -
    alg: "1,0/-1,2/-3,0/1,4/5,2/0,1"
  -
    alg: "-3,2/3,0/1,-2/3,0/-4,5/0,1"

# RELATED CASES
parents:
  -
    name: "Gem / Right Spill"
    short_name: "gem_rspill"
  -
    name: "Right Spill / Angel"
    short_name: "rspill_angel"
  -
    name: "Left Kite / Moth"
    short_name: "lkite_moth"
  -
    name: "Left Zero / Moth"
    short_name: "lzero_moth"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Plane
      short_name: lpinwheel_plane
  lr:
    -
      name: Plane / Right Pinwheel
      short_name: plane_rpinwheel


---

