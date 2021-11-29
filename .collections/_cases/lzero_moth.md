---
title: "Case: Left Zero / Moth"
name: Left Zero / Moth
short_name: lzero_moth
top: Zero
top_short_name: zero
top_lr: Left
bot: Moth
bot_short_name: moth

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/0,-3/-4,-1/0,1"
  description: pair isolated corner on top with tent on bottom (breaking gem) to form good scottie/bird
color_mirror_algs:
  -
    alg: "0,-1/-5,-2/-3,0/-4,-1/0,1"
  -
    alg: "0,-1/1,4/0,-3/2,5/0,1"
  -
    alg: "6,5/4,1/0,-3/5,2/0,1"
  -
    alg: "3,-4/-2,4/-3,0/3,0/2,-1/0,1"
  -
    alg: "3,-4/-3,3/3,0/1,-2/-3,0/-1,0"
other_algs:
  -
    alg: "6,5/4,1/0,-3/-1,-4/0,1"
  -
    alg: "3,-4/-2,4/-3,0/3,0/-4,5/0,1"
  -
    alg: "-3,2/3,-3/3,0/-2,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
mirrors:
  top_bot:
    -
      name: Moth / Left Zero
      short_name: moth_lzero
  lr:
    -
      name: Right Zero / Moth
      short_name: rzero_moth


---

