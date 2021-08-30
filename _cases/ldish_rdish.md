---
name: Left Satellite Dish / Right Satellite Dish
short_name: ldish_rdish
top: Satellite Dish
top_short_name: dish
top_lr: Left
bot: Satellite Dish
bot_short_name: dish
bot_lr: Right

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,0/"
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
      name: Right Satellite Dish / Left Satellite Dish
      short_name: rdish_ldish
  pseudo:
    -
      name: Right Satellite Dish / Right Satellite Dish
      short_name: rdish_rdish
    -
      name: Left Satellite Dish / Left Satellite Dish
      short_name: ldish_ldish


---

Description TODO

