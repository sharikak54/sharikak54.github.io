---
title: "Case: Right Bunny / Right Thumb"
name: Right Bunny / Right Thumb
short_name: rbunny_rthumb
top: Bunny
top_short_name: bunny
top_lr: Right
bot: Thumb
bot_short_name: thumb
bot_lr: Right

optimal: 4

recognition: Preserving bunny/thumb; preserving tents on top and putting slice between shell and gem on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/5,-1/-3,0/0,1"
  description: Put shell of thumb in DL and align so slice preserves gem, swap isolated corner on top with gem.
other_algs:
  -
    alg: "0,-1/0,-3/4,-2/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Whale / Right Whale"
    short_name: "rwhale_rwhale"
mirrors:
  top_bot:
    -
      name: Right Thumb / Right Bunny
      short_name: rthumb_rbunny
  lr:
    -
      name: Left Bunny / Left Thumb
      short_name: lbunny_lthumb
  pseudo:
    -
      name: Left Bunny / Right Thumb
      short_name: lbunny_rthumb
    -
      name: Right Bunny / Left Thumb
      short_name: rbunny_lthumb


---

