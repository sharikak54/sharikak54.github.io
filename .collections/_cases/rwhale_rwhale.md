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

recognition: Good whales; whales are the same as each other.

# ALGORITHMS
default_alg:
  alg: "1,0/5,-1/-3,0/0,1"
  description: Swap both whales to form good tents.
other_algs:
  -
    alg: "1,0/-3,3/2,-1/0,1"
  -
    alg: "1,0/3,-3/-1,2/0,1"
  -
    alg: "1,0/-4,2/3,0/0,1"
  -
    alg: "1,0/2,-4/0,3/0,1"
  -
    alg: "-3,-4/4,-2/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
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

