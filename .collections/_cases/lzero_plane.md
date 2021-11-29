---
title: "Case: Left Zero / Plane"
name: Left Zero / Plane
short_name: lzero_plane
top: Zero
top_short_name: zero
top_lr: Left
bot: Plane
bot_short_name: plane

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/3,0/2,5/0,1"
  description: preserve whale on bottom and pair with bird from top to form spill/snoopy
color_mirror_algs:
  -
    alg: "0,-1/1,4/3,0/-4,-1/0,1"
  -
    alg: "4,3/3,0/-1,-1/-3,0/-3,0/0,1"
  -
    alg: "-3,2/-3,0/3,0/-3,0/-2,1/-1,0"
  -
    alg: "-2,3/-4,-1/-3,0/-2,1/-4,-1/0,1"
other_algs:
  -
    alg: "-2,-3/0,3/-1,-1/3,0/3,0/0,1"
  -
    alg: "-2,-3/0,3/2,-1/-3,0/-3,0/0,1"
  -
    alg: "-2,-3/-1,2/1,1/3,0/2,-1/0,1"
  -
    alg: "3,-4/1,-2/-3,0/3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Spill / Right Snoopy"
    short_name: "rspill_rsnoopy"
mirrors:
  top_bot:
    -
      name: Plane / Left Zero
      short_name: plane_lzero
  lr:
    -
      name: Right Zero / Plane
      short_name: rzero_plane


---

