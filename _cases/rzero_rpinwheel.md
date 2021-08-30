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
      name: Right Pinwheel / Right Zero
      short_name: rpinwheel_rzero
  lr:
    -
      name: Left Zero / Left Pinwheel
      short_name: lzero_lpinwheel
  pseudo:
    -
      name: Left Zero / Right Pinwheel
      short_name: lzero_rpinwheel
    -
      name: Right Zero / Left Pinwheel
      short_name: rzero_lpinwheel


---

Description TODO

