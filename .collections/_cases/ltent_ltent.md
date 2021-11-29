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

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/5,5/0,1"
  description: TODO
color_mirror_algs:
  -
    alg: "0,0/"
    description: TODO
other_algs:
  -
    alg: "0,0/"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
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

