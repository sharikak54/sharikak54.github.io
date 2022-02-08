---
title: "Case: Right Kite / Right Kite"
name: Right Kite / Right Kite
short_name: rkite_rkite
top: Kite
top_short_name: kite
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 1

recognition: Good kite/kite; it's a 1-slicer :)

# ALGORITHMS
default_alg:
  alg: "1,0/-1,0"
  description: Preserve everything :)
color_mirror_algs:
  -
    alg: "samecase"
# RELATED CASES
parents:
      name: Left Kite / Left Kite
      short_name: lkite_lkite
  pseudo:
    -
      name: Left Kite / Right Kite
      short_name: lkite_rkite
    -
      name: Right Kite / Left Kite
      short_name: rkite_lkite


---

