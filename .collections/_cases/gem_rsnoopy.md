---
title: "Case: Gem / Right Snoopy"
name: Gem / Right Snoopy
short_name: gem_rsnoopy
top: Gem
top_short_name: gem
bot: Snoopy
bot_short_name: snoopy
bot_lr: Right

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/0,3/-1,0"
  description: Swap gem on top with tent on bottom, "maximally" blockbuild to get tent/tent.
other_algs:
  -
    alg: "0,-1/4,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
mirrors:
  top_bot:
    -
      name: Right Snoopy / Gem
      short_name: rsnoopy_gem
  lr:
    -
      name: Gem / Left Snoopy
      short_name: gem_lsnoopy


---

