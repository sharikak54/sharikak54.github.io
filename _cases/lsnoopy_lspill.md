---
name: Left Snoopy / Left Spill
short_name: lsnoopy_lspill
top: Snoopy
top_short_name: snoopy
top_lr: Left
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
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy
  lr:
    -
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill
  pseudo:
    -
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill
    -
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill


---

Description TODO

