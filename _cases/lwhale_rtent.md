---
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
    type: top_bot
    values: 
      -
        name: Right Tent / Left Whale
        short_name: rtent_lwhale
  -
    type: lr
    values: 
      -
        name: Right Whale / Left Tent
        short_name: rwhale_ltent
  -
    type: pseudo
    values: 
      -
        name: Right Whale / Right Tent
        short_name: rwhale_rtent
      -
        name: Left Whale / Left Tent
        short_name: lwhale_ltent


---

Description TODO

