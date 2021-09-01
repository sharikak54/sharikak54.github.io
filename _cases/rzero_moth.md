---
name: Right Zero / Moth
short_name: rzero_moth
top: Zero
top_short_name: zero
top_lr: Right
bot: Moth
bot_short_name: moth

optimal: 4

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/0,3/4,1/-1,0"
  description: TODO
color_mirror_algs:
  -
    alg: "1,0/5,2/3,0/4,1/-1,0"
    description: TODO
  -
    alg: "1,0/-1,-4/0,3/-2,-5/-1,0"
    description: TODO
  -
    alg: "-5,6/-4,-1/0,3/-5,-2/-1,0"
    description: TODO
  -
    alg: "-2,3/-3,3/0,-3/-1,2/0,3/0,1"
    description: TODO
  -
    alg: "-2,3/2,-4/3,0/-2,1/-3,0/-1,0"
    description: TODO
  -
    alg: "-2,3/3,-3/-3,0/-4,-1/-3,0/0,1"
    description: TODO
other_algs:
  -
    alg: "-5,6/-4,-1/0,3/1,4/-1,0"
    description: TODO
  -
    alg: "-2,3/-3,3/0,-3/-1,2/6,-3/0,1"
    description: TODO
  -
    alg: "4,-3/-3,3/-3,0/2,-1/3,0/0,1"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
mirrors:
  top_bot:
    -
      name: Moth / Right Zero
      short_name: moth_rzero
  lr:
    -
      name: Left Zero / Moth
      short_name: lzero_moth


---

Notes: zero/moth; optimal involves swapping isolated corner on top with whale (breaking gem) on bottom, but "blockbuilding" by pairing bird with gem is pretty fast too

Description TODO

