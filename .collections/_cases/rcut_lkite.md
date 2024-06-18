---
title: "Case: Right Cut / Left Kite"
name: Right Cut / Left Kite
short_name: rcut_lkite
top: Cut
top_short_name: cut
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 3

recognition: Good cut/kite; aligning bird with kite breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/3,0/-1,0"
  description: Preserve kite on bottom, send whale to form good tents.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "1,0/-1,-1/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Left Kite / Right Cut
      short_name: lkite_rcut
  lr:
    -
      name: Left Cut / Right Kite
      short_name: lcut_rkite
  pseudo:
    -
      name: Left Cut / Left Kite
      short_name: lcut_lkite
    -
      name: Right Cut / Right Kite
      short_name: rcut_rkite


---

