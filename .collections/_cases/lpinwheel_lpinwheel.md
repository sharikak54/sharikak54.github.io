---
title: "Case: Left Pinwheel / Left Pinwheel"
name: Left Pinwheel / Left Pinwheel
short_name: lpinwheel_lpinwheel
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 2

recognition: good pinwheel/pinwheel; tents can connect to form kites

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,-3/0,1"
  description: CO, make kite/kite
other_algs:
  -
    alg: "3,2/3,3/0,1"

# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
mirrors:
  lr:
    -
      name: Right Pinwheel / Right Pinwheel
      short_name: rpinwheel_rpinwheel
  pseudo:
    -
      name: Right Pinwheel / Left Pinwheel
      short_name: rpinwheel_lpinwheel
    -
      name: Left Pinwheel / Right Pinwheel
      short_name: lpinwheel_rpinwheel


---

