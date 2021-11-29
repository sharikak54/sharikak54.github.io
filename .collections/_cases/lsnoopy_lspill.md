---
title: "Case: Left Snoopy / Left Spill"
name: Left Snoopy / Left Spill
short_name: lsnoopy_lspill
top: Snoopy
top_short_name: snoopy
top_lr: Left
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 3

recognition: good snoopy/spill; tent from snoopy can't exactly swap with tent from spill

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,4/-1,0"
  description: swap tent on top with only corner from spill on bottom to make dish/dish
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
mirrors:
  top_bot:
    -
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy
  lr:
    -
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill
  pseudo:
    -
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill
    -
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill


---

