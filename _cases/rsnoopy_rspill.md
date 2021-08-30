---
name: Right Snoopy / Right Spilled Paint Can
short_name: rsnoopy_rspill
top: Snoopy
top_short_name: snoopy
top_lr: Right
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
  top_bot:
    -
      name: Right Spilled Paint Can / Right Snoopy
      short_name: rspill_rsnoopy
  lr:
    -
      name: Left Snoopy / Left Spilled Paint Can
      short_name: lsnoopy_lspill
  pseudo:
    -
      name: Left Snoopy / Right Spilled Paint Can
      short_name: lsnoopy_rspill
    -
      name: Right Snoopy / Left Spilled Paint Can
      short_name: rsnoopy_lspill


---

Description TODO

