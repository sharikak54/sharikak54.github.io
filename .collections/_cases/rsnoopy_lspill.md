---
title: "Case: Right Snoopy / Left Spill"
name: Right Snoopy / Left Spill
short_name: rsnoopy_lspill
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Spill
bot_short_name: spill
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
      name: Left Spill / Right Snoopy
      short_name: lspill_rsnoopy
  lr:
    -
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill
  pseudo:
    -
      name: Left Snoopy / Left Spill
      short_name: lsnoopy_lspill
    -
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill


---

Description TODO

