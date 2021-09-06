---
name: Right Snoopy / Left Snoopy
short_name: rsnoopy_lsnoopy
top: Snoopy
top_short_name: snoopy
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
  lr:
    -
      name: Left Snoopy / Right Snoopy
      short_name: lsnoopy_rsnoopy
  pseudo:
    -
      name: Left Snoopy / Left Snoopy
      short_name: lsnoopy_lsnoopy
    -
      name: Right Snoopy / Right Snoopy
      short_name: rsnoopy_rsnoopy


---

Description TODO

