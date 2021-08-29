---
name: Left Kite / Left Kite
short_name: lkite_lkite
top: Kite
top_short_name: kite
top_lr: Left
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
        name: Right Kite / Right Kite
        short_name: rkite_rkite
  -
    type: pseudo
    values: 
      -
        name: Right Kite / Left Kite
        short_name: rkite_lkite
      -
        name: Left Kite / Right Kite
        short_name: lkite_rkite


---

Description TODO

