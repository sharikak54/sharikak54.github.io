---
title: "Case: Left Dish / Left Dish"
name: Left Dish / Left Dish
short_name: ldish_ldish
top: Dish
top_short_name: dish
top_lr: Left
bot: Dish
bot_short_name: dish
bot_lr: Left

optimal: 2

recognition: Good dish/dish; thumbs are the same as each other, or making a kite on one face makes a kite on the other face.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-1,0"
  description: Keep bottom shell in DL, pair gem on top with isolated corner on bottom to form kite/kite.
color_mirror_algs:
  -
    alg: "0,-1/-2,-5/-1,0"
  -
    alg: "6,5/5,2/-1,0"
other_algs:
  -
    alg: "6,5/-1,-4/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Kite / Right Kite"
    short_name: "rkite_rkite"
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

