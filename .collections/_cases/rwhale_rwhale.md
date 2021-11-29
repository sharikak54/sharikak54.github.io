---
title: "Case: Right Whale / Right Whale"
name: Right Whale / Right Whale
short_name: rwhale_rwhale
top: Whale
top_short_name: whale
top_lr: Right
bot: Whale
bot_short_name: whale
bot_lr: Right

optimal: 3

recognition: good whale/whale; whales are the same as each other

# ALGORITHMS
default_alg:
  alg: "1,0/5,-1/-3,0/0,1"
  description: swap both whales to form tent/tent
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "1,0/-3,3/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
mirrors:
  lr:
    -
      name: Left Whale / Left Whale
      short_name: lwhale_lwhale
  pseudo:
    -
      name: Left Whale / Right Whale
      short_name: lwhale_rwhale
    -
      name: Right Whale / Left Whale
      short_name: rwhale_lwhale


---

