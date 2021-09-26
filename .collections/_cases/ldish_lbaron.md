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

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/5,5/0,1"
  description: TODO
color_mirror_algs:
  -
    alg: "0,0/"
    description: TODO
other_algs:
  -
    alg: "0,0/"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
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

Description TODO

