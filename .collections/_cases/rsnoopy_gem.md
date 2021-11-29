---
title: "Case: Right Snoopy / Gem"
name: Right Snoopy / Gem
short_name: rsnoopy_gem
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Gem
bot_short_name: gem

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/3,0/-1,0"
  description: Swap tent on top with gem on bottom, "maximally" blockbuild to get tent/tent.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
mirrors:
  top_bot:
    -
      name: Gem / Right Snoopy
      short_name: gem_rsnoopy
  lr:
    -
      name: Left Snoopy / Gem
      short_name: lsnoopy_gem


---

