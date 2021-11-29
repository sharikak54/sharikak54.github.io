---
title: "Case: Right Zero / Left Kite"
name: Right Zero / Left Kite
short_name: rzero_lkite
top: Zero
top_short_name: zero
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 3

recognition: Good zero/kite; aligning bird with kite breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/3,0/-1,0"
  description: Preserve kite on bottom, send whale to form tent/tent.

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
mirrors:
  top_bot:
    -
      name: Left Kite / Right Zero
      short_name: lkite_rzero
  lr:
    -
      name: Left Zero / Right Kite
      short_name: lzero_rkite
  pseudo:
    -
      name: Left Zero / Left Kite
      short_name: lzero_lkite
    -
      name: Right Zero / Right Kite
      short_name: rzero_rkite


---

