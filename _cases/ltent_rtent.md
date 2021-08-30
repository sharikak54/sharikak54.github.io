---
name: Left Tent / Right Tent
short_name: ltent_rtent
top: Tent
top_short_name: tent
top_lr: Left
bot: Tent
bot_short_name: tent
bot_lr: Right

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/5,5/0,1"
  description: TODO
mirror_algs:
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
      name: Right Tent / Left Tent
      short_name: rtent_ltent
  pseudo:
    -
      name: Right Tent / Right Tent
      short_name: rtent_rtent
    -
      name: Left Tent / Left Tent
      short_name: ltent_ltent


---

Description TODO

