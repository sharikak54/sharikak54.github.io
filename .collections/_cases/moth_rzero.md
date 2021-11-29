---
title: "Case: Moth / Right Zero"
name: Moth / Right Zero
short_name: moth_rzero
top: Moth
top_short_name: moth
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/3,0/1,4/-1,0"
  description: Pair isolated corner on bottom with tent on top (breaking gem) to form good bird/scottie.
color_mirror_algs:
  -
    alg: "1,0/-4,-1/3,0/-5,-2/-1,0"
  -
    alg: "-5,6/-1,-4/3,0/-2,-5/-1,0"
  -
    alg: "-5,6/5,2/0,3/4,1/-1,0"
  -
    alg: "4,-3/3,-3/-3,0/3,0/2,-1/0,1"
  -
    alg: "4,-3/-3,3/0,-3/2,-1/0,3/0,1"
other_algs:
  -
    alg: "-5,6/-1,-4/3,0/4,1/-1,0"
  -
    alg: "4,-3/3,-3/-3,0/2,-1/-3,6/0,1"
  -
    alg: "-2,3/-3,3/-3,0/-4,-1/-3,0/0,1"
  -
    alg: "-2,3/-3,3/-3,0/0,3/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Bird / Left Scottie"
    short_name: "rbird_lscottie"
mirrors:
  top_bot:
    -
      name: Right Zero / Moth
      short_name: rzero_moth
  lr:
    -
      name: Moth / Left Zero
      short_name: moth_lzero


---

