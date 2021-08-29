---
name: Left Red Baron / Left Satellite Dish
short_name: lbaron_ldish
top: Red Baron
top_short_name: baron
top_lr: Left
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
  -
    type: top_bot
    values: 
      -
        name: Left Satellite Dish / Left Red Baron
        short_name: ldish_lbaron
  -
    type: lr
    values: 
      -
        name: Right Red Baron / Right Satellite Dish
        short_name: rbaron_rdish
  -
    type: pseudo
    values: 
      -
        name: Right Red Baron / Left Satellite Dish
        short_name: rbaron_ldish
      -
        name: Left Red Baron / Right Satellite Dish
        short_name: lbaron_rdish


---

Description TODO

