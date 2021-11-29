---
title: "Case: Left Whale / Right Tent"
name: Left Whale / Right Tent
short_name: lwhale_rtent
top: Whale
top_short_name: whale
top_lr: Left
bot: Tent
bot_short_name: tent
bot_lr: Right

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
  top_bot:
    -
      name: Right Tent / Left Whale
      short_name: rtent_lwhale
  lr:
    -
      name: Right Whale / Left Tent
      short_name: rwhale_ltent
  pseudo:
    -
      name: Right Whale / Right Tent
      short_name: rwhale_rtent
    -
      name: Left Whale / Left Tent
      short_name: lwhale_ltent


---

