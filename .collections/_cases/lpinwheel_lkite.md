---
title: "Case: Left Pinwheel / Left Kite"
name: Left Pinwheel / Left Kite
short_name: lpinwheel_lkite
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 3

recognition: Good pinwheel/kite - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-3,0/0,1"
  description: CO case; preserve blocks.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "3,-1/3,0/3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
mirrors:
  top_bot:
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel
  lr:
    -
      name: Right Pinwheel / Right Kite
      short_name: rpinwheel_rkite
  pseudo:
    -
      name: Right Pinwheel / Left Kite
      short_name: rpinwheel_lkite
    -
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite


---

