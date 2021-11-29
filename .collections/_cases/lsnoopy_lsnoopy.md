---
title: "Case: Left Snoopy / Left Snoopy"
name: Left Snoopy / Left Snoopy
short_name: lsnoopy_lsnoopy
top: Snoopy
top_short_name: snoopy
top_lr: Left
bot: Snoopy
bot_short_name: snoopy
bot_lr: Left

optimal: 5

recognition: Matching snoopies; tents can connect to form kites.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/4,1/3,0/2,-1/0,1"
  description: Put shells on left, pair tent on bottom with isolated edge on top.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Gem / Gem"
    short_name: "gem_gem"
mirrors:
  lr:
    -
      name: Right Snoopy / Right Snoopy
      short_name: rsnoopy_rsnoopy
  pseudo:
    -
      name: Right Snoopy / Left Snoopy
      short_name: rsnoopy_lsnoopy
    -
      name: Left Snoopy / Right Snoopy
      short_name: lsnoopy_rsnoopy


---

