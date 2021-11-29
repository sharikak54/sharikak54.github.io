---
title: "Case: Moth / Moth"
name: Moth / Moth
short_name: moth_moth
top: Moth
top_short_name: moth
bot: Moth
bot_short_name: moth

optimal: 4

recognition: Opposite moth/moth; moths are of different colors.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-1,-1/-3,0/0,1"
  description: Make kite on bottom from pairing gem on top with matching isolated corner.
color_mirror_algs:
  -
    alg: "0,-1/1,-2/-1,-1/3,6/0,1"
  -
    alg: "1,0/0,-3/-1,-1/3,6/0,1"
  -
    alg: "-2,-3/-1,2/1,1/-3,6/-1,0"
  -
    alg: "-3,-4/0,3/1,1/-3,6/-1,0"
other_algs:
  -
    alg: "1,0/0,-3/-1,-1/-3,0/0,1"
  -
    alg: "-2,-3/-1,2/1,1/3,0/-1,0"
  -
    alg: "-3,-4/0,3/1,1/3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Zero / Right Kite"
    short_name: "lzero_rkite"
  -
    name: "Right Zero / Left Kite"
    short_name: "rzero_lkite"
---

