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
color_mirror_algs:
  -
    alg: "1,0/3,0/-1,-1/3,6/0,1"

# RELATED CASES
parents:
  -
    name: "Left Zero / Right Kite"
    short_name: "lzero_rkite"
---

