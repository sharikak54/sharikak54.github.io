---
title: "Case: Gem / Right Axe"
name: Gem / Right Axe
short_name: gem_raxe
top: Gem
top_short_name: gem
bot: Axe
bot_short_name: axe
bot_lr: Right

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/0,3/-1,0"
  description: Swap gem on top with tent on bottom, "maximally" blockbuild to get good tents.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/0,3/-1,0"
  -
    alg: "6,5/1,-2/6,-3/-1,0"
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
      name: Right Axe / Gem
      short_name: raxe_gem
  lr:
    -
      name: Gem / Left Axe
      short_name: gem_laxe


---

