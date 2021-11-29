---
title: "Case: Right Baron / Right Dish"
name: Right Baron / Right Dish
short_name: rbaron_rdish
top: Baron
top_short_name: baron
top_lr: Right
bot: Dish
bot_short_name: dish
bot_lr: Right

optimal: 4

recognition: Preserving baron/dish; preserving tents on top and putting slice between shell and gem on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-5,1/3,0/-1,0"
  description: Put shell of dish in DL and align so slice preserves gem, swap isolated corner on top with gem.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Left Whale / Left Whale"
    short_name: "lwhale_lwhale"
mirrors:
  top_bot:
    -
      name: Right Dish / Right Baron
      short_name: rdish_rbaron
  lr:
    -
      name: Left Baron / Left Dish
      short_name: lbaron_ldish
  pseudo:
    -
      name: Left Baron / Right Dish
      short_name: lbaron_rdish
    -
      name: Right Baron / Left Dish
      short_name: rbaron_ldish


---

