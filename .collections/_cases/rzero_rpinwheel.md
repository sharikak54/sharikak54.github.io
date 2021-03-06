---
title: "Case: Right Zero / Right Pinwheel"
name: Right Zero / Right Pinwheel
short_name: rzero_rpinwheel
top: Zero
top_short_name: zero
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 4

recognition: Good zero/pinwheel - aligning blocks to slice preserves cubeshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/-3,3/-1,-4/0,1"
  description: Intentionally align both faces' blocks to go to good baron/baron.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "0,-1/1,4/3,-3/-4,-1/0,1"
  -
    alg: "0,2/4,1/-3,3/2,5/0,1"
  -
    alg: "1,0/-3,3/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "1,3/-3,3/-1,-1/1,-2/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Baron / Right Baron"
    short_name: "rbaron_rbaron"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Right Zero
      short_name: rpinwheel_rzero
  lr:
    -
      name: Left Zero / Left Pinwheel
      short_name: lzero_lpinwheel
  pseudo:
    -
      name: Left Zero / Right Pinwheel
      short_name: lzero_rpinwheel
    -
      name: Right Zero / Left Pinwheel
      short_name: rzero_lpinwheel


---

