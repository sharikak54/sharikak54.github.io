---
title: "Case: Left Baron / Left Baron"
name: Left Baron / Left Baron
short_name: lbaron_lbaron
top: Baron
top_short_name: baron
top_lr: Left
bot: Baron
bot_short_name: baron
bot_lr: Left

optimal: 3

recognition: good baron/baron; preserving tents preserves cubeshape

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,3/4,1/-1,0"
  description: put all 4 tents on Right Kite and swap them to get dish/dish
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "0,-1/3,-3/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
mirrors:
  lr:
    -
      name: Right Baron / Right Baron
      short_name: rbaron_rbaron
  pseudo:
    -
      name: Right Baron / Left Baron
      short_name: rbaron_lbaron
    -
      name: Left Baron / Right Baron
      short_name: lbaron_rbaron


---

