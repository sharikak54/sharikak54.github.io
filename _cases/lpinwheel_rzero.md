---
name: Left Pinwheel / Right Zero
short_name: lpinwheel_rzero
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Zero
bot_short_name: zero
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
        name: Right Zero / Left Pinwheel
        short_name: rzero_lpinwheel
  -
    type: lr
    values: 
      -
        name: Right Pinwheel / Left Zero
        short_name: rpinwheel_lzero
  -
    type: pseudo
    values: 
      -
        name: Right Pinwheel / Right Zero
        short_name: rpinwheel_rzero
      -
        name: Left Pinwheel / Left Zero
        short_name: lpinwheel_lzero


---

Description TODO

