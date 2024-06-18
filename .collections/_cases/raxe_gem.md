---
title: "Case: Right Axe / Gem"
name: Right Axe / Gem
short_name: raxe_gem
top: Axe
top_short_name: axe
top_lr: Right
bot: Gem
bot_short_name: gem

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/3,0/-1,0"
  description: Swap tent on top with gem on bottom, "maximally" blockbuild to get good tents.
color_mirror_algs:
  -
    alg: "0,-1/1,-2/3,0/-1,0"
  -
    alg: "6,5/-2,1/-3,6/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
mirrors:
  top_bot:
    -
      name: Gem / Right Axe
      short_name: gem_raxe
  lr:
    -
      name: Left Axe / Gem
      short_name: laxe_gem


---

