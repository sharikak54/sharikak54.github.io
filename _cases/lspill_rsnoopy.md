---
name: Left Spilled Paint Can / Right Snoopy
short_name: lspill_rsnoopy
top: Spilled Paint Can
top_short_name: spill
top_lr: Left
bot: Snoopy
bot_short_name: snoopy
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
      name: Right Snoopy / Left Spilled Paint Can
      short_name: rsnoopy_lspill
  lr:
    -
      name: Right Spilled Paint Can / Left Snoopy
      short_name: rspill_lsnoopy
  pseudo:
    -
      name: Right Spilled Paint Can / Right Snoopy
      short_name: rspill_rsnoopy
    -
      name: Left Spilled Paint Can / Left Snoopy
      short_name: lspill_lsnoopy


---

Description TODO

