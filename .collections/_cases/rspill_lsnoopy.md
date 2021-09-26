---
title: "Case: Right Spill / Left Snoopy"
name: Right Spill / Left Snoopy
short_name: rspill_lsnoopy
top: Spill
top_short_name: spill
top_lr: Right
bot: Snoopy
bot_short_name: snoopy
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
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill
  lr:
    -
      name: Left Spill / Right Snoopy
      short_name: lspill_rsnoopy
  pseudo:
    -
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy
    -
      name: Right Spill / Right Snoopy
      short_name: rspill_rsnoopy


---

Description TODO

