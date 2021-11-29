---
title: "Case: Eopp / Eopp"
name: Eopp / Eopp
short_name: eopp_eopp
top: Eopp
top_short_name: eopp
bot: Eopp
bot_short_name: eopp

optimal: 2

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/0,1"
  description: hold edges in FB
color_mirror_algs:
  -
    alg: "1,0/5,5/0,1"
  -
    alg: "0,-1/-5,-5/-1,0"
other_algs:
  -
    alg: "0,-1/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
---

