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

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/0,-3/-4,-1/0,1"
  description: TODO
color_mirror_algs:
  -
    alg: "0,-1/-5,-2/-3,0/-4,-1/0,1"
    description: TODO
  -
    alg: "0,-1/1,4/0,-3/2,5/0,1"
    description: TODO
  -
    alg: "6,5/4,1/0,-3/5,2/0,1"
    description: TODO
  -
    alg: "3,-4/-2,4/-3,0/3,0/2,-1/0,1"
    description: TODO
  -
    alg: "3,-4/-3,3/3,0/1,-2/-3,0/-1,0"
    description: TODO
other_algs:
  -
    alg: "6,5/4,1/0,-3/-1,-4/0,1"
    description: TODO
  -
    alg: "3,-4/-2,4/-3,0/3,0/-4,5/0,1"
    description: TODO
  -
    alg: "-3,2/3,-3/3,0/-2,1/-3,0/-1,0"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
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

Notes: zero/moth; optimal involves swapping isolated corner on top with whale (breaking gem) on bottom, but "blockbuilding" by pairing bird with gem is pretty fast too

Description TODO

