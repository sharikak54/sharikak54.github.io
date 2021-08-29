---
name: Right Kite / Left Kite
short_name: rkite_lkite
top: Kite
top_short_name: kite
top_lr: Right
bot: Kite
bot_short_name: kite
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
    type: lr
    values: 
      -
        name: Left Kite / Right Kite
        short_name: lkite_rkite
  -
    type: pseudo
    values: 
      -
        name: Left Kite / Left Kite
        short_name: lkite_lkite
      -
        name: Right Kite / Right Kite
        short_name: rkite_rkite


---

Description TODO

