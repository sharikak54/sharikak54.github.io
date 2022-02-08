---
title: "Case: Right Kite / Left Cut"
name: Right Kite / Left Cut
short_name: rkite_lcut
top: Kite
top_short_name: kite
top_lr: Right
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 3

recognition: Good kite/cut; aligning kite with bird breaks squareshape.

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
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Left Cut / Right Kite
      short_name: lcut_rkite
  lr:
    -
      name: Left Kite / Right Cut
      short_name: lkite_rcut
  pseudo:
    -
      name: Left Kite / Left Cut
      short_name: lkite_lcut
    -
      name: Right Kite / Right Cut
      short_name: rkite_rcut


---

