---
name: Left Kite / Left Zero
short_name: lkite_lzero
top: Kite
top_short_name: kite
top_lr: Left
bot: Zero
bot_short_name: zero
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
        name: Left Zero / Left Kite
        short_name: lzero_lkite
  -
    type: lr
    values: 
      -
        name: Right Kite / Right Zero
        short_name: rkite_rzero
  -
    type: pseudo
    values: 
      -
        name: Right Kite / Left Zero
        short_name: rkite_lzero
      -
        name: Left Kite / Right Zero
        short_name: lkite_rzero


---

Description TODO

