---
name: Right Red Baron / Right Satellite Dish
short_name: rbaron_rdish
top: Red Baron
top_short_name: baron
top_lr: Right
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
  -
    type: top_bot
    values: 
      -
        name: Right Satellite Dish / Right Red Baron
        short_name: rdish_rbaron
  -
    type: lr
    values: 
      -
        name: Left Red Baron / Left Satellite Dish
        short_name: lbaron_ldish
  -
    type: pseudo
    values: 
      -
        name: Left Red Baron / Right Satellite Dish
        short_name: lbaron_rdish
      -
        name: Right Red Baron / Left Satellite Dish
        short_name: rbaron_ldish


---

Description TODO

