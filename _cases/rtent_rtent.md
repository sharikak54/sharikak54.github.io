---
name: Right Tent / Right Tent
short_name: rtent_rtent
top: Tent
top_short_name: tent
top_lr: Right
bot: Tent
bot_short_name: tent
bot_lr: Right

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,0/"
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
  -
    type: lr
    values: 
      -
        name: Left Tent / Left Tent
        short_name: ltent_ltent
  -
    type: pseudo
    values: 
      -
        name: Left Tent / Right Tent
        short_name: ltent_rtent
      -
        name: Right Tent / Left Tent
        short_name: rtent_ltent


---

Description TODO

