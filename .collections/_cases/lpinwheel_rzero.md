---
title: "Case: Left Pinwheel / Right Zero"
name: Left Pinwheel / Right Zero
short_name: lpinwheel_rzero
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 5

recognition: Bad pinwheel/zero - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,2/-3,0/-2,1/-4,-1/0,1"
  description: Hold any angle on top and preserve bird on bottom to go to snoopy/angel.
other_algs:
  -
    alg: "-2,0/-4,2/0,-3/1,-2/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Angel"
    short_name: "lsnoopy_angel"
mirrors:
  top_bot:
    -
      name: Right Zero / Left Pinwheel
      short_name: rzero_lpinwheel
  lr:
    -
      name: Right Pinwheel / Left Zero
      short_name: rpinwheel_lzero
  pseudo:
    -
      name: Right Pinwheel / Right Zero
      short_name: rpinwheel_rzero
    -
      name: Left Pinwheel / Left Zero
      short_name: lpinwheel_lzero


---

