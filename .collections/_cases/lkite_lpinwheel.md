---
title: "Case: Left Kite / Left Pinwheel"
name: Left Kite / Left Pinwheel
short_name: lkite_lpinwheel
top: Kite
top_short_name: kite
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 3

recognition: Good kite/pinwheel - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/0,3/0,3/0,1"
  description: CO case; preserve blocks.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "0,2/0,-3/0,-3/0,1"
# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Left Kite
      short_name: lpinwheel_lkite
  lr:
    -
      name: Right Kite / Right Pinwheel
      short_name: rkite_rpinwheel
  pseudo:
    -
      name: Right Kite / Left Pinwheel
      short_name: rkite_lpinwheel
    -
      name: Left Kite / Right Pinwheel
      short_name: lkite_rpinwheel


---

