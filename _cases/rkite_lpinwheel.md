---
name: Right Kite / Left Pinwheel
short_name: rkite_lpinwheel
top: Kite
top_short_name: kite
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
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
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite
  lr:
    -
      name: Left Kite / Right Pinwheel
      short_name: lkite_rpinwheel
  pseudo:
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel
    -
      name: Right Kite / Right Pinwheel
      short_name: rkite_rpinwheel


---

Description TODO

