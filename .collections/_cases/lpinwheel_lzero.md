---
title: "Case: Left Pinwheel / Left Zero"
name: Left Pinwheel / Left Zero
short_name: lpinwheel_lzero
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 4

recognition: Good pinwheel/zero - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-3,3/4,1/-1,0"
  description: Intentionally misalign both faces' blocks to go to good baron/baron.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "-2,0/-1,-4/-3,3/-5,-2/-1,0"
  -
    alg: "0,-1/-3,3/1,1/-1,2/0,3/0,1"
  -
    alg: "0,-1/3,-3/1,1/-4,-1/-3,0/0,1"
  -
    alg: "3,-1/-3,3/1,1/3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Baron / Left Baron"
    short_name: "lbaron_lbaron"
mirrors:
  top_bot:
    -
      name: Left Zero / Left Pinwheel
      short_name: lzero_lpinwheel
  lr:
    -
      name: Right Pinwheel / Right Zero
      short_name: rpinwheel_rzero
  pseudo:
    -
      name: Right Pinwheel / Left Zero
      short_name: rpinwheel_lzero
    -
      name: Left Pinwheel / Right Zero
      short_name: lpinwheel_rzero


---

