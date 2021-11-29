---
title: "Case: Right Pinwheel / Right Zero"
name: Right Pinwheel / Right Zero
short_name: rpinwheel_rzero
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 4

recognition: good pinwheel/zero - aligning blocks to slice preserves squareshape

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-3,3/-1,-4/0,1"
  description: intentionally misalign both faces' blocks to go to good baron/baron
other_algs:
  -
    alg: "3,-1/1,4/-3,3/2,5/0,1"
  -
    alg: "1,0/-3,3/-1,-1/4,1/3,0/-1,0"
  -
    alg: "-2,0/-3,3/-1,-1/-2,1/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Baron / Right Baron"
    short_name: "rbaron_rbaron"
mirrors:
  top_bot:
    -
      name: Right Zero / Right Pinwheel
      short_name: rzero_rpinwheel
  lr:
    -
      name: Left Pinwheel / Left Zero
      short_name: lpinwheel_lzero
  pseudo:
    -
      name: Left Pinwheel / Right Zero
      short_name: lpinwheel_rzero
    -
      name: Right Pinwheel / Left Zero
      short_name: rpinwheel_lzero


---

