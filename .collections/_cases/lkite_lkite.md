---
title: "Case: Left Kite / Left Kite"
name: Left Kite / Left Kite
short_name: lkite_lkite
top: Kite
top_short_name: kite
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 1

recognition: Good kites; it's a 1-slicer :)

# ALGORITHMS
default_alg:
  alg: "0,-1/0,1"
  description: Preserve everything :)
color_mirror_algs:
  -
    alg: "samecase"

# RELATED CASES
parents:
mirrors:
  lr:
    -
      name: Right Kite / Right Kite
      short_name: rkite_rkite
  pseudo:
    -
      name: Right Kite / Left Kite
      short_name: rkite_lkite
    -
      name: Left Kite / Right Kite
      short_name: lkite_rkite


---

