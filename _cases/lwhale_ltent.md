---
name: Left Whale / Left Tent
short_name: lwhale_ltent
top: Whale
top_short_name: whale
top_lr: Left
bot: Tent
bot_short_name: tent
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
        name: Left Tent / Left Whale
        short_name: ltent_lwhale
  -
    type: lr
    values: 
      -
        name: Right Whale / Right Tent
        short_name: rwhale_rtent
  -
    type: pseudo
    values: 
      -
        name: Right Whale / Left Tent
        short_name: rwhale_ltent
      -
        name: Left Whale / Right Tent
        short_name: lwhale_rtent


---

Description TODO

