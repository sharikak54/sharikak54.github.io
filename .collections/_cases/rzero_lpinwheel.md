---
title: "Case: Right Zero / Left Pinwheel"
name: Right Zero / Left Pinwheel
short_name: rzero_lpinwheel
top: Zero
top_short_name: zero
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 5

recognition: Bad zero/pinwheel - aligning blocks to slice breaks cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,-4/-3,0/-2,1/-4,-1/0,1"
  description: Preserve bird on tap and hold any angle on bottom to go to angel/snoopy or snoopy/angel.
other_algs:
  -
    alg: "1,0/-4,2/0,-3/-2,1/-1,-4/0,1"
  -
    alg: "1,3/-4,2/-3,0/1,-2/-4,-1/0,1"
  -
    alg: "1,3/2,-4/0,-3/1,-2/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Angel / Left Snoopy"
    short_name: "angel_lsnoopy"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Right Zero
      short_name: lpinwheel_rzero
  lr:
    -
      name: Left Zero / Right Pinwheel
      short_name: lzero_rpinwheel
  pseudo:
    -
      name: Left Zero / Left Pinwheel
      short_name: lzero_lpinwheel
    -
      name: Right Zero / Right Pinwheel
      short_name: rzero_rpinwheel


---

