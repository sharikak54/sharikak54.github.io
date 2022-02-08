---
title: "Case: Left Axe / Gem"
name: Left Axe / Gem
short_name: laxe_gem
top: Axe
top_short_name: axe
top_lr: Left
bot: Gem
bot_short_name: gem

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-3,0/0,1"
  description: Swap tent on top with gem on bottom, "maximally" blockbuild to get tent/tent.

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
mirrors:
  top_bot:
    -
      name: Gem / Left Axe
      short_name: gem_laxe
  lr:
    -
      name: Right Axe / Gem
      short_name: raxe_gem


---

