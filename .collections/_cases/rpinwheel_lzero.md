---
title: "Case: Right Pinwheel / Left Zero"
name: Right Pinwheel / Left Zero
short_name: rpinwheel_lzero
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 5

recognition: bad pinwheel/zero - aligning blocks to slice breaks squareshape

# ALGORITHMS
default_alg:
  alg: "3,-1/-2,4/0,3/2,-1/1,4/-1,0"
  description: hold any angle on top and preserve bird on bottom to go to snoopy/angel
other_algs:
  -
    alg: "0,-1/-2,4/3,0/-1,2/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Angel"
    short_name: "rsnoopy_angel"
mirrors:
  top_bot:
    -
      name: Left Zero / Right Pinwheel
      short_name: lzero_rpinwheel
  lr:
    -
      name: Left Pinwheel / Right Zero
      short_name: lpinwheel_rzero
  pseudo:
    -
      name: Left Pinwheel / Left Zero
      short_name: lpinwheel_lzero
    -
      name: Right Pinwheel / Right Zero
      short_name: rpinwheel_rzero


---

