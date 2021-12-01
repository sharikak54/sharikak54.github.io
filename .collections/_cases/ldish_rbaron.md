---
title: "Case: Left Dish / Right Baron"
name: Left Dish / Right Baron
short_name: ldish_rbaron
top: Dish
top_short_name: dish
top_lr: Left
bot: Baron
bot_short_name: baron
bot_lr: Right

optimal: 4

recognition: Breaking dish/baron; putting slice between shell and gem on top and preserving tents on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/0,-3/-1,-4/0,1"
  description: Put shell of dish in UL and align so slice breaks gem, preserve both tents in DL (goes to good bird/scottie).
other_algs:
  -
    alg: "-5,6/3,0/0,-3/-4,-1/0,1"
  -
    alg: "-2,6/-3,0/0,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
  -
    name: "Right Snoopy / Right Spill"
    short_name: "rsnoopy_rspill"
mirrors:
  top_bot:
    -
      name: Right Baron / Left Dish
      short_name: rbaron_ldish
  lr:
    -
      name: Right Dish / Left Baron
      short_name: rdish_lbaron
  pseudo:
    -
      name: Right Dish / Right Baron
      short_name: rdish_rbaron
    -
      name: Left Dish / Left Baron
      short_name: ldish_lbaron


---

