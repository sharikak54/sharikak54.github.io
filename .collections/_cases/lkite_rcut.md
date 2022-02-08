---
title: "Case: Left Kite / Right Cut"
name: Left Kite / Right Cut
short_name: lkite_rcut
top: Kite
top_short_name: kite
top_lr: Left
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 3

recognition: Good kite/cut; aligning kite with bird breaks squareshape.

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
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Right Cut / Left Kite
      short_name: rcut_lkite
  lr:
    -
      name: Right Kite / Left Cut
      short_name: rkite_lcut
  pseudo:
    -
      name: Right Kite / Right Cut
      short_name: rkite_rcut
    -
      name: Left Kite / Left Cut
      short_name: lkite_lcut


---

