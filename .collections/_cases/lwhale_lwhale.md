---
title: "Case: Left Whale / Left Whale"
name: Left Whale / Left Whale
short_name: lwhale_lwhale
top: Whale
top_short_name: whale
top_lr: Left
bot: Whale
bot_short_name: whale
bot_lr: Left

optimal: 3

recognition: Good whales; whales are the same as each other.

# ALGORITHMS
default_alg:
  alg: "0,-1/-5,1/3,0/-1,0"
  description: Swap both whales to form good tents.
other_algs:
  -
    alg: "0,-1/-3,3/1,-2/-1,0"
  -
    alg: "0,-1/3,-3/-2,1/-1,0"
  -
    alg: "0,-1/4,-2/-3,0/-1,0"
  -
    alg: "0,-1/-2,4/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  lr:
    -
      name: Right Whale / Right Whale
      short_name: rwhale_rwhale
  pseudo:
    -
      name: Right Whale / Left Whale
      short_name: rwhale_lwhale
    -
      name: Left Whale / Right Whale
      short_name: lwhale_rwhale


---

