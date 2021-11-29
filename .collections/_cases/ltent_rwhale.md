---
title: "Case: Left Tent / Right Whale"
name: Left Tent / Right Whale
short_name: ltent_rwhale
top: Tent
top_short_name: tent
top_lr: Left
bot: Whale
bot_short_name: whale
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
      name: Right Whale / Left Tent
      short_name: rwhale_ltent
  lr:
    -
      name: Right Tent / Left Whale
      short_name: rtent_lwhale
  pseudo:
    -
      name: Right Tent / Right Whale
      short_name: rtent_rwhale
    -
      name: Left Tent / Left Whale
      short_name: ltent_lwhale


---

