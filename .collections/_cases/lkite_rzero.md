---
title: "Case: Left Kite / Right Zero"
name: Left Kite / Right Zero
short_name: lkite_rzero
top: Kite
top_short_name: kite
top_lr: Left
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 3

recognition: Good kite/zero; aligning kite with bird breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/0,3/-1,0"
  description: Preserve kite on top, pair with whale from bottom to get tent/tent.
color_mirror_algs:
  -
    alg: "samecase"

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
      name: Right Zero / Left Kite
      short_name: rzero_lkite
  lr:
    -
      name: Right Kite / Left Zero
      short_name: rkite_lzero
  pseudo:
    -
      name: Right Kite / Right Zero
      short_name: rkite_rzero
    -
      name: Left Kite / Left Zero
      short_name: lkite_lzero


---

