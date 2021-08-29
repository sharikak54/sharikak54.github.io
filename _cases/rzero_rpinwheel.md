---
name: Right Zero / Right Pinwheel
short_name: rzero_rpinwheel
top: Zero
top_short_name: zero
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
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
        name: Right Pinwheel / Right Zero
        short_name: rpinwheel_rzero
  -
    type: lr
    values: 
      -
        name: Left Zero / Left Pinwheel
        short_name: lzero_lpinwheel
  -
    type: pseudo
    values: 
      -
        name: Left Zero / Right Pinwheel
        short_name: lzero_rpinwheel
      -
        name: Right Zero / Left Pinwheel
        short_name: rzero_lpinwheel


---

Description TODO

