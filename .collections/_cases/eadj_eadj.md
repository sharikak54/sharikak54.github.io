---
title: "Case: Eadj / Eadj"
name: Eadj / Eadj
short_name: eadj_eadj
top: Eadj
top_short_name: eadj
bot: Eadj
bot_short_name: eadj

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-1,-1/-3,0/0,1"
  description: Hold edges next to slice in front, keeping the pairs together.
other_algs:
  -
    alg: "-3,-4/0,-3/1,1/0,3/-1,0"
  -
    alg: "-5,6/0,3/-1,-1/0,-3/0,1"

# RELATED CASES
parents:
  -
    name: "Left Cut / Right Kite"
    short_name: "lcut_rkite"
---

