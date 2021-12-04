---
title: "Case: Right Kite / Left Zero"
name: Right Kite / Left Zero
short_name: rkite_lzero
top: Kite
top_short_name: kite
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 3

recognition: Good kite/zero; aligning kite with bird breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/0,-3/0,1"
  description: Preserve kite on top, pair with whale from bottom to get tent/tent.
color_mirror_algs:
  -
    alg: "samecase"

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
      name: Left Zero / Right Kite
      short_name: lzero_rkite
  lr:
    -
      name: Left Kite / Right Zero
      short_name: lkite_rzero
  pseudo:
    -
      name: Left Kite / Left Zero
      short_name: lkite_lzero
    -
      name: Right Kite / Right Zero
      short_name: rkite_rzero


---

