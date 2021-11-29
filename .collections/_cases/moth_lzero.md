---
title: "Case: Moth / Left Zero"
name: Moth / Left Zero
short_name: moth_lzero
top: Moth
top_short_name: moth
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-3,0/-1,-4/0,1"
  description: pair isolated corner on bottom with tent on top (breaking gem) to form good bird/scottie
color_mirror_algs:
  -
    alg: "0,-1/4,1/-3,0/5,2/0,1"
  -
    alg: "6,5/1,4/-3,0/2,5/0,1"
  -
    alg: "6,5/-5,-2/0,-3/-4,-1/0,1"
  -
    alg: "-3,2/-3,3/3,0/-3,0/-2,1/-1,0"
other_algs:
  -
    alg: "6,5/1,4/-3,0/-4,-1/0,1"
  -
    alg: "-3,2/-3,3/3,0/-2,1/3,6/-1,0"
  -
    alg: "3,-4/-3,3/0,3/1,-2/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
mirrors:
  top_bot:
    -
      name: Left Zero / Moth
      short_name: lzero_moth
  lr:
    -
      name: Moth / Right Zero
      short_name: moth_rzero


---

