---
title: "Case: Left Spill / Right Spill"
name: Left Spill / Right Spill
short_name: lspill_rspill
top: Spill
top_short_name: spill
top_lr: Left
bot: Spill
bot_short_name: spill
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
  lr:
    -
      name: Right Spill / Left Spill
      short_name: rspill_lspill
  pseudo:
    -
      name: Right Spill / Right Spill
      short_name: rspill_rspill
    -
      name: Left Spill / Left Spill
      short_name: lspill_lspill


---

Description TODO

