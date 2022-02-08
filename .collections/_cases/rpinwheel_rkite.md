---
title: "Case: Right Pinwheel / Right Kite"
name: Right Pinwheel / Right Kite
short_name: rpinwheel_rkite
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 3

recognition: Good pinwheel/kite - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-3,0/-1,0"
  description: CO case; preserve blocks.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "-2,0/3,0/3,0/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Kite / Right Kite"
    short_name: "rkite_rkite"
mirrors:
  top_bot:
    -
      name: Right Kite / Right Pinwheel
      short_name: rkite_rpinwheel
  lr:
    -
      name: Left Pinwheel / Left Kite
      short_name: lpinwheel_lkite
  pseudo:
    -
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite
    -
      name: Right Pinwheel / Left Kite
      short_name: rpinwheel_lkite


---

