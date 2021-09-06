---
name: Right Kite / Right Zero
short_name: rkite_rzero
top: Kite
top_short_name: kite
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Right

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
      name: Right Zero / Right Kite
      short_name: rzero_rkite
  lr:
    -
      name: Left Kite / Left Zero
      short_name: lkite_lzero
  pseudo:
    -
      name: Left Kite / Right Zero
      short_name: lkite_rzero
    -
      name: Right Kite / Left Zero
      short_name: rkite_lzero


---

Description TODO
