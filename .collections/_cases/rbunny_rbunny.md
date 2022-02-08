---
title: "Case: Right Bunny / Right Bunny"
name: Right Bunny / Right Bunny
short_name: rbunny_rbunny
top: Bunny
top_short_name: bunny
top_lr: Right
bot: Bunny
bot_short_name: bunny
bot_lr: Right

optimal: 3

recognition: Good bunnies; preserving tents preserves cubeshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,3/4,1/-1,0"
  description: Put all 4 tents on right half of puzzle and swap them to get good thumbs.
other_algs:
  -
    alg: "0,-1/3,-3/1,4/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  lr:
    -
      name: Left Bunny / Left Bunny
      short_name: lbunny_lbunny
  pseudo:
    -
      name: Left Bunny / Right Bunny
      short_name: lbunny_rbunny
    -
      name: Right Bunny / Left Bunny
      short_name: rbunny_lbunny


---

