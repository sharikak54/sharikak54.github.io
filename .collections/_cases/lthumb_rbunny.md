---
title: "Case: Left Thumb / Right Bunny"
name: Left Thumb / Right Bunny
short_name: lthumb_rbunny
top: Thumb
top_short_name: thumb
top_lr: Left
bot: Bunny
bot_short_name: bunny
bot_lr: Right

optimal: 4

recognition: Breaking thumb/bunny; putting slice between shell and gem on top and preserving tents on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/0,3/1,4/-1,0"
  description: Put shell of thumb in UL and align so slice breaks gem, preserve both tents in DL (goes to good bird/scottie).
other_algs:
  -
    alg: "6,5/-3,0/0,3/4,1/-1,0"
  -
    alg: "3,5/3,0/0,-3/1,4/-1,0"
    alg: "3,5/3,0/0,-3/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Bird / Left Scottie"
    short_name: "rbird_lscottie"
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
mirrors:
  top_bot:
    -
      name: Right Bunny / Left Thumb
      short_name: rbunny_lthumb
  lr:
    -
      name: Right Thumb / Left Bunny
      short_name: rthumb_lbunny
  pseudo:
    -
      name: Right Thumb / Right Bunny
      short_name: rthumb_rbunny
    -
      name: Left Thumb / Left Bunny
      short_name: lthumb_lbunny


---

