---
title: "Case: Right Thumb / Right Bunny"
name: Right Thumb / Right Bunny
short_name: rthumb_rbunny
top: Thumb
top_short_name: thumb
top_lr: Right
bot: Bunny
bot_short_name: bunny
bot_lr: Right

optimal: 4

recognition: Preserving thumb/bunny; putting slice between shell and gem on top and preserving tents on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/5,-1/-3,0/0,1"
  description: Put shell of thumb in UL and align so slice preserves gem, swap gem with isolated corner on bottom.
other_algs:
  -
    alg: "0,-1/-3,0/4,-2/-4,-1/0,1"
  -
    alg: "0,-1/-3,0/-2,4/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Whale / Right Whale"
    short_name: "rwhale_rwhale"
mirrors:
  top_bot:
    -
      name: Right Bunny / Right Thumb
      short_name: rbunny_rthumb
  lr:
    -
      name: Left Thumb / Left Bunny
      short_name: lthumb_lbunny
  pseudo:
    -
      name: Left Thumb / Right Bunny
      short_name: lthumb_rbunny
    -
      name: Right Thumb / Left Bunny
      short_name: rthumb_lbunny


---

