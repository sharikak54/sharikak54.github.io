---
name: Left Tent / Left Whale
short_name: ltent_lwhale
top: Tent
top_short_name: tent
top_lr: Left
bot: Whale
bot_short_name: whale
bot_lr: Left

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
        name: Left Whale / Left Tent
        short_name: lwhale_ltent
  -
    type: lr
    values: 
      -
        name: Right Tent / Right Whale
        short_name: rtent_rwhale
  -
    type: pseudo
    values: 
      -
        name: Right Tent / Left Whale
        short_name: rtent_lwhale
      -
        name: Left Tent / Right Whale
        short_name: ltent_rwhale


---

Description TODO

