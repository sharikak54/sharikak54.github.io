---
title: "Case: Right Zero / Plane"
name: Right Zero / Plane
short_name: rzero_plane
top: Zero
top_short_name: zero
top_lr: Right
bot: Plane
bot_short_name: plane

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/-3,0/-2,-5/-1,0"
  description: Preserve whale on bottom and pair with bird from top to form spill/snoopy.
color_mirror_algs:
  -
    alg: "1,0/-1,-4/-3,0/4,1/-1,0"
  -
    alg: "-3,-4/-3,0/1,1/3,0/3,0/-1,0"
  -
    alg: "-3,-4/-3,0/-2,1/-3,0/-3,0/-1,0"
  -
    alg: "4,-3/3,0/-3,0/3,0/2,-1/0,1"
  -
    alg: "3,-4/4,1/3,0/2,-1/4,1/-1,0"
other_algs:
  -
    alg: "3,2/1,-2/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "3,2/1,-2/-1,-1/-3,0/-2,1/-1,0"
  -
    alg: "3,2/0,-3/1,1/-3,0/-3,0/-1,0"
  -
    alg: "-2,3/-1,2/3,0/-2,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
mirrors:
  top_bot:
    -
      name: Plane / Right Zero
      short_name: plane_rzero
  lr:
    -
      name: Left Zero / Plane
      short_name: lzero_plane


---

