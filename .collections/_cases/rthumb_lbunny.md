---
title: "Case: Right Thumb / Left Bunny"
name: Right Thumb / Left Bunny
short_name: rthumb_lbunny
top: Thumb
top_short_name: thumb
top_lr: Right
bot: Bunny
bot_short_name: bunny
bot_lr: Left

optimal: 4

recognition: Breaking thumb/bunny; putting slice between shell and gem on top and preserving tents on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/0,-3/-1,-4/0,1"
  description: Put shell of thumb in UL and align so slice breaks gem, preserve both tents in DL (goes to good bird/scottie).
other_algs:
  -
    alg: "-5,6/3,0/0,-3/-4,-1/0,1"
  -
    alg: "-2,6/-3,0/0,3/-1,-4/0,1"
    alg: "-2,6/-3,0/0,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
mirrors:
  top_bot:
    -
      name: Left Bunny / Right Thumb
      short_name: lbunny_rthumb
  lr:
    -
      name: Left Thumb / Right Bunny
      short_name: lthumb_rbunny
  pseudo:
    -
      name: Left Thumb / Left Bunny
      short_name: lthumb_lbunny
    -
      name: Right Thumb / Right Bunny
      short_name: rthumb_rbunny


---

