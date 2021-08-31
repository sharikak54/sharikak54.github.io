---
name: Left Pinwheel / Left Kite
short_name: lpinwheel_lkite
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Left

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
  top_bot:
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel
  lr:
    -
      name: Right Pinwheel / Right Kite
      short_name: rpinwheel_rkite
  pseudo:
    -
      name: Right Pinwheel / Left Kite
      short_name: rpinwheel_lkite
    -
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite


---

Description TODO

