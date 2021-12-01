---
title: "Case: Right Dish / Right Baron"
name: Right Dish / Right Baron
short_name: rdish_rbaron
top: Dish
top_short_name: dish
top_lr: Right
bot: Baron
bot_short_name: baron
bot_lr: Right

optimal: 4

recognition: Preserving dish/baron; putting slice between shell and gem on top and preserving tents on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/-5,1/3,0/-1,0"
  description: Put shell of dish in UL and align so slice preserves gem, swap gem with isolated corner on bottom.
other_algs:
  -
    alg: "1,0/3,0/-4,2/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Whale / Left Whale"
    short_name: "lwhale_lwhale"
mirrors:
  top_bot:
    -
      name: Right Baron / Right Dish
      short_name: rbaron_rdish
  lr:
    -
      name: Left Dish / Left Baron
      short_name: ldish_lbaron
  pseudo:
    -
      name: Left Dish / Right Baron
      short_name: ldish_rbaron
    -
      name: Right Dish / Left Baron
      short_name: rdish_lbaron


---

