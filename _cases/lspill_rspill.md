---
name: Left Spilled Paint Can / Right Spilled Paint Can
short_name: lspill_rspill
top: Spilled Paint Can
top_short_name: spill
top_lr: Left
bot: Spilled Paint Can
bot_short_name: spill
bot_lr: Right

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,0/"
  description: TODO
mirror_algs:
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
      name: Right Spilled Paint Can / Left Spilled Paint Can
      short_name: rspill_lspill
  pseudo:
    -
      name: Right Spilled Paint Can / Right Spilled Paint Can
      short_name: rspill_rspill
    -
      name: Left Spilled Paint Can / Left Spilled Paint Can
      short_name: lspill_lspill


---

Description TODO

