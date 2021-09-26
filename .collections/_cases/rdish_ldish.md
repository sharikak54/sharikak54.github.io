---
title: "Case: Right Dish / Left Dish"
name: Right Dish / Left Dish
short_name: rdish_ldish
top: Dish
top_short_name: dish
top_lr: Right
bot: Dish
bot_short_name: dish
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
  lr:
    -
      name: Left Dish / Right Dish
      short_name: ldish_rdish
  pseudo:
    -
      name: Left Dish / Left Dish
      short_name: ldish_ldish
    -
      name: Right Dish / Right Dish
      short_name: rdish_rdish


---

Description TODO

