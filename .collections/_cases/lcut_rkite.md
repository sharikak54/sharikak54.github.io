---
title: "Case: Left Cut / Right Kite"
name: Left Cut / Right Kite
short_name: lcut_rkite
top: Cut
top_short_name: cut
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 3

recognition: Good cut/kite; aligning bird with kite breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/-3,0/0,1"
  description: Preserve kite on bottom, send whale to form good tents.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "0,-1/1,1/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Right Kite / Left Cut
      short_name: rkite_lcut
  lr:
    -
      name: Right Cut / Left Kite
      short_name: rcut_lkite
  pseudo:
    -
      name: Right Cut / Right Kite
      short_name: rcut_rkite
    -
      name: Left Cut / Left Kite
      short_name: lcut_lkite


---

