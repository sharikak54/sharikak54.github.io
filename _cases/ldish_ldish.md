---
name: Left Satellite Dish / Left Satellite Dish
short_name: ldish_ldish
top: Satellite Dish
top_short_name: dish
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
    type: lr
    values: 
      -
        name: Right Satellite Dish / Right Satellite Dish
        short_name: rdish_rdish
  -
    type: pseudo
    values: 
      -
        name: Right Satellite Dish / Left Satellite Dish
        short_name: rdish_ldish
      -
        name: Left Satellite Dish / Right Satellite Dish
        short_name: ldish_rdish


---

Description TODO

