---
title: "Case: Left Tent / Left Tent"
name: Left Tent / Left Tent
short_name: ltent_ltent
top: Tent
top_short_name: tent
top_lr: Left
bot: Tent
bot_short_name: tent
bot_lr: Left

optimal: 2

recognition: Good tents; aligning tents next to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/0,1"
  description: CO case; preserve blocks.
other_algs:
  -
    alg: "3,2/3,0/0,1"
  -
    alg: "4,3/2,-1/0,1"
  -
    alg: "so"
  -
    alg: "many"
  -
    alg: "others"
    alg: "4,3/2,-1/0,1"
  -
    alg: "so"
  -
    alg: "many"
  -
    alg: "others"
    alg: "4,3/2,-1/0,1"
  -
    alg: "so"
  -
    alg: "many"
  -
    alg: "others"

# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
mirrors:
  lr:
    -
      name: Right Tent / Right Tent
      short_name: rtent_rtent
  pseudo:
    -
      name: Right Tent / Left Tent
      short_name: rtent_ltent
    -
      name: Left Tent / Right Tent
      short_name: ltent_rtent


---

