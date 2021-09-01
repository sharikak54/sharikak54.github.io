---
name: Left Spill / Left Spill
short_name: lspill_lspill
top: Spill
top_short_name: spill
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
  lr:
    -
      name: Right Spill / Right Spill
      short_name: rspill_rspill
  pseudo:
    -
      name: Right Spill / Left Spill
      short_name: rspill_lspill
    -
      name: Left Spill / Right Spill
      short_name: lspill_rspill


---

Description TODO

