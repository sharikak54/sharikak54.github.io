---
title: "Case: Left Spill / Right Snoopy"
name: Left Spill / Right Snoopy
short_name: lspill_rsnoopy
top: Spill
top_short_name: spill
top_lr: Left
bot: Snoopy
bot_short_name: snoopy
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
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill
  lr:
    -
      name: Right Spill / Left Snoopy
      short_name: rspill_lsnoopy
  pseudo:
    -
      name: Right Spill / Right Snoopy
      short_name: rspill_rsnoopy
    -
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy


---

