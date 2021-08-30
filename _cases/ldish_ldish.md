---
name: Left Dish / Left Dish
short_name: ldish_ldish
top: Dish
top_short_name: dish
top_lr: Left
bot: Dish
bot_short_name: dish
bot_lr: Left

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
  lr:
    -
      name: Right Dish / Right Dish
      short_name: rdish_rdish
  pseudo:
    -
      name: Right Dish / Left Dish
      short_name: rdish_ldish
    -
      name: Left Dish / Right Dish
      short_name: ldish_rdish


---

Description TODO

