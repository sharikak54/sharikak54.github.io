---
name: Right Dish / Left Baron
short_name: rdish_lbaron
top: Dish
top_short_name: dish
top_lr: Right
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
      name: Left Baron / Right Dish
      short_name: lbaron_rdish
  lr:
    -
      name: Left Dish / Right Baron
      short_name: ldish_rbaron
  pseudo:
    -
      name: Left Dish / Left Baron
      short_name: ldish_lbaron
    -
      name: Right Dish / Right Baron
      short_name: rdish_rbaron


---

Description TODO

