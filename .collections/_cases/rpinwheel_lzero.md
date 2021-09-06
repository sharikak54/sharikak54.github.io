---
name: Right Pinwheel / Left Zero
short_name: rpinwheel_lzero
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Zero
bot_short_name: zero
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
      name: Left Zero / Right Pinwheel
      short_name: lzero_rpinwheel
  lr:
    -
      name: Left Pinwheel / Right Zero
      short_name: lpinwheel_rzero
  pseudo:
    -
      name: Left Pinwheel / Left Zero
      short_name: lpinwheel_lzero
    -
      name: Right Pinwheel / Right Zero
      short_name: rpinwheel_rzero


---

Description TODO
