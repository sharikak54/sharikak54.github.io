---
name: Right Zero / Left Kite
short_name: rzero_lkite
top: Zero
top_short_name: zero
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Left

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/5,5/0,1"
  description: TODO
color_mirror_algs:
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
      name: Left Kite / Right Zero
      short_name: lkite_rzero
  lr:
    -
      name: Left Zero / Right Kite
      short_name: lzero_rkite
  pseudo:
    -
      name: Left Zero / Left Kite
      short_name: lzero_lkite
    -
      name: Right Zero / Right Kite
      short_name: rzero_rkite


---

Description TODO
