---
title: "Case: Left Dish / Left Baron"
name: Left Dish / Left Baron
short_name: ldish_lbaron
top: Dish
top_short_name: dish
top_lr: Left
bot: Baron
bot_short_name: baron
bot_lr: Left

optimal: 4

recognition: preserving dish/baron; putting slice between shell and gem on top and preserving tents on bottom preserves squareshape

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/5,-1/-3,0/0,1"
  description: put shell of dish in UL and align so slice preserves gem, swap gem with isolated corner on bottom
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "0,-1/-3,0/4,-2/-4,-1/0,1"
  -
    alg: "0,-1/-3,0/-2,4/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Whale / Right Whale"
    short_name: "rwhale_rwhale"
mirrors:
  top_bot:
    -
      name: Left Baron / Left Dish
      short_name: lbaron_ldish
  lr:
    -
      name: Right Dish / Right Baron
      short_name: rdish_rbaron
  pseudo:
    -
      name: Right Dish / Left Baron
      short_name: rdish_lbaron
    -
      name: Left Dish / Right Baron
      short_name: ldish_rbaron


---

