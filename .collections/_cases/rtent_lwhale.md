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

# RELATED CASES
parents:
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
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

