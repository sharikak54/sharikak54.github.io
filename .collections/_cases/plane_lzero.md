---
title: "Case: Plane / Left Zero"
name: Plane / Left Zero
short_name: plane_lzero
top: Plane
top_short_name: plane
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-5,-2/3,0/-4,-1/0,1"
  description: Preserve D-layer bird in DL, pair whale from plane with same-color bird.
color_mirror_algs:
  -
    alg: "0,-1/4,1/0,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Spill / Right Snoopy"
    short_name: "rspill_rsnoopy"
mirrors:
  top_bot:
    -
      name: Left Zero / Plane
      short_name: lzero_plane
  lr:
    -
      name: Plane / Right Zero
      short_name: plane_rzero


---

