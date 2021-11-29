---
title: "Case: Gem / Left Snoopy"
name: Gem / Left Snoopy
short_name: gem_lsnoopy
top: Gem
top_short_name: gem
bot: Snoopy
bot_short_name: snoopy
bot_lr: Left

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/2,-1/0,1"
  description: Swap gem on top with tent on bottom, "maximally" blockbuild to get tent/tent.
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "1,0/-4,-1/3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
mirrors:
  top_bot:
    -
      name: Left Snoopy / Gem
      short_name: lsnoopy_gem
  lr:
    -
      name: Gem / Right Snoopy
      short_name: gem_rsnoopy


---

