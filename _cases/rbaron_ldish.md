---
name: Right Red Baron / Left Satellite Dish
short_name: rbaron_ldish
top: Red Baron
top_short_name: baron
top_lr: Right
bot: Satellite Dish
bot_short_name: dish
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
      name: Left Satellite Dish / Right Red Baron
      short_name: ldish_rbaron
  lr:
    -
      name: Left Red Baron / Right Satellite Dish
      short_name: lbaron_rdish
  pseudo:
    -
      name: Left Red Baron / Left Satellite Dish
      short_name: lbaron_ldish
    -
      name: Right Red Baron / Right Satellite Dish
      short_name: rbaron_rdish


---

Description TODO

