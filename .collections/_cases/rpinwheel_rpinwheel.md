---
title: "Case: Right Pinwheel / Right Pinwheel"
name: Right Pinwheel / Right Pinwheel
short_name: rpinwheel_rpinwheel
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 2

recognition: Good pinwheel/pinwheel; tents can connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,-3/-1,0"
  description: CO case; preserve blocks.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "-2,3/3,3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Kite / Right Kite"
    short_name: "rkite_rkite"
mirrors:
  lr:
    -
      name: Left Pinwheel / Left Pinwheel
      short_name: lpinwheel_lpinwheel
  pseudo:
    -
      name: Left Pinwheel / Right Pinwheel
      short_name: lpinwheel_rpinwheel
    -
      name: Right Pinwheel / Left Pinwheel
      short_name: rpinwheel_lpinwheel


---

