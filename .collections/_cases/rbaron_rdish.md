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

