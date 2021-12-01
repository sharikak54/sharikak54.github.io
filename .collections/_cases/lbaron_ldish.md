---
title: "Case: Left Baron / Left Dish"
name: Left Baron / Left Dish
short_name: lbaron_ldish
top: Baron
top_short_name: baron
top_lr: Left
bot: Dish
bot_short_name: dish
bot_lr: Left

optimal: 4

recognition: Preserving baron/dish; preserving tents on top and putting slice between shell and gem on bottom preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/5,-1/-3,0/0,1"
  description: Put shell of dish in DL and align so slice preserves gem, swap isolated corner on top with gem.
other_algs:
  -
    alg: "0,-1/0,-3/4,-2/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Whale / Right Whale"
    short_name: "rwhale_rwhale"
mirrors:
  top_bot:
    -
      name: Left Dish / Left Baron
      short_name: ldish_lbaron
  lr:
    -
      name: Right Baron / Right Dish
      short_name: rbaron_rdish
  pseudo:
    -
      name: Right Baron / Left Dish
      short_name: rbaron_ldish
    -
      name: Left Baron / Right Dish
      short_name: lbaron_rdish


---

