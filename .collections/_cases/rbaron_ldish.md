---
title: "Case: Right Baron / Left Dish"
name: Right Baron / Left Dish
short_name: rbaron_ldish
top: Baron
top_short_name: baron
top_lr: Right
bot: Dish
bot_short_name: dish
bot_lr: Left

optimal: 4

recognition: breaking baron/dish; preserving tents on top and putting slice between shell and gem on bottom breaks squareshape

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-3,0/-4,-1/0,1"
  description: put shell of dish in DL and align so slice breaks gem, preserve both tents in UL (goes to scottie/bird)
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Right Spill / Right Snoopy"
    short_name: "rspill_rsnoopy"
mirrors:
  top_bot:
    -
      name: Left Dish / Right Baron
      short_name: ldish_rbaron
  lr:
    -
      name: Left Baron / Right Dish
      short_name: lbaron_rdish
  pseudo:
    -
      name: Left Baron / Left Dish
      short_name: lbaron_ldish
    -
      name: Right Baron / Right Dish
      short_name: rbaron_rdish


---

