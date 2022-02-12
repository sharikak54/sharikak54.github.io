---
title: "Case: Right Tent / Left Whale"
name: Right Tent / Left Whale
short_name: rtent_lwhale
top: Tent
top_short_name: tent
top_lr: Right
bot: Whale
bot_short_name: whale
bot_lr: Left

optimal: 3

recognition: Good tent/whale; splitting tent on top and sandwiched tent on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/-1,-4/0,1"
  description: Split tent on top and sandwiched tent on bottom, holding both tents in front.
color_mirror_algs:
  -
    alg: "0,-1/4,1/-1,-4/0,1"
  -
    alg: "6,5/1,4/5,2/0,1"
    alg: "6,5/1,4/5,2/0,1"
    alg: "6,5/1,4/5,2/0,1"
other_algs:
  -
    alg: "6,5/4,1/5,2/0,1"
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Left Whale / Right Tent
      short_name: lwhale_rtent
  lr:
    -
      name: Left Tent / Right Whale
      short_name: ltent_rwhale
  pseudo:
    -
      name: Left Tent / Left Whale
      short_name: ltent_lwhale
    -
      name: Right Tent / Right Whale
      short_name: rtent_rwhale


---

