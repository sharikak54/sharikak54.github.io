---
name: Left Satellite Dish / Left Red Baron
short_name: ldish_lbaron
top: Satellite Dish
top_short_name: dish
top_lr: Left
bot: Red Baron
bot_short_name: baron
bot_lr: Left

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
  top_bot:
    -
      name: Left Red Baron / Left Satellite Dish
      short_name: lbaron_ldish
  lr:
    -
      name: Right Satellite Dish / Right Red Baron
      short_name: rdish_rbaron
  pseudo:
    -
      name: Right Satellite Dish / Left Red Baron
      short_name: rdish_lbaron
    -
      name: Left Satellite Dish / Right Red Baron
      short_name: ldish_rbaron


---

Description TODO

