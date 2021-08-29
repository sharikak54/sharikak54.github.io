---
name: Right Pinwheel / Right Kite
short_name: rpinwheel_rkite
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Kite
bot_short_name: kite
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
        name: Right Kite / Right Pinwheel
        short_name: rkite_rpinwheel
  -
    type: lr
    values: 
      -
        name: Left Pinwheel / Left Kite
        short_name: lpinwheel_lkite
  -
    type: pseudo
    values: 
      -
        name: Left Pinwheel / Right Kite
        short_name: lpinwheel_rkite
      -
        name: Right Pinwheel / Left Kite
        short_name: rpinwheel_lkite


---

Description TODO

