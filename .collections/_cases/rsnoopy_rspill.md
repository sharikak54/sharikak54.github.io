---
title: "Case: Right Snoopy / Right Spill"
name: Right Snoopy / Right Spill
short_name: rsnoopy_rspill
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 3

recognition: Good snoopy/spill; tent from snoopy can't exactly swap with tent from spill.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-1,-4/0,1"
  description: Swap tent on top with only corner from spill on bottom to make dish/dish.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
mirrors:
  top_bot:
    -
      name: Right Spill / Right Snoopy
      short_name: rspill_rsnoopy
  lr:
    -
      name: Left Snoopy / Left Spill
      short_name: lsnoopy_lspill
  pseudo:
    -
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill
    -
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill


---

