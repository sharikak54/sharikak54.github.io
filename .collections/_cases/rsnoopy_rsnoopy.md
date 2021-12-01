---
title: "Case: Right Snoopy / Right Snoopy"
name: Right Snoopy / Right Snoopy
short_name: rsnoopy_rsnoopy
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Snoopy
bot_short_name: snoopy
bot_lr: Right

optimal: 5

recognition: Matching snoopies; tents can connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-4,-1/-2,1/-3,0/-1,0"
  description: Put shells on left, pair tent on bottom with isolated edge on top.
other_algs:
  -
    alg: "1,0/3,0/-4,-1/-3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Gem / Gem"
    short_name: "gem_gem"
mirrors:
  lr:
    -
      name: Left Snoopy / Left Snoopy
      short_name: lsnoopy_lsnoopy
  pseudo:
    -
      name: Left Snoopy / Right Snoopy
      short_name: lsnoopy_rsnoopy
    -
      name: Right Snoopy / Left Snoopy
      short_name: rsnoopy_lsnoopy


---

