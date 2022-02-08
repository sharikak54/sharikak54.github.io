---
title: "Case: Left Bunny / Left Thumb"
name: Left Bunny / Left Thumb
short_name: lbunny_lthumb
top: Bunny
top_short_name: bunny
top_lr: Left
bot: Thumb
bot_short_name: thumb
bot_lr: Left

optimal: 4

recognition: Preserving bunny/thumb; preserving tents on top and putting slice between shell and gem on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-5,1/3,0/-1,0"
  description: Put shell of thumb in DL and align so slice preserves gem, swap isolated corner on top with gem.

# RELATED CASES
parents:
  -
    name: "Left Whale / Left Whale"
    short_name: "lwhale_lwhale"
mirrors:
  top_bot:
    -
      name: Left Thumb / Left Bunny
      short_name: lthumb_lbunny
  lr:
    -
      name: Right Bunny / Right Thumb
      short_name: rbunny_rthumb
  pseudo:
    -
      name: Right Bunny / Left Thumb
      short_name: rbunny_lthumb
    -
      name: Left Bunny / Right Thumb
      short_name: lbunny_rthumb


---

