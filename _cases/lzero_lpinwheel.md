---
name: Left Zero / Left Pinwheel
short_name: lzero_lpinwheel
top: Zero
top_short_name: zero
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
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
        name: Left Pinwheel / Left Zero
        short_name: lpinwheel_lzero
  -
    type: lr
    values: 
      -
        name: Right Zero / Right Pinwheel
        short_name: rzero_rpinwheel
  -
    type: pseudo
    values: 
      -
        name: Right Zero / Left Pinwheel
        short_name: rzero_lpinwheel
      -
        name: Left Zero / Right Pinwheel
        short_name: lzero_rpinwheel


---

Description TODO

