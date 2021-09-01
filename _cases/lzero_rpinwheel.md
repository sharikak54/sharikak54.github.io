---
name: Left Zero / Right Pinwheel
short_name: lzero_rpinwheel
top: Zero
top_short_name: zero
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 5

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,4/3,0/2,-1/4,1/-1,0"
  description: TODO
other_algs:
  -
    alg: "0,2/-2,4/0,3/-1,2/1,4/-1,0"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Left Zero
      short_name: rpinwheel_lzero
  lr:
    -
      name: Right Zero / Left Pinwheel
      short_name: rzero_lpinwheel
  pseudo:
    -
      name: Right Zero / Right Pinwheel
      short_name: rzero_rpinwheel
    -
      name: Left Zero / Left Pinwheel
      short_name: lzero_lpinwheel


---

Notes: offset zero/n; preserve top bird fully on top, and any rotation on bottom to go to angel/hammer or hammer/angel

Description TODO

