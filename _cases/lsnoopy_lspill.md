---
name: Left Snoopy / Left Spilled Paint Can
short_name: lsnoopy_lspill
top: Snoopy
top_short_name: snoopy
top_lr: Left
bot: Spilled Paint Can
bot_short_name: spill
bot_lr: Left

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
  -
    type: top_bot
    values: 
      -
        name: Left Spilled Paint Can / Left Snoopy
        short_name: lspill_lsnoopy
  -
    type: lr
    values: 
      -
        name: Right Snoopy / Right Spilled Paint Can
        short_name: rsnoopy_rspill
  -
    type: pseudo
    values: 
      -
        name: Right Snoopy / Left Spilled Paint Can
        short_name: rsnoopy_lspill
      -
        name: Left Snoopy / Right Spilled Paint Can
        short_name: lsnoopy_rspill


---

Description TODO

