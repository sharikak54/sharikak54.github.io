---
title: "Case: Left Snoopy / Right Spill"
name: Left Snoopy / Right Spill
short_name: lsnoopy_rspill
top: Snoopy
top_short_name: snoopy
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
  top_bot:
    -
      name: Right Spill / Left Snoopy
      short_name: rspill_lsnoopy
  lr:
    -
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill
  pseudo:
    -
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill
    -
      name: Left Snoopy / Left Spill
      short_name: lsnoopy_lspill


---

