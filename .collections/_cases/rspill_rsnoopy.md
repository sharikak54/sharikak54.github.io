---
title: "Case: Right Spill / Right Snoopy"
name: Right Spill / Right Snoopy
short_name: rspill_rsnoopy
top: Spill
top_short_name: spill
top_lr: Right
bot: Snoopy
bot_short_name: snoopy
bot_lr: Right

optimal: 3

recognition: Good spill/snoopy; tent from spill can't exactly swap with tent from snoopy.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-4,-1/0,1"
  description: Swap only corner from spill on top with tent on bottom to make dish/dish.
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
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill
  lr:
    -
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy
  pseudo:
    -
      name: Left Spill / Right Snoopy
      short_name: lspill_rsnoopy
    -
      name: Right Spill / Left Snoopy
      short_name: rspill_lsnoopy


---

