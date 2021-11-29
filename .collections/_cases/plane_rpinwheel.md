---
title: "Case: Plane / Right Pinwheel"
name: Plane / Right Pinwheel
short_name: plane_rpinwheel
top: Plane
top_short_name: plane
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,-3/2,-1/4,1/2,5/0,1"
  description: Pair shell on top with a tent on bottom to form gem/spill.
color_mirror_algs:
  -
    alg: "1,0/0,-3/2,-1/4,1/-4,-1/0,1"
  -
    alg: "0,-1/1,-2/3,0/-1,-4/1,4/-1,0"
  -
    alg: "-2,3/0,-3/-1,2/4,1/-3,6/-1,0"
other_algs:
  -
    alg: "-5,0/-3,0/2,-1/1,4/-4,-1/0,1"
  -
    alg: "0,-1/1,-2/3,0/-1,-4/-5,-2/-1,0"
  -
    alg: "-2,3/0,-3/-1,2/4,1/3,0/-1,0/"

# RELATED CASES
parents:
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Left Spill / Angel"
    short_name: "lspill_angel"
  -
    name: "Right Kite / Moth"
    short_name: "rkite_moth"
  -
    name: "Right Zero / Moth"
    short_name: "rzero_moth"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Plane
      short_name: rpinwheel_plane
  lr:
    -
      name: Plane / Left Pinwheel
      short_name: plane_lpinwheel


---

