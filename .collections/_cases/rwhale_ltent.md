---
title: "Case: Right Whale / Left Tent"
name: Right Whale / Left Tent
short_name: rwhale_ltent
top: Whale
top_short_name: whale
top_lr: Right
bot: Tent
bot_short_name: tent
bot_lr: Left

optimal: 3

recognition: Good whale/tent; splitting sandwiched tent on top and tent on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/4,1/-1,0"
  description: Split sandwiched tent on top and tent on bottom, holding both tents in front.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
mirrors:
  top_bot:
    -
      name: Left Tent / Right Whale
      short_name: ltent_rwhale
  lr:
    -
      name: Left Whale / Right Tent
      short_name: lwhale_rtent
  pseudo:
    -
      name: Left Whale / Left Tent
      short_name: lwhale_ltent
    -
      name: Right Whale / Right Tent
      short_name: rwhale_rtent


---

