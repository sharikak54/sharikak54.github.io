---
title: "Case: Left Bunny / Left Bunny"
name: Left Bunny / Left Bunny
short_name: lbunny_lbunny
top: Bunny
top_short_name: bunny
top_lr: Left
bot: Bunny
bot_short_name: bunny
bot_lr: Left

optimal: 3

recognition: Good bunnies; preserving tents preserves cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/3,-3/-4,-1/0,1"
  description: Put all 4 tents on right half of puzzle and swap them to get good thumbs.
color_mirror_algs:
  -
    alg: "1,0/-3,3/-4,-1/0,1"
  -
    alg: "1,0/3,-3/-1,-4/0,1"
  -
    alg: "-5,6/-3,3/5,2/0,1"
  -
    alg: "-5,6/3,-3/2,5/0,1"
other_algs:
  -
    alg: "1,0/-3,3/-1,-4/0,1"
  -
    alg: "-5,6/3,-3/5,2/0,1"
  -
    alg: "-5,6/-3,3/2,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  lr:
    -
      name: Right Bunny / Right Bunny
      short_name: rbunny_rbunny
  pseudo:
    -
      name: Right Bunny / Left Bunny
      short_name: rbunny_lbunny
    -
      name: Left Bunny / Right Bunny
      short_name: lbunny_rbunny


---

