---
name: Left Dish / Right Baron
short_name: ldish_rbaron
top: Dish
top_short_name: dish
top_lr: Left
bot: Baron
bot_short_name: baron
bot_lr: Right

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/5,5/0,1"
  description: TODO
mirror_algs:
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
      name: Right Baron / Left Dish
      short_name: rbaron_ldish
  lr:
    -
      name: Right Dish / Left Baron
      short_name: rdish_lbaron
  pseudo:
    -
      name: Right Dish / Right Baron
      short_name: rdish_rbaron
    -
      name: Left Dish / Left Baron
      short_name: ldish_lbaron


---

Description TODO

