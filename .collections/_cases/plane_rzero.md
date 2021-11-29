---
title: "Case: Plane / Right Zero"
name: Plane / Right Zero
short_name: plane_rzero
top: Plane
top_short_name: plane
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/5,2/-3,0/4,1/-1,0"
  description: Preserve D-layer bird in DL, pair whale from plane with same-color bird.
color_mirror_algs:
  -
    alg: "1,0/-4,-1/0,-3/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
mirrors:
  top_bot:
    -
      name: Right Zero / Plane
      short_name: rzero_plane
  lr:
    -
      name: Plane / Left Zero
      short_name: plane_lzero


---

