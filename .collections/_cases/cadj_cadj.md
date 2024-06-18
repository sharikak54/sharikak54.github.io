---
title: "Case: Cadj / Cadj"
name: Cadj / Cadj
short_name: cadj_cadj
top: Cadj
top_short_name: cadj
bot: Cadj
bot_short_name: cadj

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,-1/-3,0/0,1"
  description: Hold corners next to slice in front, keeping them together.
other_algs:
  -
    alg: "1,0/-4,-1/1,1/-4,-1/0,1"
  -
    alg: "6,5/0,3/1,1/0,3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Cut / Left Cut"
    short_name: "lcut_lcut"
---

