---
name: Left Satellite Dish / Right Red Baron
short_name: ldish_rbaron
top: Satellite Dish
top_short_name: dish
top_lr: Left
bot: Red Baron
bot_short_name: baron
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
        name: Right Red Baron / Left Satellite Dish
        short_name: rbaron_ldish
  -
    type: lr
    values: 
      -
        name: Right Satellite Dish / Left Red Baron
        short_name: rdish_lbaron
  -
    type: pseudo
    values: 
      -
        name: Right Satellite Dish / Right Red Baron
        short_name: rdish_rbaron
      -
        name: Left Satellite Dish / Left Red Baron
        short_name: ldish_lbaron


---

Description TODO

