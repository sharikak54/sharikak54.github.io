---
name: Left Red Baron / Right Satellite Dish
short_name: lbaron_rdish
top: Red Baron
top_short_name: baron
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
  top_bot:
    -
      name: Right Satellite Dish / Left Red Baron
      short_name: rdish_lbaron
  lr:
    -
      name: Right Red Baron / Left Satellite Dish
      short_name: rbaron_ldish
  pseudo:
    -
      name: Right Red Baron / Right Satellite Dish
      short_name: rbaron_rdish
    -
      name: Left Red Baron / Left Satellite Dish
      short_name: lbaron_ldish


---

Description TODO

