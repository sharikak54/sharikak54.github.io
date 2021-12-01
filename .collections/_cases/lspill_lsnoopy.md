---
title: "Case: Left Spill / Left Snoopy"
name: Left Spill / Left Snoopy
short_name: lspill_lsnoopy
top: Spill
top_short_name: spill
top_lr: Left
bot: Snoopy
bot_short_name: snoopy
bot_lr: Left

optimal: 3

recognition: Good spill/snoopy; tent from spill can't exactly swap with tent from snoopy.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/4,1/-1,0"
  description: Swap only corner from spill on top with tent on bottom to make dish/dish.

# RELATED CASES
parents:
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
mirrors:
  top_bot:
    -
      name: Left Snoopy / Left Spill
      short_name: lsnoopy_lspill
  lr:
    -
      name: Right Spill / Right Snoopy
      short_name: rspill_rsnoopy
  pseudo:
    -
      name: Right Spill / Left Snoopy
      short_name: rspill_lsnoopy
    -
      name: Left Spill / Right Snoopy
      short_name: lspill_rsnoopy


---

