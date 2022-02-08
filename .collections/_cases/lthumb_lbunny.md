---
title: "Case: Left Thumb / Left Bunny"
name: Left Thumb / Left Bunny
short_name: lthumb_lbunny
top: Thumb
top_short_name: thumb
top_lr: Left
bot: Bunny
bot_short_name: bunny
bot_lr: Left

optimal: 4

recognition: Preserving thumb/bunny; putting slice between shell and gem on top and preserving tents on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/-5,1/3,0/-1,0"
  description: Put shell of thumb in UL and align so slice preserves gem, swap gem with isolated corner on bottom.
other_algs:
  -
    alg: "1,0/3,0/-4,2/4,1/-1,0"
# RELATED CASES
parents:
  -
    name: "Left Whale / Left Whale"
    short_name: "lwhale_lwhale"
mirrors:
  top_bot:
    -
      name: Left Bunny / Left Thumb
      short_name: lbunny_lthumb
  lr:
    -
      name: Right Thumb / Right Bunny
      short_name: rthumb_rbunny
  pseudo:
    -
      name: Right Thumb / Left Bunny
      short_name: rthumb_lbunny
    -
      name: Left Thumb / Right Bunny
      short_name: lthumb_rbunny


---

