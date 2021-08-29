---
name: Right Zero / Right Kite
short_name: rzero_rkite
top: Zero
top_short_name: zero
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
        name: Right Kite / Right Zero
        short_name: rkite_rzero
  -
    type: lr
    values: 
      -
        name: Left Zero / Left Kite
        short_name: lzero_lkite
  -
    type: pseudo
    values: 
      -
        name: Left Zero / Right Kite
        short_name: lzero_rkite
      -
        name: Right Zero / Left Kite
        short_name: rzero_lkite


---

Description TODO

