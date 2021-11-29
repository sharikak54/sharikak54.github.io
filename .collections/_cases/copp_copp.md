---
title: "Case: Copp / Copp"
name: Copp / Copp
short_name: copp_copp
top: Copp
top_short_name: copp
bot: Copp
bot_short_name: copp

optimal: 2

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/0,1"
  description: m2; preserve gems on both sides
color_mirror_algs:
  -
    alg: "1,0/-4,-4/0,1"
  -
    alg: "3,2/4,4/-1,0"
other_algs:
  -
    alg: "3,2/-2,-2/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
---

