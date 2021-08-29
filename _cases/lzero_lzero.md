---
name: Left Zero / Left Zero
short_name: lzero_lzero
top: Zero
top_short_name: zero
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
    type: lr
    values: 
      -
        name: Right Zero / Right Zero
        short_name: rzero_rzero
  -
    type: pseudo
    values: 
      -
        name: Right Zero / Left Zero
        short_name: rzero_lzero
      -
        name: Left Zero / Right Zero
        short_name: lzero_rzero


---

Description TODO

