---
name: Right Tent / Left Whale
short_name: rtent_lwhale
top: Tent
top_short_name: tent
top_lr: Right
bot: Whale
bot_short_name: whale
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
  top_bot:
    -
      name: Left Whale / Right Tent
      short_name: lwhale_rtent
  lr:
    -
      name: Left Tent / Right Whale
      short_name: ltent_rwhale
  pseudo:
    -
      name: Left Tent / Left Whale
      short_name: ltent_lwhale
    -
      name: Right Tent / Right Whale
      short_name: rtent_rwhale


---

Description TODO

