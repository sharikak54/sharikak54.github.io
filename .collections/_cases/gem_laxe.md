---
title: "Case: Gem / Left Axe"
name: Gem / Left Axe
short_name: gem_laxe
top: Gem
top_short_name: gem
bot: Axe
bot_short_name: axe
bot_lr: Left

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/2,-1/0,1"
  description: Swap gem on top with tent on bottom, "maximally" blockbuild to get tent/tent.
color_mirror_algs:
  -
    alg: "1,0/2,-1/0,-3/0,1"
  -
    alg: "1,0/0,-3/2,-1/0,1"
  -
    alg: "1,0/-1,-4/3,0/0,1"
    alg: "1,0/0,-3/2,-1/0,1"
  -
    alg: "1,0/-1,-4/3,0/0,1"
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
      name: Left Axe / Gem
      short_name: laxe_gem
  lr:
    -
      name: Gem / Right Axe
      short_name: gem_raxe


---

