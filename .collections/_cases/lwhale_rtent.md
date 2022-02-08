---
title: "Case: Left Whale / Right Tent"
name: Left Whale / Right Tent
short_name: lwhale_rtent
top: Whale
top_short_name: whale
top_lr: Left
bot: Tent
bot_short_name: tent
bot_lr: Right

optimal: 3

recognition: Good whale/tent; splitting sandwiched tent on top and tent on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-4,-1/0,1"
  description: Split sandwiched tent on top and tent on bottom, holding both tents in front.

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Right Tent / Left Whale
      short_name: rtent_lwhale
  lr:
    -
      name: Right Whale / Left Tent
      short_name: rwhale_ltent
  pseudo:
    -
      name: Right Whale / Right Tent
      short_name: rwhale_rtent
    -
      name: Left Whale / Left Tent
      short_name: lwhale_ltent


---

