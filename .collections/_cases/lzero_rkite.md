---
title: "Case: Left Zero / Right Kite"
name: Left Zero / Right Kite
short_name: lzero_rkite
top: Zero
top_short_name: zero
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 3

recognition: good zero/kite; aligning bird with kite breaks squareshape

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/-3,0/0,1"
  description: preserve kite on bottom, send whale to form tent/tent

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
mirrors:
  top_bot:
    -
      name: Right Kite / Left Zero
      short_name: rkite_lzero
  lr:
    -
      name: Right Zero / Left Kite
      short_name: rzero_lkite
  pseudo:
    -
      name: Right Zero / Right Kite
      short_name: rzero_rkite
    -
      name: Left Zero / Left Kite
      short_name: lzero_lkite


---

