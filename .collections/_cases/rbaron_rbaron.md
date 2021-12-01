---
title: "Case: Right Baron / Right Baron"
name: Right Baron / Right Baron
short_name: rbaron_rbaron
top: Baron
top_short_name: baron
top_lr: Right
bot: Baron
bot_short_name: baron
bot_lr: Right

optimal: 3

recognition: Good baron/baron; preserving tents preserves cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/3,-3/-4,-1/0,1"
  description: Put all 4 tents on right half of puzzle and swap them to get dish/dish.
other_algs:
  -
    alg: "1,0/-3,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
mirrors:
  lr:
    -
      name: Left Baron / Left Baron
      short_name: lbaron_lbaron
  pseudo:
    -
      name: Left Baron / Right Baron
      short_name: lbaron_rbaron
    -
      name: Right Baron / Left Baron
      short_name: rbaron_lbaron


---

