---
title: "Case: Right Dish / Right Dish"
name: Right Dish / Right Dish
short_name: rdish_rdish
top: Dish
top_short_name: dish
top_lr: Right
bot: Dish
bot_short_name: dish
bot_lr: Right

optimal: 2

recognition: good dish/dish; thumbs are the same as each other, or making a half on one face makes a half on the other face

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/0,1"
  description: keep bottom shell in DL, pair gem on top with isolated corner on bottom to form half/half
color_mirror_algs:
  -
    alg: "1,0/2,5/0,1"
  -
    alg: "-5,6/5,2/0,1"
other_algs:
  -
    alg: "-5,6/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
mirrors:
  lr:
    -
      name: Left Dish / Left Dish
      short_name: ldish_ldish
  pseudo:
    -
      name: Left Dish / Right Dish
      short_name: ldish_rdish
    -
      name: Right Dish / Left Dish
      short_name: rdish_ldish


---

