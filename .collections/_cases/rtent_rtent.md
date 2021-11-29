---
title: "Case: Right Tent / Right Tent"
name: Right Tent / Right Tent
short_name: rtent_rtent
top: Tent
top_short_name: tent
top_lr: Right
bot: Tent
bot_short_name: tent
bot_lr: Right

optimal: 2

recognition: Good tent/tent; aligning tents next to slice preserves squareshape

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,0"
  description: CO case; preserve blocks.
color_mirror_algs:
  -
    alg: "1,0/3,6/-1,0"
  -
    alg: "-2,-3/6,-3/-1,0"
  -
    alg: "6,5/-5,4/-1,0"
  -
    alg: "so"
  -
    alg: "many"
  -
    alg: "others"
other_algs:
  -
    alg: "0,-1/-2,1/-1,0"
  -
    alg: "-2,-3/0,3/-1,0"
  -
    alg: "so"
  -
    alg: "many"
  -
    alg: "others"

# RELATED CASES
parents:
  -
    name: "Right Kite / Right Kite"
    short_name: "rkite_rkite"
mirrors:
  lr:
    -
      name: Left Tent / Left Tent
      short_name: ltent_ltent
  pseudo:
    -
      name: Left Tent / Right Tent
      short_name: ltent_rtent
    -
      name: Right Tent / Left Tent
      short_name: rtent_ltent


---

