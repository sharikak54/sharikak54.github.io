---
title: "Case: Left Tent / Right Whale"
name: Left Tent / Right Whale
short_name: ltent_rwhale
top: Tent
top_short_name: tent
top_lr: Left
bot: Whale
bot_short_name: whale
bot_lr: Right

optimal: 3

recognition: Good tent/whale; splitting tent on top and sandwiched tent on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/1,4/-1,0"
  description: Split tent on top and sandwiched tent on bottom, holding both tents in front.
color_mirror_algs:
  -
    alg: "1,0/-4,-1/1,4/-1,0"
  -
    alg: "-5,6/-1,-4/-5,-2/-1,0"
  -
    alg: "-5,6/5,2/-2,-5/-1,0"
    alg: "-5,6/-1,-4/-5,-2/-1,0"
  -
    alg: "-5,6/5,2/-2,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Right Whale / Left Tent
      short_name: rwhale_ltent
  lr:
    -
      name: Right Tent / Left Whale
      short_name: rtent_lwhale
  pseudo:
    -
      name: Right Tent / Right Whale
      short_name: rtent_rwhale
    -
      name: Left Tent / Left Whale
      short_name: ltent_lwhale


---

