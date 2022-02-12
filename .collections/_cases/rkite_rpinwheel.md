---
title: "Case: Right Kite / Right Pinwheel"
name: Right Kite / Right Pinwheel
short_name: rkite_rpinwheel
top: Kite
top_short_name: kite
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 3

recognition: Good kite/pinwheel - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/0,3/-1,0"
  description: CO case; preserve blocks.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "1,3/0,-3/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Right Kite
      short_name: rpinwheel_rkite
  lr:
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel
  pseudo:
    -
      name: Left Kite / Right Pinwheel
      short_name: lkite_rpinwheel
    -
      name: Right Kite / Left Pinwheel
      short_name: rkite_lpinwheel


---

