---
title: "Case: Left Zero / Right Pinwheel"
name: Left Zero / Right Pinwheel
short_name: lzero_rpinwheel
top: Zero
top_short_name: zero
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 5

recognition: Bad zero/pinwheel - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,4/3,0/2,-1/4,1/-1,0"
  description: Preserve bird on top and hold any angle on bottom to go to angel/snoopy.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "0,2/-2,4/0,3/-1,2/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Angel / Right Snoopy"
    short_name: "angel_rsnoopy"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Left Zero
      short_name: rpinwheel_lzero
  lr:
    -
      name: Right Zero / Left Pinwheel
      short_name: rzero_lpinwheel
  pseudo:
    -
      name: Right Zero / Right Pinwheel
      short_name: rzero_rpinwheel
    -
      name: Left Zero / Left Pinwheel
      short_name: lzero_lpinwheel


---

